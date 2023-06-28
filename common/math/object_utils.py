from manimlib import *


def get_right_angle(point, x, y, stroke_width=4):
    line1 = Line(point + x + y, point + x).set_stroke(width=stroke_width)
    line2 = Line(point + x + y, point + y).set_stroke(width=stroke_width)
    return VGroup(line1, line2)


def add_right_arrow(obj):
    arrow = Line(obj.get_right() + 0.2 * RIGHT, obj.get_right() + RIGHT)
    arrow.add_tip(width=0.16, length=0.16)
    return arrow


def get_rect(obj, **kwargs):
    """ 给obj加框，以obj为中心
    """
    return Rectangle(
        width=obj.get_width() + 2 * kwargs["buff"],
        height=obj.get_height() + 2 * kwargs["buff"],
        **kwargs
    ).set_color(kwargs["color"]).move_to(obj.get_center())