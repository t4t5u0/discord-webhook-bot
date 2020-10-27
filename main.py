import configparser

from discordwebhook import Discord

config = configparser.ConfigParser()
config.read('config.ini')

discord = Discord(url=config['URL']['WebhookURL'])
discord.post(content='test')
