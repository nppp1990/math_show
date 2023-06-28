from manimlib import *


def get_rect2(obj, **kwargs):
    """ 给obj加框，以obj为中心
    """
    return Rectangle(
        width=obj.get_width() + 2 * kwargs["buff"],
        height=obj.get_height() + 2 * kwargs["buff"],
        **kwargs
    ).move_to(obj.get_center())


def swap(i, j):
    temp = i
    i = j
    j = temp


def swap_arr(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def get_circle(obj, **kwargs):
    """ 给obj加框，以obj为中心
    """
    return Circle(
        radius=max(obj.get_width(), obj.get_height()) / 2 + kwargs["buff"],
        **kwargs
    ).move_to(obj.get_center())


def get_del_line(obj, **kwargs):
    """ 给obj删除线，以obj为中心
    """
    return Line(obj.get_left(), obj.get_right(), **kwargs)


def get_path_by_points(points: [np.ndarray], **args):
    """points构成的路径列表"""
    pre = points[0]
    path = []
    for item in points[1:]:
        path.append(Line(pre, item, **args))
        pre = item
    return path


def connect_circle(circle1: Circle, circle2: Circle, **args):
    """连接两个Circle的线"""
    line_center = Line(circle1.get_center(), circle2.get_center())
    unit_vector = line_center.get_unit_vector()
    start, end = line_center.get_start_and_end()
    new_start = start + unit_vector * circle1.get_radius()
    new_end = end - unit_vector * circle2.get_radius()
    return Line(new_start, new_end)


def hide_object(scene: Scene, obj: Mobject):
    """隐藏object"""
    obj.set_color(scene.camera.background_color)


def get_angle(p1, p2, center):
    return np.arctan2(p2[1] - center[1], p2[0] - center[0]) - np.arctan2(p1[1] - center[1], p1[0] - center[0])
