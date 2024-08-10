import datetime
from telethon import TelegramClient

# Your API ID and API Hash
api_id = '22936363'
api_hash = '86c3044a784370034e29370c5016b7a1'
# The phone number associated with your Telegram account
phone_number = '972527346155'

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)


async def main():
    # Connect to the Telegram server
    await client.start(phone=phone_number)

    # Get the group entity using its username or invite link
    group = await client.get_entity('https://t.me/ahwalaltreq')

    # Define the specific date and time range
    specific_date = datetime.date(2024, 5, 24)
    myHour = 23

    # Iterate through the messages
    async for message in client.iter_messages(group, limit=50):
        # Convert the message date to UTC+3
        message_date_utc_plus_3 = message.date + datetime.timedelta(hours=3)

        # Check if the message date matches the specific date
        if message_date_utc_plus_3.date() == specific_date:
            # Extract the hour of the message
            message_hour = message_date_utc_plus_3.hour

            # Check if the message hour is within the specified range
            if message_hour == myHour:
                date_only = message_date_utc_plus_3.date()
                time_only = message_date_utc_plus_3.time().strftime('%H:%M')
                print(f"Date and Time (UTC+3): {message_date_utc_plus_3}")
                print(f"Date (UTC+3): {date_only}")
                print(f"Time (UTC+3): {time_only}")
                print(f"Message: {message.text}")
                print("-" * 40)
            else:
                print("Wow Breaked")
                break

    # Disconnect the client
    await client.disconnect()


# Run the client
with client:
    client.loop.run_until_complete(main())
