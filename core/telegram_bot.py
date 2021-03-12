import telegram
from core import config


def prepare_bot():
    # We need the telegram bot token and group id to send the message.
    try:
        if config.BOT_TOKEN == "" or not config.BOT_TOKEN:
            print('Error: BOT_TOKEN is not set')
            quit()
        if config.GROUP_ID == "" or not config.GROUP_ID:
            print('Error: GROUP_ID is not set')
            quit()
        return telegram.Bot(token=config.BOT_TOKEN)
    except:
        print('Error: parsing config file, BOT_TOKEN or GROUP_ID may be missing')
        quit()


def send_message(bot, message):
    bot.send_message(config.GROUP_ID, message, parse_mode=telegram.ParseMode.MARKDOWN)


def send_data(msg):
    telegram.Bot(token=config.BOT_TOKEN)
    bot = prepare_bot()
    message = msg
    send_message(bot, message)
