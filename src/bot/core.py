from hikari import GatewayBot
from .modules.config import Config
from .subclasses.subclient import SubClient


bot = GatewayBot(Config.TOKEN, banner="src.bot")
client = SubClient(bot)

client.plugins.load_folder("src.bot.commands.plugins")