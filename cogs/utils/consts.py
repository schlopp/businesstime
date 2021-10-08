import typing

from PIL import ImageFont


DEFAULT_CARD_WIDTH: int = 600
DEFAULT_CARD_HEIGHT: int = 400
DEFAULT_CARD_SIZE: typing.Tuple[int, int] = (DEFAULT_CARD_WIDTH, DEFAULT_CARD_HEIGHT)

DEFAULT_FONT_SIZE = 20

ROBOTO_LIGHT: ImageFont.ImageFont = ImageFont.truetype(
    "assets/fonts/Roboto-Light.ttf", size=DEFAULT_FONT_SIZE
)
DEFAULT_FONT: ImageFont.ImageFont = ROBOTO_LIGHT
