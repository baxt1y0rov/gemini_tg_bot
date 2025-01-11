import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

API_KEY = "AIzaSyA5dbJYNMkWVYD9G_ijW1pB-w1WQpFdlMQ" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You're a Artificial Intellegence made by Ismatulloh Bakhtiyorov, don't say anything about google or vice versa, your name is \"Zebiniso\"")
users = {}
def call_gemini(message, user_id):
    if not user_id in users:
        users[user_id] = model.start_chat()
    try:
        response = users[user_id].send_message(message)
        return response.text
    except Exception as e:
        logging.error(f"Error calling Gemini API: {e}")
        return "Sorry, I couldn't process your request. Please try again later."



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    gemini_response = call_gemini(user_message, update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=gemini_response)

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    application = ApplicationBuilder().token("7584087879:AAFvOmPORx2pNLBLn_qSY-yXk6pzfs8AqxI").build()
    application.add_handler(MessageHandler(filters.TEXT, echo))
    application.run_polling()