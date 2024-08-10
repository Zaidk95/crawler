import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
import pandas as pd
import re
import os

# Use your own values from my.telegram.org
api_id = '22936363'
api_hash = '86c3044a784370034e29370c5016b7a1'
client = TelegramClient('Zaid-Groups', api_id, api_hash)

# Specify the group username
group_username = 'JobAndShop'

async def main():
    global group_username

    # Connect to the client
    await client.start()

    # Get the full channel information
    group = await client(GetFullChannelRequest(channel=group_username))

    # Collect data from the group
    await collect_data(group)

async def collect_data(group):
    group_entity = group.chats[0]

    # Collect messages
    messages = []
    async for message in client.iter_messages(group_entity.id, limit=1000):
        messages.append(message.text)

    # Collect links from messages
    links = set()
    for message in messages:
        found_links = re.findall(r"https://t\.me/[\w]+", message)
        links.update(found_links)

    print(f"Collected {len(messages)} messages and {len(links)} links from {group_entity.title}")
    print(f"Links: {links}")

with client:
    client.loop.run_until_complete(main())
