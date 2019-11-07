import neural
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot

# Settings
TOKEN = '1023230889:AAEAuFDVPXMNpOd9o7ZWE7AjEEJAEDzx2LA'
REQUEST_KWARGS = {
    'proxy_url': 'http://167.172.140.175:3128/',
}


def start(update, context):
    update.message.reply_text(
        'Здравстуй! Отправь мне картинку и я скажу тебе их класс.')


def image(update, context):
    update.effective_message.photo[-1].get_file().download('./img/image.jpg')
    update.message.reply_text(neural.main())


def main():
    updater = Updater(TOKEN,  use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, image))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
