import requests
import re
from config import admins
from utils.persistence import bot_persistence

class IdeaPoster(object):
  def __init__(self):
    self.info = {}
    self.info_styled = ''
    self.note = ''
    bot_data = bot_persistence.get_bot_data()
    self.cached_links = []
    if bot_data:
      self.cached_links = bot_data['cached_links']

  def is_liqi(self, url):
    pattern = r'.*liqi\.io.*'
    return bool(re.match(pattern, url))

  def is_cached(self, link):
    if link in self.cached_links:
      return True
    else:
      self.cached_links.append(link)
      if len(self.cached_links) > 30:
        self.cached_links.pop(0)
      return False

  def is_kk(self, author):
    pattern = r' 凯文·'
    return re.match(pattern, author)

  def fetch_idea(self):
    self.info = requests.get('https://q24.io/api/v1/idea').json()
    self.redir_link_req = requests.get(self.info['url'],allow_redirects=False)
    self.redir_link = self.redir_link_req.headers['Location']

  def update(self):
    self.fetch_idea()
    while self.is_cached(self.info['url']) or self.is_kk(self.info['author']):
      self.fetch_idea()
    if self.info['note']:
      curator_id = str(admins[self.info['curator']])
      self.info['note'] = self.info['note'].rstrip('。')
      self.note = f"{self.info['note']}：(via [{self.info['curator']}](tg://user?id={curator_id}))\n\n" 
    else:
      self.note = None
  
    if self.is_liqi(self.redir_link):
      url_styled = f"https://t.me/iv?url={self.redir_link}&rhash=7610e8062aab10"
    else: 
      url_styled = self.redir_link
    self.info_styled = f"{self.info['idea']}  [‣]({url_styled})\n\n—— {self.info['author']}" + (f" ({self.info['intro']})" if self.info['intro'] else '')
  def post(self, context):
    self.update()
    if self.note:
      self.info_styled = self.note + self.info_styled
    context.bot.send_message(
      chat_id='@uselessideas', 
      text=self.info_styled, 
      parse_mode='Markdown'
    )
    context.bot_data['cached_links'] = self.cached_links
    bot_persistence.flush()
