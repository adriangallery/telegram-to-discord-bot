import telebot
import requests
import os

# Configuración desde variables de entorno
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_ID = int(os.getenv("TELEGRAM_GROUP_ID"))
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
BOT_COMPRAS_ID = int(os.getenv("BOT_COMPRAS_ID"))  # ID del bot de compras

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: message.chat.id == TELEGRAM_GROUP_ID and message.from_user.id == BOT_COMPRAS_ID)
def forward_to_discord(message):
    data = {"content": f"📢 **Nuevo mensaje del bot de compras:**\n\n{message.text}"}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

bot.polling()
