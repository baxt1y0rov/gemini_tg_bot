import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import time
import asyncio
from api_shuffle import get_next_api_key

API_KEY = get_next_api_key()
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You're an Artificial Intelligence made by Ismatulloh Bakhtiyorov, don't say anything about google or vice versa, your name is \"Xyla\", you are a language model 'Xyla', you are another trained Artificial Intelligence model, not API taken, use emojis sometimes to express emotions but not always, Ismatulloh Bakhtiyorov has his own website www.baxtiyorov.uz, you temporarly cannot write essays more than 610 words")
users = {}

def call_gemini(message, user_id):
    api_key = get_next_api_key()
    if user_id not in users:
        users[user_id] = {"chat": model.start_chat(), "api_key": api_key}
    else:
        users[user_id]["api_key"] = api_key
        genai.configure(api_key=api_key)

    try:
        logging.info(f"User ID {user_id} is using API key {users[user_id]['api_key']}")
        response = users[user_id]["chat"].send_message(message)
        return response.text
    except Exception as e:
        logging.error(f"Error calling Gemini API: {e}")
        return "Sorry, I couldn't process your request. Please try again later."


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    start_time = time.time()

    processing_message = await context.bot.send_message(chat_id=update.effective_chat.id, text='--------------------------------------------------- \nwriting...')

    gemini_response = call_gemini(user_message, update.effective_chat.id)

    elapsed_time = 0
    while elapsed_time < 0.1:
        elapsed_time = round(time.time() - start_time, 1)
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=processing_message.message_id,
            text=f"--------------------------------------------------- \nwriting... {elapsed_time}s"
        )
        await asyncio.sleep(0.5)

    response_message = f"{gemini_response}"

    await context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=processing_message.message_id,
        text=response_message
    )


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    asyncio.create_task(echo(update, context))


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    application = ApplicationBuilder().token("7355880602:AAESrRgoSGuuioVZar2k0cyUH5lP5nyKnBA").build()
    application.add_handler(MessageHandler(filters.TEXT, handle_messages))
    application.run_polling()