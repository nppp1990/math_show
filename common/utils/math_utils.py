from manimlib import *


def cal_triangle_angle(point1, point2, point3):
    vector1 = point1 - point2
    vector2 = point3 - point2
    return np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))


def cal_dis(point1, point2):
    return np.linalg.norm(point1 - point2)
