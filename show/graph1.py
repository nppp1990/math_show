import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.math_show.common.utils.utils import connect_circle
from yj.math_show.common.utils.utils import hide_object
from yj.math_show.common.utils.utils import get_rect2

color_map_graph1 = {
    "1.": "#A0A0A0",
    "2.": "#A0A0A0",
    "3.": "#A0A0A0",
    "4.": "#A0A0A0",
    "5.": "#A0A0A0",
    "typedef": "#000080",
    "struct": "#000080",
    "int": "#000080",
    "char": "#000080",
    "index": "#7B2F8C",
    "value": "#7B2F8C",
    "next": "#7B2F8C",
    "ArcNode": "#7B2F8C",
    "{": BLACK,
    "}": BLACK,
    ";": BLACK,
}


def create_code(text):
    code = Text(text, color="#808080",
                font_size=19,
                slant=ITALIC,
                t2c=color_map_graph1,
                t2s={'1.': NORMAL, '2.': NORMAL, '3.': NORMAL, '4.': NORMAL},
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map_graph1)
    return code


class Graph1(Scene):
    def construct(self) -> None:
        self.draw_graph_matrix1()
        self.wait(3)
        self.clear()
        self.draw_graph_matrix2()
        self.wait(3)
        self.clear()
        self.draw_adj_table()
        self.wait(3)
        self.clear()
        self.draw_adj_table2()
        self.wait(5)

    def draw_graph_matrix1(self):
        title = Title("无向图-邻接矩阵").scale(0.9)
        self.add(title)
        matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
        integer_matrix, x_text_group, y_text_group, matrix_group = self.draw_matrix(matrix)
        point_group = self.draw_point()
        self.draw_line(matrix, integer_matrix, point_group)

    def draw_graph_matrix2(self):
        title = Title("无向图-邻接矩阵").scale(0.9)
        self.add(title)
        matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]

        # 画点和线
        point1, point2, point3, point4 = self.create_point()
        point_group = VGroup(point1, point2, point3, point4).move_to(ORIGIN)
        lines = []
        line_map = [[None, None, None, None],
                    [None, None, None, None],
                    [None, None, None, None],
                    [None, None, None, None]]
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix)):
                if matrix[i][j] == 1:
                    line = connect_circle(point_group[i][0], point_group[j][0])
                    line_map[i][j] = line
                    line_map[j][i] = line
                    lines.append(line)
        graph = VGroup(point_group, *lines)
        self.add(graph)
        self.wait(2)
        self.play(graph.shift, LEFT * 3 + UP * 1)
        self.wait()
        graph.save_state()

        arrow = Line(LEFT * 0.8, RIGHT * 0.8, stroke_width=15, color=YELLOW).shift(UP + LEFT * 0.2)
        arrow.add_tip(width=0.4, length=0.4)
        self.play(ShowCreation(arrow))

        # 画矩阵
        integer_matrix, x_text_group, y_text_group, matrix_group = self.create_matrix(matrix)
        matrix_group.shift(RIGHT * 3 + UP * 0.8)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                hide_object(self, integer_matrix.mob_matrix[i][j])
        self.add(matrix_group)

        number_text = None
        for i in range(0, len(matrix)):
            self.wait(1)
            self.play(point_group[i][0].set_color, BLACK)
            self.wait(1)
            for j in range(0, len(matrix)):
                number = Text("matrix[" + str(i) + "][" + str(j) + "]=" + str(matrix[i][j]), font="Menlo",
                              color=BLUE).scale(0.7).shift(DOWN)
                if number_text is None:
                    number_text = number
                if matrix[i][j] == 1:
                    self.play(
                        Indicate(line_map[i][j]),
                        Indicate(point_group[j]),
                        Transform(number_text, number),
                        integer_matrix.mob_matrix[i][j].set_color, WHITE
                    )
                else:
                    self.play(
                        Indicate(point_group[j]),
                        Transform(number_text, number),
                        integer_matrix.mob_matrix[i][j].set_color, WHITE
                    )

        self.wait(2)
        self.play(FadeOut(number_text),
                  graph.restore)
        self.wait(1)
        number_text = Text("matrix[1][3]=" + str(matrix[1][3]), font="Menlo", color=BLUE).scale(0.7).shift(DOWN)

        self.play(
            Indicate(point2),
            Indicate(point4),
            Indicate(integer_matrix.mob_matrix[1][3]),
            Write(number_text),
        )
        graph.save_state()
        integer_matrix.save_state()
        point2.set_color(YELLOW)
        point4.set_color(YELLOW)
        integer_matrix.mob_matrix[1][3].set_color(YELLOW)

        self.wait(2)
        graph.restore()
        integer_matrix.restore()
        self.remove(number_text)

        self.wait(2)
        self.play(Indicate(point1))
        point1.set_color(YELLOW)
        rect = get_rect2(VGroup(
            integer_matrix.mob_matrix[0][0],
            integer_matrix.mob_matrix[0][1],
            integer_matrix.mob_matrix[0][2],
            integer_matrix.mob_matrix[0][3],
        ), buff=0.1, stroke_color=YELLOW, stroke_width=2)
        self.play(ShowCreation(rect))
        for i in range(0, len(matrix)):
            self.wait()
            self.play(Indicate(integer_matrix.mob_matrix[0][i], scale_factor=1.6))

    def create_matrix(self, matrix):
        integer_matrix = IntegerMatrix(matrix, v_buff=1, h_buff=1)
        x_text_group = VGroup(
            Tex("V1").set_color(YELLOW).scale(0.75),
            Tex("V2").set_color(YELLOW).scale(0.75),
            Tex("V3").set_color(YELLOW).scale(0.75),
            Tex("V4").set_color(YELLOW).scale(0.75),
        ).arrange(RIGHT, buff=0.5).next_to(integer_matrix.mob_matrix[0][0], UP, aligned_edge=LEFT)
        y_text_group = VGroup(
            Tex("V1").set_color(YELLOW).scale(0.75),
            Tex("V2").set_color(YELLOW).scale(0.75),
            Tex("V3").set_color(YELLOW).scale(0.75),
            Tex("V4").set_color(YELLOW).scale(0.75),
        ).arrange(DOWN, buff=0.75).next_to(integer_matrix.mob_matrix[0][0], LEFT, aligned_edge=UP, buff=0.7)
        matrix_group = VGroup(integer_matrix, x_text_group, y_text_group).scale(0.7)
        return integer_matrix, x_text_group, y_text_group, matrix_group

    def draw_matrix(self, matrix):
        integer_matrix, x_text_group, y_text_group, matrix_group = self.create_matrix(matrix)
        self.add(integer_matrix)
        self.wait(2)

        text = Text("任意的i、j满足：").scale(0.85)
        tex = Tex("A[i][j]=A[j][i]").set_color(BLUE).scale(0.75).next_to(text, RIGHT)
        tip = VGroup(text, tex).next_to(integer_matrix, DOWN).scale(0.9)
        self.play(Write(tip))
        self.wait()
        self.remove(tip)
        text = Text("例如：").scale(0.85)
        tex = Tex("A[1][2]=A[2][1]").set_color(BLUE).scale(0.75).next_to(text, RIGHT)
        tip = VGroup(text, tex).next_to(integer_matrix, DOWN).scale(0.9)
        self.play(
            Write(tip, run_time=1),
            Indicate(integer_matrix.mob_matrix[1][2], color=BLUE, scale_factor=2, run_time=1.5),
            Indicate(integer_matrix.mob_matrix[2][1], color=BLUE, scale_factor=2, run_time=1.5)
        )
        self.wait(1)
        tex2 = Tex("A[2][3]=A[3][2]").set_color(BLUE).scale(0.75).next_to(text, RIGHT)
        self.play(
            Transform(tex, tex2, run_time=1),
            Indicate(integer_matrix.mob_matrix[2][3], color=BLUE, scale_factor=2, run_time=1.5),
            Indicate(integer_matrix.mob_matrix[3][2], color=BLUE, scale_factor=2, run_time=1.5)
        )
        self.play(FadeOut(tip))
        self.wait(2)

        self.play(integer_matrix.shift, LEFT * 3 + UP * 1, run_time=1.5)
        x_text_group.shift(LEFT * 3 + UP * 1)
        y_text_group.shift(LEFT * 3 + UP * 1)
        self.wait()
        self.play(Write(x_text_group))
        self.play(Write(y_text_group))
        self.wait(2)
        return integer_matrix, x_text_group, y_text_group, matrix_group

    def create_point(self):
        point1 = VGroup(Circle(color=WHITE).scale(0.4), Tex("V1").set_color(YELLOW).scale(0.6))
        point2 = VGroup(Circle(color=WHITE).scale(0.4), Tex("V2").set_color(YELLOW).scale(0.6)).next_to(
            point1, DOWN, buff=1.3)
        point3 = VGroup(Circle(color=WHITE).scale(0.4), Tex("V3").set_color(YELLOW).scale(0.6)).next_to(
            point2, RIGHT, buff=1.3)
        point4 = VGroup(Circle(color=WHITE).scale(0.4), Tex("V4").set_color(YELLOW).scale(0.6)).next_to(
            point1, RIGHT, buff=1.3)
        return point1, point2, point3, point4

    def draw_point(self):
        point1, point2, point3, point4 = self.create_point()
        point_group = VGroup(point1, point2, point3, point4).move_to(ORIGIN + RIGHT * 3 + UP * 1)

        arrow = Line(LEFT * 0.8, RIGHT * 0.8, stroke_width=15, color=YELLOW).shift(UP)
        arrow.add_tip(width=0.4, length=0.4)
        self.play(ShowCreation(arrow))

        self.play(ShowCreation(point1, run_time=0.5))
        self.play(ShowCreation(point2, run_time=0.5))
        self.play(ShowCreation(point3, run_time=0.5))
        self.play(ShowCreation(point4, run_time=0.5))
        self.wait(2)
        return point_group

    def draw_line(self, matrix, integer_matrix, point_group):
        number_text = None
        lines = []
        integer_matrix.save_state()
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix)):
                number = Text("按行遍历下标：i=" + str(i) + " j=" + str(j), font="Menlo", color=BLUE).scale(0.7).next_to(
                    integer_matrix, DOWN, buff=1)
                if number_text is None:
                    number_text = number
                print("i, j:", i, j)
                self.wait()
                self.play(
                    Indicate(integer_matrix.mob_matrix[i][j], color=BLUE, scale_factor=1.8, run_time=1),
                    Transform(number_text, number)
                )
                integer_matrix.mob_matrix[i][j].set_color(YELLOW)
                self.wait(0.2)
                if matrix[i][j] == 1:
                    line = connect_circle(point_group[i][0], point_group[j][0])
                    lines.append(line)
                    self.play(ShowCreation(line))

        self.wait(3)
        self.remove(*lines)
        integer_matrix.restore()
        self.remove(number_text)

        number_text = None
        lines = []
        integer_matrix.save_state()
        for j in range(0, len(matrix)):
            for i in range(j + 1, len(matrix)):
                number = Text("按列遍历下标：i=" + str(i) + " j=" + str(j), font="Menlo", color=BLUE).scale(0.7).next_to(
                    integer_matrix, DOWN, buff=1)
                if number_text is None:
                    number_text = number
                print("i, j:", i, j)
                self.wait()
                self.play(
                    Indicate(integer_matrix.mob_matrix[i][j], color=BLUE, scale_factor=1.8, run_time=1),
                    Transform(number_text, number)
                )
                integer_matrix.mob_matrix[i][j].set_color(YELLOW)
                self.wait(0.2)
                if matrix[i][j] == 1:
                    line = connect_circle(point_group[i][0], point_group[j][0])
                    lines.append(line)
                    self.play(ShowCreation(line))

    def draw_line2(self, matrix, adj_group, point_group, link_data):
        size = len(matrix)
        line_text = Text("", font="Menlo", color=BLUE).scale(0.7)
        lines = []
        for i in range(size):
            self.wait()
            arr_item = adj_group[0][i]
            link_item = adj_group[1][i]
            self.play(
                Indicate(arr_item[1], scale_factor=1.1, run_time=1.5),
            )
            arr_item[1].set_color(BLACK)
            for index in range(len(link_item)):
                link_text: Tex = link_item[index][1][1]
                j = link_data[i][index]
                if i < j:
                    line = connect_circle(point_group[i][0], point_group[j][0])
                    lines.append(line)
                    self.play(
                        Indicate(link_text, scale_factor=1.1, run_time=1),
                        Transform(line_text, Text(
                            "边：V" + str(i + 1) + "V" + str(j + 1), font="Menlo", color=BLUE).scale(0.7)),
                        ShowCreation(line)
                    )
                else:
                    self.play(
                        Indicate(link_text, scale_factor=1.1, run_time=1),
                        Transform(line_text,
                                  Text("边：V" + str(i + 1) + "V" + str(j + 1), font="Menlo", color=BLUE).scale(0.7))
                    )
                link_text.set_color(BLACK)
                self.wait()

            self.wait(2)

    def draw_adj_table(self):
        title = Title("无向图-邻接矩阵").scale(0.9)
        self.add(title)
        matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
        arr_item1 = VGroup(Rectangle(width=2.3, height=3, fill_color=BLUE, fill_opacity=1).scale(0.35),
                           Tex("V1").set_color(WHITE).scale(0.6))
        arr_item2 = VGroup(Rectangle(width=2.3, height=3, fill_color=BLUE, fill_opacity=1).scale(0.35),
                           Tex("V2").set_color(WHITE).scale(0.6)).next_to(arr_item1, DOWN, buff=0)
        arr_item3 = VGroup(Rectangle(width=2.3, height=3, fill_color=BLUE, fill_opacity=1).scale(0.35),
                           Tex("V3").set_color(WHITE).scale(0.6)).next_to(arr_item2, DOWN, buff=0)
        arr_item4 = VGroup(Rectangle(width=2.3, height=3, fill_color=BLUE, fill_opacity=1).scale(0.35),
                           Tex("V4").set_color(WHITE).scale(0.6)).next_to(arr_item3, DOWN, buff=0)
        arr_group = VGroup(arr_item1, arr_item2, arr_item3, arr_item4).shift(UP * 2)
        self.add(arr_group)

        link_group_list = [[], [], [], []]
        link_data = [[], [], [], []]
        for i in range(len(matrix)):
            last = arr_group[i]
            group_item = link_group_list[i]
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    arrow = Line(LEFT * 0.6, RIGHT * 0.6, stroke_width=4)
                    arrow.add_tip(width=0.2, length=0.2)
                    item = VGroup(Square(color=WHITE, fill_color=GREEN, fill_opacity=1).scale(0.4),
                                  Tex("V" + str(j + 1)).set_color(WHITE).scale(0.6))
                    g = VGroup(arrow, item).arrange(RIGHT, buff=0).scale(0.8).next_to(last, buff=0)
                    last = g
                    link_data[i].append(j)
                    group_item.append(g)
        link_group = VGroup(*[
            VGroup(*link_group_list[i])
            for i in range(len(matrix))
        ])

        adj_group = VGroup(arr_group, link_group).scale(0.9).move_to(LEFT_SIDE, aligned_edge=LEFT).shift(
            RIGHT * 1 + UP * 0.7)
        self.add(adj_group)

        point_group = self.draw_point()

        self.draw_line2(matrix, adj_group, point_group, link_data)

    def draw_adj_table2(self):
        title = Title("无向图-邻接表").scale(0.9)
        self.add(title)
        matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]

        # 画点和线
        point1, point2, point3, point4 = self.create_point()
        point_group = VGroup(point1, point2, point3, point4).move_to(ORIGIN)
        lines = []
        line_map = [[None, None, None, None],
                    [None, None, None, None],
                    [None, None, None, None],
                    [None, None, None, None]]
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix)):
                if matrix[i][j] == 1:
                    line = connect_circle(point_group[i][0], point_group[j][0])
                    line_map[i][j] = line
                    line_map[j][i] = line
                    lines.append(line)
        graph = VGroup(point_group, *lines)
        self.add(graph)
        self.wait(2)
        self.play(graph.shift, LEFT * 3 + UP * 1)
        self.wait()

        last_head = None
        code1 = create_code("1.  typedef struct ArcNode {")
        code2 = create_code("2.      int index; // 顶点序号，从0开始，相同序号就是相同点")
        code3 = create_code("3.      char value; // 顶点值")
        code4 = create_code("4.      struct ArcNode *next; //邻接链表")
        code5 = create_code("5.  } ArcNode;")

        code6 = create_code("1.  //邻接表：用一个数组存放链表第一个结点")
        code7 = create_code("2.  typedef struct {")
        code8 = create_code("3.      ArcNode **adjList; // 邻接表数组")
        code9 = create_code("4.      int n;//顶点总数")
        code10 = create_code("5.  } AdjGraph;")

        code_group1 = VGroup(
            code1, code2, code3, code4, code5,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(graph, DOWN, buff=0.8).shift(LEFT * 0.8)
        code_rect1 = get_rect2(code_group1, buff=0.1, stroke_width=0, fill_opacity=1, fill_color=WHITE)

        code_group2 = VGroup(
            code6, code7, code8, code9, code10,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(code_group1, RIGHT)
        code_rect2 = get_rect2(code_group2, buff=0.1, stroke_width=0, fill_opacity=1, fill_color=WHITE)
        VGroup(code_group2, code_rect2).shift(RIGHT * 3)

        head_list = []
        for i in range(len(matrix)):
            self.wait(2)
            link = []
            item = VGroup(Square(fill_color=GREEN, fill_opacity=1).scale(0.4),
                          Tex("V" + str(i + 1)).set_color(WHITE).scale(0.6)).scale(0.7)
            if last_head is not None:
                item.next_to(last_head, DOWN, buff=0.3)
            else:
                item.shift(UP * 2)
            last_head = item
            head_list.append(item)
            self.play(ShowCreation(item))
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    arrow = Line(LEFT * 0.6, RIGHT * 0.6, stroke_width=4).scale(0.7)
                    arrow.add_tip(width=0.2, length=0.2)
                    link_item = VGroup(Square(color=WHITE, fill_color=GREEN, fill_opacity=1).scale(0.4),
                                       Tex("V" + str(j + 1)).scale(0.6)).scale(0.7)
                    g = VGroup(arrow, link_item).arrange(RIGHT, buff=0).next_to(item, buff=0)
                    item = g
                    self.play(ShowCreation(arrow))
                    self.play(ShowCreation(link_item))
                    # link.append(g)
            if i == 0:
                self.add(code_rect1)
                self.play(Write(code1))
                self.play(Write(code3))
                self.play(Write(code4))
                self.play(Write(code5))
            if i == 1:
                self.play(Write(code2))

        self.wait()
        head_rect = get_rect2(VGroup(*head_list), buff=0.1, color=YELLOW)
        self.play(ShowCreation(head_rect))
        self.wait()
        array_index = VGroup(*[
            Tex(str(i)).next_to(head_list[i], LEFT, buff=0.2)
            for i in range(len(head_list))
        ])
        self.play(ShowCreation(array_index))
        self.wait()
        self.add(code_rect2)
        self.play(Write(code5))
        self.play(Write(code6))
        self.play(Write(code7))
        self.play(Write(code8))
        self.play(Write(code9))
        self.play(Write(code10))

    # integer_matrix, x_text_group, y_text_group, matrix_group = self.draw_matrix(matrix)


class Graph2(Scene):
    def construct(self) -> None:
        title = Title("无向图-邻接表").scale(0.9)
        self.add(title)
        matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]


class Test(Scene):
    def construct(self) -> None:
        # matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
        # integer_matrix, x_text_group, y_text_group, matrix_group = create_matrix(matrix)

        # self.add(integer_matrix)

        # arrow = Line(LEFT * 0.6, RIGHT * 0.6, stroke_width=4)
        # arrow.add_tip(width=0.2, length=0.2)
        # item = VGroup(Square(color=WHITE).scale(0.4), Tex("V1").set_color(WHITE).scale(0.6))
        # g = VGroup(arrow, item).arrange(RIGHT, buff=0)
        # self.add(g)

        code1 = create_code("1.  typedef struct ArcNode {")
        code2 = create_code("2.      int index; // 顶点序号，从0开始，相同序号就是相同点")
        code3 = create_code("3.      char value; // 顶点值")
        code4 = create_code("4.      struct ArcNode *next; //邻接链表")
        code5 = create_code("5.  } ArcNode;")

        code_group1 = VGroup(
            code1, code2, code3, code4, code5,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(RIGHT).move_to(LEFT_SIDE, aligned_edge=LEFT)
        # self.add(code_group)
        self.add(get_rect2(code_group1, buff=0.1, stroke_width=0, fill_opacity=1, fill_color=WHITE))
        self.play(Write(code1))
        self.play(Write(code3))
        self.play(Write(code4))
        self.play(Write(code5))
        self.play(Write(code2))

        code6 = create_code("1.  //邻接表：用一个数组存放链表第一个结点")
        code7 = create_code("2.  typedef struct {")
        code8 = create_code("3.      ArcNode **adjList; // 邻接表数组")
        code9 = create_code("4.      int n;//顶点总数")
        code10 = create_code("5.  } AdjGraph;")
        code_group2 = VGroup(
            code6, code7, code8, code9, code10,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(code_group1, RIGHT).move_to(RIGHT_SIDE, aligned_edge=RIGHT)
        self.add(code_group2)

# text = Text("任意的i、j满足：").scale(0.85)
# tex = Tex("A[i][j]=A[j][i]").set_color(BLUE).scale(0.75).next_to(text, RIGHT)
# self.add(text, tex)
