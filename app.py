import datetime
from telethon import TelegramClient
from flask import Flask, render_template_string

app = Flask(__name__)

# Your API ID and API Hash
api_id = '22936363'
api_hash = '86c3044a784370034e29370c5016b7a1'
phone_number = '972527346155'

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

@app.route('/')
async def main():
    messages = []
    # Connect to the Telegram server
    await client.start(phone=phone_number)
    
    # Get the group entity using its username or invite link
    group = await client.get_entity('https://t.me/hasancryptogram')
    
    # Get messages from the group sent in the last day
    now = datetime.datetime.now(datetime.timezone.utc)
    yesterday = now - datetime.timedelta(days=1)
    
    async for message in client.iter_messages(group, offset_date=yesterday, reverse=True, limit=100):
        messages.append({
            'sender_id': message.sender_id,
            'date': message.date,
            'text': message.text
        })
    
    # Disconnect the client
    await client.disconnect()
    
    # Render messages in a simple HTML template
    html_template = '''
    <!doctype html>
    <html>
    <head><title>Telegram Messages</title></head>
    <body>
    <h1>Telegram Messages</h1>
    {% for msg in messages %}
      <div>
        <strong>Sender ID:</strong> {{ msg.sender_id }}<br>
        <strong>Date and Time:</strong> {{ msg.date }}<br>
        <strong>Message:</strong> {{ msg.text }}<br>
        <hr>
      </div>
    {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html_template, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
