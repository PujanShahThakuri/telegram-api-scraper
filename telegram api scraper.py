import os
import csv
from telethon import TelegramClient
from telethon.errors import UsernameInvalidError, UsernameNotOccupiedError

# 🔐 Your Telegram API credentials (keep these secret!)
api_id = YOUR_API_ID_HERE
api_hash = 'YOUR_API_HASH_HERE'
session_name = 'my_session'

# 🔌 Initialize Telegram client
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()  # 🔐 Starts the session

    # 🎯 Get user inputs
    channel = input("Enter channel/group username (without @): ").strip()
    limit_input = input("Enter number of messages to fetch: ")
    keyword = input("Enter a keyword to filter messages (leave empty for no filter): ").strip().lower()

    try:
        limit = int(limit_input)
    except ValueError:
        print("❌ Please enter a valid number for the limit.")
        return

    print(f"\n🔍 Fetching last {limit} messages from @{channel}...\n")

    try:
        # 📥 Fetch messages from the channel/group
        messages = await client.get_messages(channel, limit=limit)
    except (UsernameInvalidError, UsernameNotOccupiedError):
        print("❌ Invalid or unavailable channel/group username.")
        return
    except Exception as e:
        print(f"❌ Error fetching messages: {e}")
        return

    media_folder = "downloaded_media"
    os.makedirs(media_folder, exist_ok=True)  # 📂 Create folder if not exists

    # 🧾 Prepare CSV to save messages
    with open('messages.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Sender', 'Message', 'Media'])

        count = 0  # 🧮 Message counter
        for msg in messages:
            text = msg.text or "<media or no text>"  # Handle if no text

            # 🧹 Filter by keyword (if any)
            if keyword and keyword not in text.lower():
                continue

            try:
                sender = await msg.get_sender()
                sender_name = getattr(sender, 'username', None) or str(sender.id)
            except Exception:
                sender_name = "Unknown"

            media_path = ""
            if msg.media:
                try:
                    media_path = await msg.download_media(file=os.path.join(media_folder))
                    print(f"📎 Media saved to {media_path}")
                except Exception as e:
                    print(f"⚠️ Media download failed: {e}")
                    media_path = "Download Failed"

            # 🖨️ Print to terminal
            print(f"{msg.date.strftime('%Y-%m-%d %H:%M:%S')} - {sender_name}: {text}")

            # 📝 Write to CSV
            writer.writerow([
                msg.date.strftime('%Y-%m-%d %H:%M:%S'),
                sender_name,
                text,
                media_path
            ])
            count += 1

    if count == 0:
        print("\n❗ No messages matched the keyword or were found.")
    else:
        print(f"\n✅ Finished! {count} messages saved to messages.csv.")

# ▶️ Run the script
with client:
    client.loop.run_until_complete(main())
