import configparser
from utils.persistence import bot_persistence

config = configparser.ConfigParser()
config.read('config.ini')

# Bot
bot_token_test = config['BOT']['TOKEN_TEST']
bot_token = config['BOT']['TOKEN']
proxy = config['BOT']['PROXY']

# Admin
admins = {}
NUM = 4
for i in range(NUM):
  admins.update({config[f'ADMIN_{i}']['NAME']: config[f'ADMIN_{i}']['ID']})

# Test(with proxy)
# update_info = {
#   'token': bot_token_test,
#   'use_context': True,
#   'request_kwargs': {
#     'proxy_url':proxy
#   },
#   'persistence':bot_persistence
# }


# Build
update_info = {
  'token': bot_token,
  'use_context': True,
  'persistence':bot_persistence
} 

