import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.common.utils.utils import connect_circle
from yj.common.utils.utils import get_del_line


def create_point(name: str):
    return VGroup(Circle(color=WHITE).scale(0.4), Tex(name).set_color(YELLOW).scale(0.4))


def create_line(point1, point2, weight: int):
    line = connect_circle(point1[0], point2[0]).add_tip(width=0.2, length=0.2)
    unit_vector = line.get_unit_vector()
    # 垂直向量
    unit_vector2 = np.array([-unit_vector[1], unit_vector[0], 0]) * 0.2
    weight = Tex(str(weight)).move_to(line.get_center()).set_color(YELLOW_A).scale(0.7).shift(unit_vector2)
    return VGroup(line, weight)


# 度数为0
def get_in(visited: [], degree: []):
    for i in range(len(degree)):
        if visited[i] == 0 and degree[i] == 0:
            return i
    return -1


class DragSort(Scene):
    def construct(self) -> None:
        title = Title("图-关键路径的计算").scale(0.9).shift(UP * 0.2)
        self.add(title)
        matrix, point_group, line_list, line_map = self.draw_graph()
        # 如图这是一个带权值的有向无环图AOE
        # 介绍下有AOE关键路径长度的计算方法
        self.wait(5)
        self.show_desc(matrix, point_group, line_list, line_map)
        self.wait(2)
        self.show_process1(matrix, point_group, line_list, line_map)
        self.wait(10)
        # self.add(*line_list)
        # self.wait(8)

    def draw_graph(self):
        point1 = create_point("V1")
        point2 = create_point("V2").shift(UP + RIGHT * 2)
        point3 = create_point("V3").shift(DOWN + RIGHT * 1.8)
        point4 = create_point("V4").shift(DOWN * 1.1 + RIGHT * 3.7)
        point5 = create_point("V5").shift(UP * 1.2 + RIGHT * 4)
        point6 = create_point("V6").shift(UP * 1.3 + RIGHT * 6.6)
        point7 = create_point("V7").shift(DOWN * 0.1 + RIGHT * 5.1)
        point8 = create_point("V8").shift(DOWN * 1.4 + RIGHT * 6.3)
        point9 = create_point("V9").shift(DOWN * 0.8 + RIGHT * 8.3)
        point10 = create_point("V10").shift(UP * 0.1 + RIGHT * 10.3)
        point_group = VGroup(point1, point2, point3, point4,
                             point5, point6, point7, point8,
                             point9, point10).shift(LEFT * 5 + UP * 0.95)

        size = 10
        matrix = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]
        matrix[0][1] = 5
        matrix[0][2] = 6
        matrix[1][4] = 3
        matrix[2][4] = 6
        matrix[2][3] = 3
        matrix[3][4] = 3
        matrix[3][6] = 1
        matrix[3][7] = 4
        matrix[4][5] = 4
        matrix[4][6] = 2
        matrix[5][9] = 4
        matrix[6][8] = 5
        matrix[7][8] = 2
        matrix[8][9] = 2

        line_list = []

        line_map = [
            [None for _ in range(size)]
            for _ in range(size)
        ]

        for i in range(size):
            for j in range(size):
                if matrix[i][j] > 0:
                    line = create_line(point_group[i], point_group[j], matrix[i][j])
                    line_list.append(line)
                    line_map[i][j] = line

        self.add(point_group, VGroup(*line_list))
        return matrix, point_group, line_list, line_map

    def show_desc(self, matrix, point_group, line_list, line_map):
        route = [0, 2, 4, 6, 8, 9]
        example = []
        for i in range(len(route) - 1):
            pre_index = route[i]
            next_index = route[i + 1]
            point = point_group[pre_index][0].copy().set_color(BLACK)
            line = line_map[pre_index][next_index][0].copy().set_color(BLACK)
            example.append(point)
            example.append(line)
            self.play(ShowCreation(point, run_time=1))
            self.play(ShowCreation(line, run_time=1))
        point = point_group[9][0].copy().set_color(BLACK)
        example.append(point)
        self.play(ShowCreation(point, run_time=1))

        self.wait(3)

        str1 = Text("事件的最早发生时间", font="Menlo", color=WHITE).scale(0.7).shift(DOWN)
        str2 = Text("事件的最晚发生时间", font="Menlo", color=WHITE).scale(0.7).shift(DOWN)
        str3 = Text("活动的最早开始时间", font="Menlo", color=WHITE).scale(0.7).shift(DOWN)
        str4 = Text("活动的最晚结束时间", font="Menlo", color=WHITE).scale(0.7).shift(DOWN)
        str_group = VGroup(str1, str2, str3, str4).arrange(DOWN).shift(DOWN * 2)
        self.play(FadeIn(str_group, run_time=2))

        # 黑人问号
        self.wait(7)
        del_lines = VGroup(
            get_del_line(str1, color=RED),
            get_del_line(str2, color=RED),
            get_del_line(str3, color=RED),
            get_del_line(str4, color=RED)
        )
        self.play(ShowCreation(del_lines, run_time=3))

        # 利用拓扑排序来计算关键路径
        self.wait(3)
        self.play(FadeOut(del_lines), FadeOut(str_group))
        self.remove(VGroup(*example))

    def get_dis_text(self, point_group, i, dis):
        if i == 4:
            return Tex(str(dis)).set_color(BLACK).scale(0.7).next_to(point_group[i], UP, buff=0.1)
        else:
            return Tex(str(dis)).set_color(BLACK).scale(0.7).next_to(point_group[i], DOWN, buff=0.1)

    def show_process1(self, matrix, point_group, line_list, line_map):
        size = len(matrix)

        degree = []
        visited = [0 for _ in range(size)]
        weights = [0 for _ in range(size)]
        value_list = [None for _ in range(size)]

        for i in range(size):
            v = 0
            for j in range(size):
                if matrix[j][i] > 0:
                    v += 1
            degree.append(v)

        # print(degree)
        # print(visited)
        visited_size = 0
        self.play(ShowCreation(self.get_dis_text(point_group, 0, 0)))
        # 用一个数组存放起点到每个顶点的临时关键路径长度，开始为0
        # 咱们打草稿就直接写在顶点旁边就行
        self.wait(3)
        while visited_size < size:
            in_index = get_in(visited, degree)
            # 随机找一个入度为0的点
            self.play(
                ShowCreation(point_group[in_index][0].copy().set_color(BLACK)),
                Indicate(point_group[in_index][1], color=YELLOW, scale_factor=1.4)
            )
            # self.wait(2)
            visited_size += 1
            visited[in_index] = 1
            if visited_size == 1:
                # 讲解：随机找一个入度为0的顶点
                self.wait(4)
            for j in range(size):
                if matrix[in_index][j] > 0:
                    line = line_map[in_index][j][0].copy().set_color(BLACK)
                    self.play(ShowCreation(line))
                    old_text = value_list[j]
                    max_dis = max(weights[j], weights[in_index] + matrix[in_index][j])
                    weights[j] = max_dis
                    new_text = self.get_dis_text(point_group, j, max_dis)
                    if old_text is None:
                        self.play(ShowCreation(new_text))
                        value_list[j] = new_text
                    else:
                        self.play(Transform(old_text, new_text))
                    if visited_size == 1:
                        # 讲解：遍历从这个顶点出发的边：并且更新到达点的关键路径长度
                        # 讲解：取较大的更新
                        self.wait(5)
                    elif visited_size == 2:
                        self.wait(8)
                    degree[j] = degree[j] - 1
                    self.remove(line_map[in_index][j][0])
                    self.play(
                        FadeOut(line),
                        FadeOut(line_map[in_index][j][1]),
                    )
                    if visited_size == 1:
                        # 讲解：更新临时关键路径后，删除对应的边
                        self.wait(3)


class Test(Scene):
    def construct(self) -> None:
        # v = Integer(1, group_with_commas=False, fill_color=BLACK, color=BLACK).set_color(BLACK)
        # self.add(v)
        # v.set_value(1233456)
        rect = Rectangle()
        self.add(rect)

        line = Line(LEFT * 3, LEFT + UP * 2).shift(UP * 2)
        self.add(line)

        text = Text("123").move_to(line.get_center())
        self.add(text)
