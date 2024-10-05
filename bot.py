from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import logging
import os

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Fungsi start untuk menampilkan tombol
async def start(update: Update, context) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Contact Information", callback_data='contact'),
            InlineKeyboardButton("Instagram", callback_data='instagram'),
        ],
        [
            InlineKeyboardButton("Feedback", callback_data='feedback'),
            InlineKeyboardButton("Payment", callback_data='payment'),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose an option:', reply_markup=reply_markup)

# Fungsi untuk menangani tombol yang ditekan
async def button(update: Update, context) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'contact':
        await query.edit_message_text(text="Contact Information: \nEmail: contact@yourwebsite.com\nPhone: +123456789")
    elif query.data == 'instagram':
        await query.edit_message_text(text="Follow us on Instagram: https://instagram.com/yourprofile")
    elif query.data == 'feedback':
        await query.edit_message_text(text="Please send your feedback to feedback@yourwebsite.com")
    elif query.data == 'payment':
        await query.edit_message_text(text="Payment Options:\n1. Bank Transfer\n2. PayPal: https://paypal.me/yourprofile")

# Main function to run the bot
async def main():
    token = os.getenv("7461649635:AAGymS_mF5Rf_hJatJEEiLia819_Bq3nq7Q")  # Mengambil token dari variabel environment Railway
    application = Application.builder().token(token).build()

    # Daftarkan handler /start
    application.add_handler(CommandHandler("start", start))

    # Daftarkan handler untuk tombol
    application.add_handler(CallbackQueryHandler(button))

    # Jalankan polling bot
    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
