from traceback import print_exception
from ..constants import EMBED_ERROR_TITLE, EMBED_ERROR_COLOR

from crescent import Client, Context, GatewayTraits
from hikari import Embed


class SubClient(Client):
    def __init__(self, app: GatewayTraits, *args, **kwargs):
        super().__init__(app, *args, **kwargs)

    async def on_crescent_command_error(
        self, exc: Exception, ctx: Context, *args, **kwargs
    ) -> None:
        description = f"`{exc.__class__.__name__}: {exc}`"
        # fmt: off
        embed = Embed(
            title=EMBED_ERROR_TITLE,
            description=description,
            color=EMBED_ERROR_COLOR,
        )
        # fmt: on

        await ctx.respond(embed=embed)
        print_exception(exc.__class__, exc, exc.__traceback__)
