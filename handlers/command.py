from telegram.ext import CommandHandler
import callbacks.command as callback

start_handler = CommandHandler('start', callback.start)
generate_handler = CommandHandler('generate', callback.generate)