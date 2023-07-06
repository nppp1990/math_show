from manimlib import *


def get_right_angle(point, x, y, **kwargs):
    line1 = Line(point + x + y, point + x, **kwargs)
    line2 = Line(point + x + y, point + y, **kwargs)
    return VGroup(line1, line2)


def get_right_angle_by_points(point1, point2, point3, size=0.3, **kwargs):
    x = Line(point2, point1).get_unit_vector() * size
    y = Line(point2, point3).get_unit_vector() * size
    return get_right_angle(point2, x, y, **kwargs)


def add_right_arrow(obj, length=0.8, **kwargs):
    arrow = Line(obj.get_right() + 0.2 * RIGHT, obj.get_right() + RIGHT * (length + 0.2), **kwargs)
    arrow.add_tip(width=0.16, length=0.16)
    return arrow


def add_arrow_from_to(pos1, pos2, **kwargs):
    arrow = Line(pos1, pos2, **kwargs)
    arrow.add_tip(width=0.16, length=0.16)
    return arrow


def get_rect(obj, **kwargs):
    """ 给obj加框，以obj为中心
    """
    # 默认color为白色
    return Rectangle(
        width=obj.get_width() + 2 * (kwargs["buff"] if "buff" in kwargs else 0.1),
        height=obj.get_height() + 2 * (kwargs["buff"] if "buff" in kwargs else 0.1),
        **kwargs
    ).set_color(
        kwargs["color"] if "color" in kwargs else WHITE
    ).move_to(obj.get_center())
