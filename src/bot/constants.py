from . import __version__
from hikari import Color, Activity, Status


ACTIVITY = Activity(name=f"v{__version__}")
STATUS = Status.IDLE

EMBED_STANDART_COLOR = Color.from_rgb(159, 157, 207)
EMBED_ERROR_COLOR = Color.from_rgb(255, 75, 75)
EMBED_ERROR_TITLE = "Ошибка"

CONFIG_PATH = './config.json'
CONTENTS_PATH = "./src/bot/commands/contents/"