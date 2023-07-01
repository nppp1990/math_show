from manimlib import *


def cal_triangle_angle(point1, point2, point3):
    vector1 = point1 - point2
    vector2 = point3 - point2
    return np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))


def cal_triangle_angle2(point1, point2, point3):
    # 逆时针从3到1的度数
    if point3[1] > point2[1]:
        return cal_triangle_angle(point1, point2, point3)
    else:
        return 2 * np.pi - cal_triangle_angle(point1, point2, point3)


def draw_arc(point1, point2, point3, **kwargs):
    angle_1 = cal_triangle_angle2(point2 + RIGHT, point2, point1)
    angle_2 = cal_triangle_angle2(point2 + RIGHT, point2, point3)
    # angle_1 angle_2 min
    return Arc(
        angle=cal_triangle_angle(point1, point2, point3),
        start_angle=min(angle_1, angle_2),
        arc_center=point2,
        **kwargs
    )

def cal_dis(point1, point2):
    return np.linalg.norm(point1 - point2)


def get_vertical_line(point1, point2, anticlockwise=True, length=1):
    # point1、point2的垂线，起点为point1, anticlockwise为True时，垂线在point1到point2的逆时针方向
    vector = point2 - point1
    if anticlockwise:
        vector = np.array([-vector[1], vector[0], 0])
    else:
        vector = np.array([vector[1], -vector[0], 0])
    vector = vector / np.linalg.norm(vector) * length
    return Line(point1, point1 + vector)


def get_vertical_point(point1, point2, anticlockwise=True, length=1):
    vector = point2 - point1
    if anticlockwise:
        vector = np.array([-vector[1], vector[0], 0])
    else:
        vector = np.array([vector[1], -vector[0], 0])
    vector = vector / np.linalg.norm(vector) * length
    return point1 + vector
