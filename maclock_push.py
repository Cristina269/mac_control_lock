import telegram
from telegram.ext import Updater
import mac
import time
from functools import wraps
from telegram.ext import Updater


def main():

    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    timer = updater.job_queue
    import logging

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    from telegram import Update
    from telegram.ext import CallbackContext


    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="/doge")


    def status(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=mac.lock_status())


    def lock(update: Update, context: CallbackContext):
        # context.bot.send_message(chat_id=update.effective_chat.id, text=maclock.into_sleep_mode())
        context.bot.send_message(chat_id=update.effective_chat.id, text=mac.into_sleep_mode())


    def screen(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=mac.enter_screen_saver())


    from telegram.ext import CommandHandler

    start_handler = CommandHandler('start', start)
    status_handler = CommandHandler('status', status)
    lock_handler = CommandHandler('lock', lock)
    screen_handler = CommandHandler('screen', screen)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(status_handler)
    dispatcher.add_handler(lock_handler)
    dispatcher.add_handler(screen_handler)
    updater.start_polling()


    def delete(update: Update, context: CallbackContext):
        context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.effective_message.id)


    def callback_minute(context: telegram.ext.CallbackContext):
        result = context.bot.send_message(chat_id=your_chat_id,
                                          text=mac.lock_status())
        message_id = result['message_id']
        time.sleep(58)
        context.bot.deleteMessage(chat_id=your_chat_id, message_id=message_id)


    timer.run_repeating(callback_minute, interval=60, first=1)

# 这里换成你的bot_token 和 chat_id
bot_token = ''
your_chat_id = ''

try:
    main()
except:
    time.sleep(10)
    main()