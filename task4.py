from telethon import TelegramClient

api_id = 'personal_api_id'
api_hash = 'personal_api_hash'

client = TelegramClient('my_session', api_id, api_hash)

async def main():
    target_group = 'entity' # ID, username, або запрошувальне посилання групи/каналу/чату
    
    print(f"Учасники групи {target_group}")
    async for user in client.iter_participants(target_group):
        username = user.username if user.username else "No Username"
        print(f"ID: {user.id} | Name: {user.first_name} | User: @{username}")

    receiver = 'entity' # ID, username, або запрошувальне посилання групи/каналу/чату
    message = 'Hi! This is a test message from Telethon.'
    
    await client.send_message(receiver, message)
    print(f"\nMessage sent to user {receiver}")

with client:
    client.loop.run_until_complete(main())