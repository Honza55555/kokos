import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "перейдите по этой ссылке: "
        "http://account-oblivion-portal.lovable.app/"
    )

def main():
    # token vlož Render jako env var TELEGRAM_BOT_TOKEN
    token = os.environ['TELEGRAM_BOT_TOKEN']
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    # spustíme long-polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
