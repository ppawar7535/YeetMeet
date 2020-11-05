import os 
class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '1406378056:AAHjK7XkUCU_NrExrYv6BFkANrrLXzfO_84') 
    USERNAME = os.environ.get('USERNAME', '') 
    PASSWORD = os.environ.get('PASSWORD', '')
