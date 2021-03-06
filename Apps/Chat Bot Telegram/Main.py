
import logging
from telegram.ext import *
import Response

API_KEY = '1917620048:AAHXGQg5XQojEuJigkUebRGKNyVkG5TX_z4'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hola como estas?! Soy\'un bot. En que puedo\' ayudarte?')


def help_command(update, context):
    update.message.reply_text('¡Intente escribir cualquier cosa y haré todo lo posible para responder!')


def custom_command(update, context):
    update.message.reply_text('Este es un comando personalizado, puede agregar el texto que desee aquí.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = Response.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()