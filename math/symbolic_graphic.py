from manimlib import *
from manimlib.mobject.boolean_ops import Union


class Graphic1(Scene):
    def construct(self) -> None:
        title = Title("数形结合-引入").scale(0.9)
        self.add(title)
        subject1 = VGroup(
            Text("已知正数"),
            Tex("a", color=YELLOW), Tex(" "),
            Tex("b", color=YELLOW), Tex(" "),
            Tex("c", color=YELLOW), Text("和"),
            Tex("m", color=GREEN), Tex(" "),
            Tex("l", color=GREEN), Tex(" "),
            Tex("n", color=GREEN), Text("满足"),
            Tex("a+m=b+n=c+l=k"),
        ).scale(0.6).arrange(RIGHT, buff=0.1).next_to(title, DOWN, buff=0.5)
        subject2 = VGroup(
            Text("证明"),
            Tex("al", "+", "bm", "+", "cn"),
            Tex("\\le", color=PURPLE),
            Tex("k^2"),
        ).scale(0.6).arrange(RIGHT, buff=0.1).next_to(subject1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(subject1))
        self.wait()
        self.play(Write(subject2))
        self.wait()
        k = 8
        a = 6
        b = 5
        c = 2
        m = k - a
        n = k - b
        # l = k - c
        scale = 0.4
        square = Square(side_length=k).move_to(ORIGIN).scale(scale).shift(DOWN)
        self.play(ShowCreation(square))
        pos1 = square.get_vertices()[0]
        pos2 = square.get_vertices()[1]
        pos3 = square.get_vertices()[2]
        pos4 = square.get_vertices()[3]

        brace_k = Brace(Line(pos1, pos4), RIGHT, buff=1)
        text_k = Tex("k").scale(0.6).next_to(brace_k, RIGHT, buff=0.1)
        self.play(ShowCreation(brace_k), Write(text_k))
        line_a = Line(pos2, pos2 + DOWN * a * scale, color=YELLOW)
        brace_a = Brace(line_a, LEFT, buff=0.1)
        self.play(ShowCreation(line_a), GrowFromCenter(brace_a))
        self.play(Write(Tex("a").scale(0.6).next_to(brace_a, LEFT, buff=0.1)))
        line_m = Line(pos2 + DOWN * a * scale, pos3, color=GREEN)
        brace_m = Brace(line_m, LEFT, buff=0.1)
        self.play(ShowCreation(line_m), GrowFromCenter(brace_m))
        self.play(Write(Tex("m").scale(0.6).next_to(brace_m, LEFT, buff=0.1)))
        self.wait()

        line_l = Line(pos2, pos2 + RIGHT * l * scale, color=GREEN)
        brace_l = Brace(line_l, UP, buff=0.1)
        self.play(ShowCreation(line_l), GrowFromCenter(brace_l))
        self.play(Write(Tex("l").scale(0.6).next_to(brace_l, UP, buff=0.1)))
        line_c = Line(pos2 + RIGHT * l * scale, pos1, color=YELLOW)
        brace_c = Brace(line_c, UP, buff=0.1)
        self.play(ShowCreation(line_c), GrowFromCenter(brace_c))
        self.play(Write(Tex("c").scale(0.6).next_to(brace_c, UP, buff=0.1)))
        self.wait()

        line_b = Line(pos3, pos3 + RIGHT * b * scale, color=YELLOW)
        brace_b = Brace(line_b, DOWN, buff=0.1)
        self.play(ShowCreation(line_b), GrowFromCenter(brace_b))
        self.play(Write(Tex("b").scale(0.6).next_to(brace_b, DOWN, buff=0.1)))
        line_n1 = Line(pos3 + RIGHT * b * scale, pos4, color=GREEN)
        brace_n1 = Brace(line_n1, DOWN, buff=0.1)
        text_n1 = Tex("n").scale(0.6).next_to(brace_n1, DOWN, buff=0.1)
        self.play(ShowCreation(line_n1), GrowFromCenter(brace_n1))
        self.play(Write(text_n1))
        self.wait()

        square_al = Polygon(
            pos2,
            pos2 + RIGHT * l * scale,
            pos2 + RIGHT * l * scale + DOWN * a * scale,
            pos2 + DOWN * a * scale,
            fill_color=GREEN, fill_opacity=0.5
        )
        text_al = Tex("al", color=BLACK).scale(0.8).move_to(square_al.get_center())
        self.play(ShowCreation(square_al))
        self.play(TransformFromCopy(subject2[1][0], text_al))
        self.wait()
        square_bm = Polygon(
            pos3 + UP * m * scale,
            pos3 + UP * m * scale + RIGHT * b * scale,
            pos3 + RIGHT * b * scale,
            pos3,
            fill_color=YELLOW, fill_opacity=0.5
        )
        text_bm = Tex("bm", color=BLACK).scale(0.8).move_to(square_bm.get_center())
        self.play(ShowCreation(square_bm))
        self.play(TransformFromCopy(subject2[1][2], text_bm))

        line_n2 = Line(pos1, pos1 + DOWN * n * scale, color=GREEN)
        brace_n2 = Brace(line_n2, RIGHT, buff=0.1)
        text_n2 = Tex("n").scale(0.6).next_to(brace_n2, RIGHT, buff=0.1)
        self.play(
            TransformFromCopy(line_n1, line_n2),
            TransformFromCopy(brace_n1, brace_n2),
            TransformFromCopy(text_n1, text_n2),
        )
        square_cn = Polygon(
            pos1,
            pos1 + LEFT * c * scale,
            pos1 + LEFT * c * scale + DOWN * n * scale,
            pos1 + DOWN * n * scale,
            fill_color=BLUE, fill_opacity=0.5
        )
        text_cn = Tex("cn", color=BLACK).scale(0.8).move_to(square_cn.get_center())
        self.play(ShowCreation(square_cn))
        self.play(TransformFromCopy(subject2[1][4], text_cn))
        self.wait()
        square_k = square.copy().set_fill(color=GREY, opacity=0.5)
        self.play(TransformFromCopy(subject2[3], square_k))
        self.wait(5)


class Graphic2(Scene):
    def construct(self) -> None:
        cir1 = Circle(radius=3).move_to(LEFT * 1.5)
        cir2 = Circle(radius=3).move_to(RIGHT * 1.5)
        d = Intersection(cir1, cir2, color=YELLOW, fill_opacity=0.4)
        self.add(cir1, cir2, d)

        # title = Title("数形结合-veen图").scale(0.9)
        # self.add(title)
        # subject1 = VGroup(
        #     Text("某班有"),
        #     Text("50", color=BLUE),
        #     Text("名学生报名参加A、B两项比赛，"),
        #     Text("参加A项的有"),
        #     Text("30", color=BLUE),
        #     Text("人，参加B项的有"),
        #     Text("33", color=BLUE),
        #     Text("人。"),
        # ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        # subject2 = Text("且A、B都不参加的同学比A、B都参加的同学的三分之一多一人。", t2c={
        #     "不参加": RED, "都参加": GREEN, "三分之一多一人": BLUE,
        # }).scale(0.5).next_to(subject1, DOWN, buff=0.2, aligned_edge=LEFT)
        # subject3 = Text("请问只参加A、没有参加B的同学有几人？", t2c={"只参加A": GREEN, "没有参加B": RED}).scale(
        #     0.5).next_to(subject2, DOWN, buff=0.2, aligned_edge=LEFT)
        # self.add(subject1, subject2, subject3)
        # self.wait(2)
        #
        # square = Square(side_length=3).shift(DOWN * 1.5)
        # self.add(square)
        # text_50 = Tex("50").scale(0.6).move_to(square.get_corner(UR) + LEFT * 0.3 + DOWN * 0.3)
        # self.add(text_50)
        # circle_a = Circle(radius=0.7, color=BLUE_A).move_to(square.get_center() + LEFT * 0.4)
        # text_a = Tex("A").scale(0.6).move_to(circle_a.point_from_proportion(0.65))
        # text_30 = Text("30").scale(0.6).move_to(circle_a.point_from_proportion(0.5) + RIGHT * 0.3)
        # self.play(ShowCreation(circle_a), Write(text_a))
        # circle_b = Circle(radius=0.7 * 33 / 30, color=BLUE_C).move_to(square.get_center() + RIGHT * 0.45)
        # text_b = Tex("B").scale(0.6).move_to(circle_b.point_from_proportion(0.85))
        # text_33 = Text("33").scale(0.6).move_to(circle_b.point_from_proportion(0) + LEFT * 0.3)
        # self.play(ShowCreation(circle_b), Write(text_b))
        # self.wait()
        # self.play(TransformFromCopy(subject1[4], text_30))
        # self.play(TransformFromCopy(subject1[6], text_33))
        # # manim中a、b交集
        # union_ab = Union(circle_a, circle_b, fill_color=YELLOW, opacity=0.5)
        # self.add(union_ab)

