from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5217526382:AAFfplJcrL_UhRpE6nwDi7tyyqxYJS0Vypc", use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Welcome to the hood_code_bot. Type\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/youtube - To get youtube URL
	/linkedin - To get LinkedIn URL
	/github - To get Github URL""")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"LinkedIn URL => \
		https://uk.linkedin.com/")


def github_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Github URL => https://github.com/")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
