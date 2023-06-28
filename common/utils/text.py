from manimlib import *


def create_bottom_tip(text, color_map=None, **kwargs):
    """底部文案"""
    if color_map is None:
        color_map = {}
    if kwargs.get('color') is None:
        kwargs.setdefault('color', BLACK)

    tip = Text(text, **kwargs,
               t2c=color_map).scale(0.8).move_to(np.array([0, -3.5, 0]))
    tip.set_color_by_text_to_color_map(color_map)
    return tip
