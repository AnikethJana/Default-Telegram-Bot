# bot.py
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Initialize Flask
app = Flask(__name__)

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "@your-update-channel")
OFFLINE_MESSAGE = os.getenv("OFFLINE_MESSAGE", f"⚠️ The bot is currently offline. Please check {UPDATE_CHANNEL} for updates.")

# Initialize bot application
bot = Application.builder().token(BOT_TOKEN).build()

async def handle_message(update: Update, context):
    """Handle all incoming messages with the offline message"""
    await update.message.reply_text(OFFLINE_MESSAGE)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    """Handle incoming webhook updates"""
    update = Update.de_json(request.get_json(), bot.bot)
    bot.process_update(update)
    return "OK", 200

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for cloud platform"""
    return "OK", 200

# Register message handler
bot.add_handler(MessageHandler(filters.ALL, handle_message))

if __name__ == "__main__":
    # Set webhook URL based on environment
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("WEBHOOK_URL environment variable is required")
    
    bot.set_webhook(url=f"{webhook_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=8000)