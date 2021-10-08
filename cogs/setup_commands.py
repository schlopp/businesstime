import io
from PIL import Image, ImageDraw, ImageFont

import discord
from discord.ext import commands, vbu

from . import utils


class SetupCommands(vbu.Cog):
    @commands.command("create")
    @utils.checks.is_slash_command()
    @vbu.checks.bot_is_ready()
    async def _create_card_command(self, ctx: vbu.Context):
        """
        Creates a new awesome business card. \u1F60E
        """

        with io.BytesIO() as f:
            background_image_name = r"cardboard.png"
            background_image_path = fr"images\cards\{background_image_name}"

            # Load background image and resize to default card size
            image: Image.Image = Image.open(background_image_path)
            image.resize(utils.DEFAULT_CARD_SIZE)

            draw = ImageDraw.Draw(image)
            card_content = f"{ctx.author}'s test card"
            card_content_width, card_content_height = draw.textsize(card_content)
            draw.text(
                ((utils.DEFAULT_CARD_WIDTH - card_content_width) // 2 , (utils.DEFAULT_CARD_HEIGHT - card_content_height) // 2),
                card_content,
                fill=(255, 255, 0),
            )

            image.save(f, "png")
            f.seek(0)
            await ctx.interaction.response.send_message(
                "Done! Take a look at your new beautiful business card!",
                file=discord.File(f, "card.png"),
            )


def setup(bot: vbu.Bot):
    x = SetupCommands(bot)
    bot.add_cog(x)
