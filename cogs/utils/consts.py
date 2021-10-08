import typing

from PIL import ImageFont


DEFAULT_CARD_WIDTH: int = 600
DEFAULT_CARD_HEIGHT: int = 400
DEFAULT_CARD_SIZE: typing.Tuple[int, int] = (DEFAULT_CARD_WIDTH, DEFAULT_CARD_HEIGHT)


MIN_FONT_SIZE: int = 5
MAX_FONT_SIZE: int = 50
DEFAULT_FONT_SIZE: dict = 26

ROBOTO_LIGHT = {}
for i in range(MIN_FONT_SIZE, MAX_FONT_SIZE + 1):
    ROBOTO_LIGHT[i] = ImageFont.truetype("assets/fonts/Roboto-Light.ttf", size=i)

DEFAULT_FONT: dict = ROBOTO_LIGHT
