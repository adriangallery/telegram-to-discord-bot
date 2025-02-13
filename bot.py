import telebot
import requests
import os

# Configuración desde variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_ID = int(os.getenv("TELEGRAM_GROUP_ID"))
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: message.chat.id == TELEGRAM_GROUP_ID)
def forward_to_discord(message):
    data = {"content": f"📢 **Nuevo mensaje en Telegram:**\n\n{message.text}"}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

bot.polling()
