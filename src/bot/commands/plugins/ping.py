from ...constants import CONTENTS_PATH
from ...constants import EMBED_STANDART_COLOR

from crescent import command
from crescent import Plugin, Context
from hikari import Embed


plugin = Plugin()

NAME = "ping"
DESCRIPTION = None


@plugin.include
@command(name=NAME, description=DESCRIPTION)
class PingCommand():
    async def callback(self, ctx: Context) -> None:
        with open(CONTENTS_PATH + "ping.txt") as stream:
            content = stream.read()

        self.id__ = str(ctx.user.id)
        # fmt: off
        self.embed = Embed(
            title=DESCRIPTION,
            color=EMBED_STANDART_COLOR
        )
        # fmt: on

        self.embed.description = content

        await ctx.respond(embed=self.embed)
