from config import admins

def is_admin(id_):
  return str(id_) in admins.values()