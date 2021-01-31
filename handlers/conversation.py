from telegram.ext import ConversationHandler, CallbackQueryHandler
from handlers.command import start_handler, generate_handler

GENERATE, = range(1)

conversation_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        GENERATE: [generate_handler]
    },
    fallbacks=[start_handler],
    allow_reentry=True
)