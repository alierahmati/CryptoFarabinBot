from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 CryptoFarabinBot فعال شد.\n\n"
        "دستورات:\n"
        "/btc"
    )

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    price = requests.get(url).json()["price"]

    await update.message.reply_text(
        f"💰 قیمت لحظه‌ای بیت‌کوین:\n{price} USDT"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("Bot Started...")
app.run_polling()