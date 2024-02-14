This python project watches new messages in Telegram groups that a user is included, and then forward the messages to a specific group based on a list of keywords.
1. Get all the Telegram groups/channels where's my user is added
2. Get new messages based on keywords list from these groups/channels
3. Forward them to a specific group/channel
4. This group/channel has a bot that receives the message and then send it to the logged user

See the steps below for the correct execution of this project:

1. Create a Telegram bot:
	1.1 Open Telegram and search for the user @BotFather
	1.2 Type '/newbot' on Telegram message input
	1.3 Open the docker-compose.yml
	1.4 Set up the environment variable 'TELEGRAM_BOT_API_HASH' to the hash code provided by @BotFather
2. Create a Telegram group/channel
3. Add the bot as admin of this group/channel
4. Open the group/channel you created in step 1.2 and dicover the ID:
	4.1. Click to edit the group/channel
	4.2. Go to Settings > Statistics and Boosts
	4.3. See the URL in 'Link for boosting'
	4.4. The ID is the number after 'c' parameter (i.e. t.me/boost?c=<CHANNEL_ID/GROUP_ID>)
	4.4. Open the docker-compose.yml
	4.5. Set up the environment variable 'TELEGRAM_RECIPIENT_ID' with: -100<CHANNEL_ID/GROUP_ID>
5. Set Telegram API:
	5.1. Open https://my.telegram.org/apps 
	5.2. Put your telephone number used for Telegram
	5.3. Set the App Title, Short Name and save
	5.4. Open the docker-compose.yml
	5.5. Set up the environment variable 'TELEGRAM_API_ID' with the App user_id, provided by Telegram
	5.6. Set up the environment variable 'TELEGRAM_API_HASH' with the App api_hash, provided by Telegram
6. If it's the first time you're running this project, you have to save the session string:
	6.1. Open a terminal and run this:
		6.1.1. cd <your_project_dir>
		6.1.2. python save_session.py
	6.2. Copy the output string
	6.3. Open Open the docker-compose.yml
	6.4. Paste the output string to the environment variable 'TELEGRAM_API_STRING'
7. Add the keywords you want into the file 'keywords.txt'
	7.1 Add each keyword in each line of the file
8. Configure Docker:
	8.1. Open terminal and the commands below
		8.1.1. Build image: docker build -t telegram-watcher .
		8.1.2. Create and run container: docker compose up