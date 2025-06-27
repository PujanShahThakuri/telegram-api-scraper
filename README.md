📄 Telegram Message Scraper
This Python script uses the Telethon library to fetch messages from any public Telegram group or channel. It allows filtering messages by keyword, saves results to a .csv file, and downloads any attached media.

🔧 Features
Fetch messages from public Telegram groups/channels

Optional keyword filter (case-insensitive)

Downloads media files (photos, videos, documents, etc.)

Saves messages in a structured messages.csv file

Clean and beginner-friendly code with comments

📦 Requirements
Python 3.7+

Telethon

Install Telethon using pip:

bash
Copy
Edit
pip install telethon
🔐 Setup
Go to my.telegram.org and log in.

Click on API Development Tools.

Create a new app and get your:

api_id

api_hash

🛠️ Usage
Replace placeholder values in the script:

python
Copy
Edit
api_id = YOUR_API_ID_HERE
api_hash = 'YOUR_API_HASH_HERE'
Run the script:

bash
Copy
Edit
python your_script_name.py
Follow the prompts:

Enter the Telegram group/channel username (without @)

Enter how many messages to fetch

Enter a keyword (optional) to filter messages

The script will:

Save media files to the downloaded_media/ folder

Save messages to messages.csv

📁 Output Files
messages.csv – Stores message date, sender, content, and media path

downloaded_media/ – Folder for all downloaded media files

🚫 Do Not Share
Your real api_id and api_hash

Your .session file (used to maintain login)

📄 .gitignore Suggestion
Add the following to .gitignore to protect sensitive files:

gitignore
Copy
Edit
*.session
downloaded_media/
messages.csv
.env
✅ License
This project is for educational and personal use. Use responsibly and follow Telegram's Terms of Service.

