from handlers.conversation import conversation_handler
from handlers.message import message_handler

handlers = [conversation_handler, message_handler]

def register(dispatcher):
  for handler in handlers:
    dispatcher.add_handler(handler)