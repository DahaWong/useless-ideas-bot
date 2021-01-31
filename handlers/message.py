from telegram.ext import MessageHandler,Filters
from callbacks.command import generate

message_handler = MessageHandler(Filters.command, generate)