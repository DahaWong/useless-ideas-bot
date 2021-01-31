from utils.authorize import is_admin
from utils.post_idea import IdeaPoster
from utils.persistence import bot_persistence

def start(update, context):
  user_id = update.effective_user.id
  if is_admin(user_id):
    context.user_data['is_admin'] = True
    bot_persistence.flush()
    update.message.reply_text(f'嗨，{update.effective_user.first_name}。\n点击 /generate 即可生成一条灵感发到频道。')
    return 0
  else:
    context.user_data['is_admin'] = False
    bot_persistence.flush()
    update.message.reply_text("抱歉，您没有使用权限。")
    return -1

def generate(update, context):
  if context.user_data.__contains__('is_admin'):
    if context.user_data['is_admin']:
      poster = IdeaPoster()
      poster.post(context)
      print(context.bot_data)
      return 0
    else:
      update.message.reply_text("抱歉，您没有使用权限。")
      return -1
  else:
    start(update, context)

