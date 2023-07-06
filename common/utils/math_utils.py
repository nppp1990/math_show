from manimlib import *


def cal_triangle_angle(point1, point2, point3):
    vector1 = point1 - point2
    vector2 = point3 - point2
    return np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))


def cal_triangle_angle2(point1, point2, point3):
    # 逆时针从3到1的度数
    if point1[1] == point3[1]:
        if point3[0] < point2[0]:
            # 3在2的左边
            return np.pi
        else:
            # 3在2的右边
            return 0
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


def get_circle_center_from_triangle(point1, point2, point3):
    # 获取三角形的外接圆圆心坐标、克拉默法则
    # 三角形的外接圆圆心坐标为：(x,y)
    # A1=2*(x2-x1)；B1=2*(y2-y1)；C1=x2^2+y2^2-x1^2-y1^2；
    a1 = 2 * (point2[0] - point1[0])
    b1 = 2 * (point2[1] - point1[1])
    c1 = point2[0] ** 2 + point2[1] ** 2 - point1[0] ** 2 - point1[1] ** 2
    # A2=2*(x3-x2)；B2=2*(y3-y2)；C2=x3^2+y3^2-x2^2-y2^2；
    a2 = 2 * (point3[0] - point2[0])
    b2 = 2 * (point3[1] - point2[1])
    c2 = point3[0] ** 2 + point3[1] ** 2 - point2[0] ** 2 - point2[1] ** 2
    # x=((C1*B2)-(C2*B1))/((A1*B2)-(A2*B1))；
    # y=((A1*C2)-(A2*C1))/((A1*B2)-(A2*B1))；
    x = ((c1 * b2) - (c2 * b1)) / ((a1 * b2) - (a2 * b1))
    y = ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2 * b1))
    return np.array([x, y, 0])


def get_cross_point(pos1, pos2, pos3, pos4):
    # 两条线的交叉点
    # pos1 pos2为第一条线的两个端点
    # pos3 pos4为第二条线的两个端点
    # 两条线的方程分别为：
    # (y-y1)/(x-x1)=(y2-y1)/(x2-x1)
    # (y-y3)/(x-x3)=(y4-y3)/(x4-x3)
    # 两条线的交叉点为：
    # x=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    pos_x = ((pos1[0] * pos2[1] - pos1[1] * pos2[0]) * (pos3[0] - pos4[0]) - (pos1[0] - pos2[0]) * (
            pos3[0] * pos4[1] - pos3[1] * pos4[0])) / (
                    (pos1[0] - pos2[0]) * (pos3[1] - pos4[1]) - (pos1[1] - pos2[1]) * (pos3[0] - pos4[0]))
    pos_y = ((pos1[0] * pos2[1] - pos1[1] * pos2[0]) * (pos3[1] - pos4[1]) - (pos1[1] - pos2[1]) * (
            pos3[0] * pos4[1] - pos3[1] * pos4[0])) / (
                    (pos1[0] - pos2[0]) * (pos3[1] - pos4[1]) - (pos1[1] - pos2[1]) * (pos3[0] - pos4[0]))
    return np.array([pos_x, pos_y, 0])


def draw_polygon_line(*points: np.ndarray, **kwargs):
    # line画多边形
    # points为多边形的顶点坐标
    lines = []
    for i in range(len(points) - 1):
        lines.append(Line(points[i], points[i + 1], **kwargs))
    lines.append(Line(points[-1], points[0], **kwargs))
    return VGroup(*lines)


def get_lines_vertices(polygon_line_group):
    vertices = []
    for line in polygon_line_group:
        vertices.append(line.get_start())
    return vertices
