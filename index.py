import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

API_KEY = "AIzaSyA5dbJYNMkWVYD9G_ijW1pB-w1WQpFdlMQ" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def call_gemini(message):
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        logging.error(f"Error calling Gemini API: {e}")
        return "Sorry, I couldn't process your request. Please try again later."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! I'm a Gemini chatbot. Ask me anything!",
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    gemini_response = call_gemini(user_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=gemini_response)

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    application = ApplicationBuilder().token("7813832218:AAGOfg63_YxFgNbRER0X34eJ7ShWPW9sLR8").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()