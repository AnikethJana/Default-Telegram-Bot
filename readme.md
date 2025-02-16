# 📢 Telegram Offline Bot

A simple and efficient Telegram bot that notifies users when it is offline. The bot automatically responds to all messages with a notification and provides a link to the official update channel. Offline message is customizable as per User requirements.

---

## ✨ Features
- ✅ Allows users to customize the offline message.
- ✅ Provides an update channel link for further updates.

---

## 📋 Requirements
- 🐍 Python 3.8+
- 🤖 Telegram Bot Token (Obtain from [BotFather](https://t.me/BotFather))

---

## ⚙️ Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/anikethjana/Default-Telegram-Bot.git
   cd Default-Telegram-Bot
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Add the following to  `.env`**
   ```sh
   BOT_TOKEN=your_telegram_bot_token
   WEBHOOK_URL=your_application_url
   UPDATE_CHANNEL=@your_channel_name
   OFFLINE_MESSAGE=your_custom_message
   ```
4. **Replace** `your-bot-token-here` and `@your-update-channel` with actual values.

---
## 🐳 Docker Deployment
**1️⃣ Run with Docker Compose**
```sh
docker-compose up --build -d
```

---
## ▶️ Usage
Run the bot with:
```sh
python3 bot.py
```
The bot will now automatically respond to all messages with the custom offline message you set in environment variables. The bot also includes a simple Flask web UI that displays a dark-themed invite page to your Telegram channel.

---

## 📜 License
This project is licensed under the **MIT License**.

---
