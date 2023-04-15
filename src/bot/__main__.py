from os import name
from .core import bot
from .web.app import run
from threading import Thread
from .constants import ACTIVITY, STATUS

from uvloop import install


if name != 'nt':
    install()

server = Thread(target=run)
server.start()

# fmt: off
bot.run(
    activity=ACTIVITY,
    status=STATUS,
    asyncio_debug=True
)
# fmt: on