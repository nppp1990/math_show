import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.math_show.common.utils.math_utils import draw_arc
from yj.math_show.common.math.object_utils import add_right_arrow, get_right_angle

from manimlib import *


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
        l = k - c
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
        title = Title("数形结合-Veen图").scale(0.9)
        self.add(title)
        subject1 = VGroup(
            Text("某班有"),
            Text("50", color=BLUE),
            Text("名学生报名参加A、B两项比赛，"),
            Text("参加A项的有"),
            Text("30", color=BLUE),
            Text("人，参加B项的有"),
            Text("33", color=BLUE),
            Text("人。"),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        subject2 = Text("且A、B都不参加的同学比A、B都参加的同学的三分之一多一人。", t2c={
            "不参加": RED, "都参加": GREEN, "三分之一多一人": BLUE,
        }).scale(0.5).next_to(subject1, DOWN, buff=0.2, aligned_edge=LEFT)
        subject3 = Text("请问只参加A、没有参加B的同学有几人？", t2c={"只参加A": GREEN, "没有参加B": RED}).scale(
            0.5).next_to(subject2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(subject1), run_time=1.5)
        self.play(Write(subject2), run_time=1.5)
        self.play(Write(subject3))
        self.wait(2)

        square = Square(side_length=3).shift(DOWN * 1.5)
        self.play(ShowCreation(square))
        text_50 = Tex("50").scale(0.6).move_to(square.get_corner(UR) + LEFT * 0.3 + DOWN * 0.3)
        self.play(TransformFromCopy(subject1[1], text_50))
        circle_a = Circle(radius=0.7, color=BLUE_A).move_to(square.get_center() + LEFT * 0.4)
        text_a = Tex("A").scale(0.6).move_to(circle_a.point_from_proportion(0.65))
        text_30 = Text("30").scale(0.6).move_to(circle_a.point_from_proportion(0.5) + RIGHT * 0.4)
        self.play(ShowCreation(circle_a), Write(text_a))
        circle_b = Circle(radius=0.7 * 33 / 30, color=BLUE_C).move_to(square.get_center() + RIGHT * 0.45)
        text_b = Tex("B").scale(0.6).move_to(circle_b.point_from_proportion(0.85))
        text_33 = Text("33").scale(0.6).move_to(circle_b.point_from_proportion(0) + LEFT * 0.4)
        self.play(ShowCreation(circle_b), Write(text_b))
        self.wait()
        self.play(TransformFromCopy(subject1[4], text_30))
        self.play(TransformFromCopy(subject1[6], text_33))
        self.wait()
        desc1 = VGroup(
            Text("设A、B都参加的同学人数为"),
            Text("x", color=BLUE),
        ).scale(0.5).arrange(RIGHT, buff=0.1).next_to(title, DOWN, buff=2.5, aligned_edge=LEFT).shift(LEFT)
        self.play(Write(desc1))
        # manim中a、b交集 不知道是我显卡的问题还是什么，填充非常不圆滑
        intersection_ab = Intersection(circle_a.copy(),
                                       circle_b.copy(),
                                       color=YELLOW, fill_opacity=0.3)
        self.play(ShowCreation(intersection_ab))
        text_x = Tex("x").scale(0.6).move_to(intersection_ab.get_center())
        self.play(TransformFromCopy(desc1[1], text_x))
        self.wait()

        diff1 = Difference(circle_a, circle_b, color=BLUE, fill_opacity=0.3)
        self.play(ShowCreation(diff1))
        text_30_x = Tex("30-x").scale(0.4).move_to(diff1.get_center()).shift(LEFT * 0.1)
        self.play(FadeOut(text_30, run_time=0.5), ShowCreation(text_30_x))
        diff2 = Difference(circle_b, circle_a, color=BLUE, fill_opacity=0.3)
        self.play(ShowCreation(diff2))
        text_33_x = Tex("33-x").scale(0.5).move_to(diff2.get_center()).shift(RIGHT * 0.1)
        self.play(FadeOut(text_33, run_time=0.5), ShowCreation(text_33_x))

        diff3 = Difference(square, VGroup(circle_a, circle_b), color=BLUE, fill_opacity=0.3)
        text_diff3 = Text("50-33-(30-x)").scale(0.4).move_to(square.get_center() + UP * 1)
        self.play(ShowCreation(diff3, run_time=1.5), FadeOut(VGroup(diff1, diff2, intersection_ab), run_time=0.3))
        self.play(Write(text_diff3))
        desc2 = VGroup(
            Text("则A、B都不参加的同学人数为"),
            Text("50-33-(30-x)", color=BLUE),
        ).scale(0.5).arrange(RIGHT, buff=0.1).next_to(desc1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc2))
        self.wait()
        rect1 = SurroundingRectangle(subject2, color=RED)
        self.play(ShowCreation(rect1))
        desc3 = Tex("50-33-(30-x)=\\frac{x}{3}+1").scale(0.5).next_to(desc2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc3))
        arrow = VGroup(Tex("\\Downarrow"), Tex("x=21")).arrange(DOWN).scale(0.5).next_to(desc3, DOWN, buff=0.1)
        self.play(Write(arrow))
        text_res = Tex("9", color=GREEN).scale(0.6).move_to(text_30_x)
        rect2 = SurroundingRectangle(subject3, color=RED)
        self.play(Transform(rect1, rect2))
        self.wait()
        self.play(Transform(text_30_x, text_res))
        self.wait(5)


class IntersectionExample(Scene):
    def construct(self):
        sq = Circle(color=WHITE, fill_opacity=1)
        sq.move_to(np.array([-2, 0, 0]))
        cr = Circle(color=WHITE, fill_opacity=1)
        cr.move_to(np.array([-1.3, 0.7, 0]))
        un = Intersection(sq, cr, color=GREEN)
        # un.move_to(np.array([1.5, 0, 0]))
        # self.add(sq, cr)
        self.wait(2)
        self.play(ShowCreation(un))


class Graphic3(Scene):
    def construct(self) -> None:
        title = Title("数形结合-函数举例").scale(0.9)
        self.add(title)
        subject1 = VGroup(
            Text("已知函数"),
            Tex("f(x)="),
            Tex(
                "\\left\\{\\begin{matrix} -x^2+2, \\quad x\\le 1 \\\\  x+\\frac{1}{x}-1,\\quad x>1 \\end{matrix}\\right."),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        subject2 = VGroup(
            Text("若当"),
            Tex("x\\in[a,b]"),
            Text("时，"),
            Tex("1\\le f(x)\\le 3"),
            Text("，则"),
            Tex("b-a"),
            Text("的最大值"),
            Tex("=", "\\underline{\\qquad}")
        ).arrange(RIGHT).scale(0.5).next_to(subject1, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(subject1))
        self.play(Write(subject2))
        self.wait(2)
        # 画坐标系、带箭头的
        scale = 0.7
        axes = Axes(
            # x轴范围: -3到3, 步长为1
            x_range=[-3, 5.5, 1],
            y_range=[-3, 4, 1],
            width=8.5,
            height=7,
            axis_config={"include_tip": True, "include_ticks": True, "include_numbers": True},
            # 数字的方向 旋转角度
            y_axis_config={"line_to_number_direction": UP},
        ).scale(scale).shift(DOWN * 1.5 + RIGHT * 2)
        self.play(ShowCreation(axes), run_time=2)
        # 画函数图像
        func1 = axes.get_graph(lambda x: -x ** 2 + 2, x_range=[-2, 1], color=BLUE)
        func2 = axes.get_graph(lambda x: x + 1 / x - 1, x_range=[1, 5], color=YELLOW)
        self.play(ShowCreation(func1), run_time=2)
        self.play(ShowCreation(func2), run_time=2)
        self.wait()
        b = 2 + math.sqrt(3)
        rect1 = SurroundingRectangle(subject2[3], color=RED)
        line_1 = DashedLine(axes.coords_to_point(-3, 1), axes.coords_to_point(5, 1)).set_stroke(width=0.25, opacity=0.9)
        line_3 = DashedLine(axes.coords_to_point(-3, 3), axes.coords_to_point(5, 3)).set_stroke(width=0.25, opacity=0.9)
        self.play(ShowCreation(rect1))
        self.play(ShowCreation(line_1), ShowCreation(line_3),
                  Write(Tex("1").scale(0.5).next_to(line_1, LEFT, buff=0.1)),
                  Write(Tex("3").scale(0.5).next_to(line_3, LEFT, buff=0.1)))
        min_v_line = axes.get_v_line(axes.coords_to_point(-1, 1))
        text_min_point = Tex("(-1,1)").scale(0.5).next_to(axes.coords_to_point(-1, 1), UL, buff=0.1)
        min_dot = Dot(axes.coords_to_point(-1, 1), radius=0.05, color=BLACK)
        max_v_line = axes.get_v_line(axes.coords_to_point(b, 3))
        text_max_point = Tex("(x_0,3)").scale(0.5).next_to(axes.coords_to_point(b, 3), DR, buff=0.1)
        max_dot = Dot(axes.coords_to_point(b, 3), radius=0.05, color=BLACK)
        self.play(ShowCreation(min_v_line), Write(text_min_point), ShowCreation(min_dot))
        self.play(ShowCreation(max_v_line), Write(text_max_point), ShowCreation(max_dot))
        self.wait()
        desc1 = VGroup(
            Text("由于"),
            Tex("1\\le f(x)\\le 3"),
            Text("所以"),
            Tex("x\\in[-1,x_0]"),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=2.5, aligned_edge=LEFT).shift(LEFT)
        self.play(Write(desc1[0]), run_time=0.3)
        self.play(TransformFromCopy(subject2[3], desc1[1]))
        self.play(Write(desc1[2]), run_time=0.3)
        self.play(TransformFromCopy(subject2[1], desc1[3]))
        self.play(FadeOut(rect1), run_time=0.5)
        self.wait()
        desc2 = VGroup(
            Text("要使"), Tex("b-a"), Text("最大，那么", t2c={"最大": YELLOW}),
            Tex("a"), Text("应尽量小，", color=YELLOW), Tex("b"), Text("应尽量大", color=YELLOW),
        ).arrange(RIGHT).scale(0.5).next_to(desc1, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc2))
        self.wait()
        desc3 = VGroup(
            Text("显然"),
            Tex("a=-1 \\quad b=x_0"),
            Text("时，"), Tex("b-a"), Text("最大")
        ).arrange(RIGHT).scale(0.5).next_to(desc2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc3))
        desc4 = Tex("x_0+\\frac{1}{x_0}-1=3\\rightarrow x_0=2+\\sqrt{3}").scale(0.5).next_to(
            desc3, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc4))
        desc5 = Tex("\\max(b-a)=2+\\sqrt{3}-(-1)=", "3+\\sqrt{3}").scale(0.5).next_to(
            desc4, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc5))
        res = Tex("3+\\sqrt{3}", color=GREEN).scale(0.5).move_to(subject2[-1][1].get_center() + UP * 0.2 + RIGHT * 0.2)
        self.play(TransformFromCopy(desc5[-1], res))
        self.wait(5)


class Graphic4(Scene):
    def construct(self) -> None:
        title = Title("数形结合-三角篇一").scale(0.9)
        self.add(title)
        subject = VGroup(
            Text("当"),
            Tex("0 < \\theta <\\frac{\\pi}{2}"),
            Text("时，"),
            Tex("\\sin\\theta", "<", "\\theta", "<", "\\tan\\theta", color=YELLOW),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(subject[0:3]))
        self.wait()
        self.play(Write(subject[3]))
        scale = 1
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            width=5.5,
            height=5.5,
            axis_config={"include_tip": True, "include_ticks": True},
            x_axis_config={"include_numbers": True},
        ).scale(scale).shift(DOWN)
        self.play(ShowCreation(axes), run_time=2)
        self.play(Write(axes.get_x_axis_label("x")), Write(axes.get_y_axis_label("y")), run_time=0.5)
        radius = axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]
        circle = Circle(radius=radius, color=BLUE).shift(axes.c2p(0, 0))
        self.play(ShowCreation(circle), Write(Tex("O").scale(0.6).next_to(axes.c2p(0, 0), DL, buff=0.1)))
        radius_text = Tex("R=1").next_to(axes.c2p(-1.4, 1.1)).scale(0.6)
        self.play(Write(radius_text))
        angle = PI / 3
        pos_a = circle.point_from_proportion(angle / TAU)
        line_oa = Line(axes.c2p(0, 0), pos_a)
        dot_a = Dot(pos_a, radius=0.07)
        self.play(ShowCreation(line_oa), Write(Tex("A").scale(0.55).next_to(pos_a, LEFT, buff=0.1)))
        arc_aox = draw_arc(pos_a, axes.c2p(0, 0), axes.c2p(1, 0), color=YELLOW, radius=0.2)
        text_angle = Tex("\\theta", color=YELLOW).scale(0.5).next_to(arc_aox, RIGHT, buff=0.1).shift(UP * 0.1)
        self.play(ShowCreation(dot_a), ShowCreation(arc_aox), ShowCreation(text_angle))
        pos_b = axes.c2p(math.cos(angle), 0)
        line_ab = Line(pos_a, pos_b, color=YELLOW)
        text1 = Tex("\\sin\\theta").scale(0.4).next_to(line_ab, OUT)
        self.play(ShowCreation(line_ab), Write(Tex("B").scale(0.55).next_to(pos_b, DOWN, buff=0.1)))
        self.play(TransformFromCopy(subject[3][0], text1))
        # circle 圆弧
        arc = Arc(radius=radius, start_angle=0, angle=angle, arc_center=axes.c2p(0, 0), color=YELLOW)
        text2 = Tex("\\theta").scale(0.4).next_to(arc, OUT).shift(RIGHT * 0.2 + UP * 0.2)
        self.play(ShowCreation(arc))
        self.play(TransformFromCopy(subject[3][2], text2))
        dash_line_ac = DashedLine(pos_a, axes.c2p(1, 0))
        self.play(ShowCreation(dash_line_ac), Write(Tex("C").scale(0.55).next_to(axes.c2p(1, 0), DOWN, buff=0.1)))
        desc1 = VGroup(Tex("AB<AC<"), Text("弧"), Tex("AC\\rightarrow"),
                       Tex("\\sin\\theta< \\theta", color=YELLOW)).arrange(
            RIGHT).scale(0.55).next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT)
        self.play(Write(desc1))
        self.wait()
        pos_d = axes.c2p(1, math.tan(angle))
        dash_line_cd = Line(axes.c2p(1, 0), pos_d, color=YELLOW)
        dash_line_ad = DashedLine(pos_a, pos_d)
        self.play(ShowCreation(dash_line_cd), ShowCreation(dash_line_ad), FadeOut(dash_line_ac, run_time=0.3))
        self.play(Write(Tex("D").scale(0.55).next_to(pos_d, RIGHT, buff=0.1)))
        text3 = Tex("\\tan\\theta").scale(0.4).next_to(dash_line_cd, OUT)
        self.play(TransformFromCopy(subject[3][4], text3))
        # 扇形AOC
        desc2 = VGroup(Text("扇形"), Tex("S_{AOC}=\\frac{1}{2}R^2\\theta=\\frac{\\theta}{2}")).arrange(
            RIGHT).scale(0.55).next_to(desc1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(desc2))
        desc3 = VGroup(Text("三角形"), Tex("S_{ODC}=\\frac{1}{2}R\\tan\\theta=\\frac{\\tan\\theta}{2}")).arrange(
            RIGHT).scale(0.55).next_to(desc2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc3))
        self.play(ShowCreation(Brace(VGroup(desc2, desc3), LEFT)))
        self.wait()
        desc4 = VGroup(
            Tex("S_{AOC}<S_{ODC}\\rightarrow", ),
            Tex("\\theta<\\tan\\theta", color=YELLOW)
        ).arrange(RIGHT).scale(0.55).next_to(desc3, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(desc4))
        self.wait(5)


class Graphic5(Scene):
    def construct(self) -> None:
        title = Title("数形结合-三角篇二").scale(0.9)
        self.add(title)
        subject1 = VGroup(
            Text("(2021·新高考Ⅰ)", color=BLUE),
            Text("已知O为坐标原点,"),
            Text("点"), Tex("P_1(\\cos\\alpha,\\sin\\alpha),", color=BLUE),
            Text("点"), Tex("P_2(\\cos\\beta,-\\sin\\beta)", color=RED),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        subject2 = VGroup(
            Text("点"), Tex("P_3(\\cos(\\alpha+\\beta),\\sin(\\alpha+\\beta)),", color=GREEN),
            Text("点"), Tex("A(1,0)", color=YELLOW),
            Text("则"), Tex("(\\quad\\quad)"),
        ).arrange(RIGHT).scale(0.5).next_to(subject1, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(subject1))
        self.play(Write(subject2))
        self.wait()

        subject3_1 = Tex("A.\\quad", "|\\overrightarrow{OP_1}|=|\\overrightarrow{OP_2}|").scale(0.5).next_to(
            subject2, DOWN, buff=0.5, aligned_edge=LEFT)
        subject3_2 = Tex("B.\\quad", "|\\overrightarrow{AP_1}|", "=", "|\\overrightarrow{AP_2}|").scale(0.5).next_to(
            subject3_1, RIGHT, buff=2)
        subject4_1 = Tex("C.\\quad ",
                         "\\overrightarrow{OA} \\cdot \\overrightarrow{OP_3}", "=",
                         "\\overrightarrow{OP_1} \\cdot \\overrightarrow{OP_2}").scale(0.5).next_to(
            subject3_1, DOWN, buff=0.4, aligned_edge=LEFT)
        subject4_2 = Tex("D.\\quad ",
                         "\\overrightarrow{OA} \\cdot \\overrightarrow{OP_1}", "=",
                         "\\overrightarrow{OP_2} \\cdot \\overrightarrow{OP_3}").scale(0.5).next_to(
            subject3_2, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(subject3_1))
        self.play(Write(subject3_2))
        self.play(Write(subject4_1))
        self.play(Write(subject4_2))
        self.wait()

        subject_offset3 = LEFT * 4 + subject3_2.get_right() + RIGHT * 0.5 - subject4_1.get_left()
        subject_offset4 = LEFT * 4 + subject3_2.get_right() + RIGHT * 1 + subject4_1.get_width() * RIGHT - subject4_2.get_left()
        self.play(
            subject3_1.shift, LEFT * 2.5,
            subject3_2.shift, LEFT * 4,
            subject4_1.shift, subject_offset3,
            subject4_2.shift, subject_offset4,
        )
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            width=4,
            height=4,
            axis_config={"include_tip": True, "include_ticks": True},
            x_axis_config={"include_numbers": True},
        ).shift(DOWN * 1.5)
        self.play(ShowCreation(axes), run_time=2)
        text_x = axes.get_x_axis_label("x").scale(0.6)
        text_y = axes.get_y_axis_label("y").scale(0.6)
        self.play(Write(text_x), Write(text_y), run_time=0.5)
        self.play(VGroup(axes, text_x, text_y).shift, LEFT * 2.5)
        radius = axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]
        circle = Circle(radius=radius, color=WHITE).shift(axes.c2p(0, 0))
        self.play(
            ShowCreation(circle),
            Write(Tex("O").scale(0.6).next_to(axes.c2p(0, 0), DL, buff=0.1)),
            Write(Tex("A", color=YELLOW).scale(0.5).next_to(axes.c2p(1, 0), DOWN, buff=0.1))
        )
        radius_text = Tex("R=1").next_to(axes.c2p(-1.4, 1.1)).scale(0.6)
        self.play(Write(radius_text))
        angle1 = PI * 5 / 12
        pos_a = axes.c2p(1, 0)
        pos_p1 = circle.point_from_proportion(angle1 / TAU)
        arc1 = draw_arc(pos_a, axes.c2p(0, 0), pos_p1, color=BLUE, radius=0.2)
        line_op1 = Line(axes.c2p(0, 0), pos_p1, color=BLUE)
        text_p1 = Tex("P_1", color=BLUE).scale(0.4).next_to(pos_p1, UR, buff=0.05)
        text_angle1 = Tex("\\alpha", color=BLUE).scale(0.4).next_to(arc1, RIGHT, buff=0.05)
        self.play(ShowCreation(line_op1))
        self.play(Write(text_p1), run_time=0.5)
        self.play(ShowCreation(arc1), Write(text_angle1))
        desc1 = VGroup(Tex("\\gamma = -\\beta")).scale(0.5).arrange(RIGHT).next_to(
            subject4_1, DOWN, buff=0.5, aligned_edge=LEFT).shift(RIGHT)
        desc2 = Tex("\\cos\\beta = \\cos-\\beta=\\cos\\gamma").scale(0.5).next_to(
            desc1, DOWN, buff=0.2, aligned_edge=LEFT)
        desc3 = Tex("\\sin\\beta = \\sin-\\beta=-\\sin\\gamma").scale(0.5).next_to(
            desc2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc1))
        self.play(Write(desc2))
        self.play(Write(desc3))
        arrow1 = add_right_arrow(VGroup(desc2, desc3), length=0.5)
        self.play(ShowCreation(arrow1))
        desc4 = Tex("P_2(\\cos\\beta,-\\sin\\beta)=", "P_2(\\cos\\gamma,\\sin\\gamma)").scale(0.5).next_to(
            arrow1, RIGHT, buff=0.2)
        self.play(Write(desc4))
        self.wait(2)
        self.play(FadeOut(VGroup(desc2, desc3, arrow1, desc4[0])),
                  desc4[1].next_to, desc1, RIGHT, {"buff": 0.4},
                  desc4[1].set_color, RED)
        self.wait()
        angle2 = PI / 11
        pos_p2 = circle.point_from_proportion(angle2 / TAU)
        arc2 = draw_arc(pos_a, axes.c2p(0, 0), pos_p2, color=RED, radius=0.7)
        text_p2 = Tex("P_2", color=RED).scale(0.4).next_to(pos_p2, RIGHT, buff=0.05)
        line_op2 = Line(axes.c2p(0, 0), pos_p2, color=RED)
        text_angle2 = Tex("\\gamma", color=RED).scale(0.4).next_to(arc2, RIGHT, buff=0.05)
        self.play(ShowCreation(line_op2))
        self.play(Write(text_p2), run_time=0.5)
        self.play(ShowCreation(arc2), Write(text_angle2))
        self.wait(2)
        desc5 = Tex("\\cos(\\alpha+\\beta)=\\cos(\\alpha-\\gamma)").scale(0.5).next_to(
            desc1, DOWN, buff=0.5, aligned_edge=LEFT)
        desc6 = Tex("\\sin(\\alpha+\\beta)=\\sin(\\alpha-\\gamma)").scale(0.5).next_to(
            desc5, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc5))
        self.play(Write(desc6))
        arrow2 = add_right_arrow(VGroup(desc5, desc6), length=0.5)
        desc7 = Tex("P_3(\\cos(\\alpha-\\gamma),\\sin(\\alpha-\\gamma))", color=GREEN).scale(0.5).next_to(
            arrow2, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow2))
        self.play(Write(desc7))
        self.wait(2)
        self.play(FadeOut(VGroup(desc5, desc6, arrow2)), desc7.next_to, desc4[1], RIGHT, {"buff": 0.4})
        pos_p3 = circle.point_from_proportion((angle1 - angle2) / TAU)
        text_p3 = Tex("P_3", color=GREEN).scale(0.4).next_to(pos_p3, RIGHT, buff=0.05)
        arc3 = draw_arc(pos_p1, axes.c2p(0, 0), pos_p3, color=GREEN, radius=0.6)
        text_angle3 = Tex("\\gamma").scale(0.4).next_to(arc3, UR, buff=0.05)
        line_op3 = Line(axes.c2p(0, 0), pos_p3, color=GREEN)
        self.play(ShowCreation(line_op3))
        self.play(Write(text_p3), run_time=0.5)
        self.play(ShowCreation(arc3), Write(text_angle3))
        self.wait(2)
        indicate_op1 = Line(axes.get_origin(), pos_p1, color=BLACK)
        indicate_op2 = Line(axes.get_origin(), pos_p2, color=BLACK)
        self.play(ShowCreation(indicate_op1), ShowCreation(indicate_op2), run_time=2)
        res1 = Tex("|\\overrightarrow{OP_1}|=|\\overrightarrow{OP_2}|", "=1").scale(0.5).next_to(
            desc1, DOWN, buff=0.5, aligned_edge=LEFT).shift(RIGHT * 0.5)
        self.play(TransformFromCopy(subject3_1[1], res1[0]))
        self.play(Write(res1[1]))
        yes1 = SVGMobject("../assets/yes.svg").scale(0.2).move_to(subject3_1.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(yes1))
        self.wait()
        self.play(FadeOut(VGroup(indicate_op1, indicate_op2)))
        indicate_ap1 = Line(pos_a, pos_p1, color=BLACK)
        indicate_ap2 = Line(pos_a, pos_p2, color=BLACK)
        self.play(ShowCreation(indicate_ap1), ShowCreation(indicate_ap2), run_time=2)
        no2 = SVGMobject("../assets/no.svg").scale(0.2).move_to(subject3_2.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(no2))
        self.wait()
        self.play(FadeOut(VGroup(indicate_ap1, indicate_ap2)))
        res2 = Tex(
            "\\overrightarrow{OA} \\cdot \\overrightarrow{OP_3}",
            "=OA \\cdot OP_3 \\cdot \\cos\\angle P_3OA=\\cos(\\alpha-\\gamma)",
        ).scale(0.5).next_to(res1, DOWN, buff=0.4, aligned_edge=LEFT)
        indicate_oa = Line(axes.get_origin(), pos_a, color=BLACK)
        indicate_op3 = Line(axes.get_origin(), pos_p3, color=BLACK)
        self.play(TransformFromCopy(subject4_1[1], res2[0]))
        self.play(ShowCreation(indicate_oa), ShowCreation(indicate_op3), run_time=2)
        self.play(Write(res2[1]))
        self.wait()
        self.play(FadeOut(VGroup(indicate_oa, indicate_op3)))
        res3 = Tex(
            "\\overrightarrow{OP_1} \\cdot \\overrightarrow{OP_2}",
            "=OA \\cdot OP_3 \\cdot \\cos\\angle P_3OA=\\cos(\\alpha-\\gamma)",
        ).scale(0.5).next_to(res2, DOWN, buff=0.2, aligned_edge=LEFT)
        indicate_op1 = Line(axes.get_origin(), pos_p1, color=BLACK)
        indicate_op2 = Line(axes.get_origin(), pos_p2, color=BLACK)
        self.play(TransformFromCopy(subject4_1[3], res3[0]))
        self.play(ShowCreation(indicate_op1), ShowCreation(indicate_op2), run_time=2)
        self.play(Write(res3[1]))
        yes3 = SVGMobject("../assets/yes.svg").scale(0.2).move_to(subject4_1.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(yes3))
        self.wait()
        self.play(FadeOut(VGroup(indicate_op1, indicate_op2)))
        desc4 = Tex(
            "\\overrightarrow{OA} \\cdot \\overrightarrow{OP_1}",
            "=OA \\cdot OP_1 \\cdot \\cos\\angle AOP1=\\cos\\alpha",
        ).scale(0.5).next_to(res3, DOWN, buff=0.4, aligned_edge=LEFT)
        indicate_oa = Line(axes.get_origin(), pos_a, color=BLACK)
        indicate_op1 = Line(axes.get_origin(), pos_p1, color=BLACK)
        self.play(TransformFromCopy(subject4_2[1], desc4[0]))
        self.play(ShowCreation(indicate_oa), ShowCreation(indicate_op1), run_time=2)
        self.play(Write(desc4[1]))
        self.wait()
        self.play(FadeOut(VGroup(indicate_oa, indicate_op1)))
        desc5 = Tex(
            "\\overrightarrow{OP_2} \\cdot \\overrightarrow{OP_3}",
            "=OP_2 \\cdot OP_3 \\cdot \\cos\\angle P_2OP_3=\\cos 2(\\alpha-\\gamma)",
        ).scale(0.5).next_to(desc4, DOWN, buff=0.2, aligned_edge=LEFT)
        indicate_op2 = Line(axes.get_origin(), pos_p2, color=BLACK)
        indicate_op3 = Line(axes.get_origin(), pos_p3, color=BLACK)
        self.play(TransformFromCopy(subject4_2[3], desc5[0]))
        self.play(ShowCreation(indicate_op2), ShowCreation(indicate_op3), run_time=2)
        self.play(Write(desc5[1]))
        no5 = SVGMobject("../assets/no.svg").scale(0.2).move_to(subject4_2.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(no5))
        self.wait(5)


class Graphic6(Scene):
    def construct(self) -> None:
        title = Title("数形结合-向量投影").scale(0.9)
        self.add(title)
        subject = VGroup(
            Text("(2020·山东)", color=BLUE),
            Text("已知P是边长为2的正六边形"),
            Tex("ABCDEF").scale(0.9),
            Text("内的一点"),
            Text("，则"),
            Tex("\\overrightarrow{AP}").scale(0.9),
            Tex("\\cdot").scale(0.9),
            Tex("\\overrightarrow{AB}").scale(0.9),
            Text("的取值范围是"),
            Tex("(\\quad\\quad)")
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.add(subject)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            width=5,
            height=5,
        ).shift(DOWN + LEFT * 2)
        unit = axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]
        # self.add(axes)
        n = 6
        angle = PI * (n - 2) / n
        pos_a = axes.coords_to_point(-1, -2 * math.sqrt(angle / 2))
        pos_b = axes.coords_to_point(1, -2 * math.sqrt(angle / 2))
        pos_c = axes.coords_to_point(2, 0)
        pos_d = axes.coords_to_point(1, 2 * math.sqrt(angle / 2))
        pos_e = axes.coords_to_point(-1, 2 * math.sqrt(angle / 2))
        pos_f = axes.coords_to_point(-2, 0)
        text_points = VGroup(
            Tex("A").scale(0.5).next_to(pos_a, DOWN, buff=0.1).scale(0.7),
            Tex("B").scale(0.5).next_to(pos_b, DOWN, buff=0.1).scale(0.7),
            Tex("C").scale(0.5).next_to(pos_c, RIGHT, buff=0.1).scale(0.7),
            Tex("D").scale(0.5).next_to(pos_d, UP, buff=0.1).scale(0.7),
            Tex("E").scale(0.5).next_to(pos_e, UP, buff=0.1).scale(0.7),
            Tex("F").scale(0.5).next_to(pos_f, LEFT, buff=0.1).scale(0.7),
        )
        polygon = Polygon(pos_a, pos_b, pos_c, pos_d, pos_e, pos_f)
        self.play(ShowCreation(polygon))
        self.play(Write(text_points))
        self.wait()
        p1 = Dot(axes.coords_to_point(0, 0), color=RED).scale(0.7)
        text_p = Tex("P").scale(0.5).next_to(p1, RIGHT, buff=0.1).scale(0.7)
        self.play(ShowCreation(p1), Write(text_p))
        pos_p2 = pos_a + (p1.get_center() - pos_a)[0] * RIGHT
        p2 = Dot(pos_p2, color=RED).scale(0.7)
        text_p2 = Tex("P`").scale(0.5).next_to(p2, DOWN, buff=0.1).scale(0.7)
        line_ap = DashedLine(pos_a, p1)
        arc_p = draw_arc(p1.get_center(), pos_a, pos_p2, color=YELLOW, radius=0.2)
        text_arc = Tex("\\alpha").scale(0.5).next_to(arc_p, RIGHT, buff=0.1)
        self.play(ShowCreation(line_ap))
        self.play(Write(text_arc), ShowCreation(arc_p))
        self.wait()
        line_p = DashedLine(p1, p2)
        right_angle = get_right_angle(pos_p2, RIGHT * 0.15, UP * 0.15)
        self.play(ShowCreation(line_p))
        self.play(ShowCreation(right_angle), ShowCreation(p2), Write(text_p2))

        desc1 = Tex("\\overrightarrow{AP} \\cdot \\overrightarrow{AB}",
                    "=AP \\cdot AB \\cdot \\cos\\angle \\alpha",
                    "=2 \\cdot |\\overrightarrow{AP}| \\cdot \\cos\\angle \\alpha",
                    ).scale(0.6).next_to(subject, DOWN, buff=1, aligned_edge=RIGHT).shift(RIGHT * 0.5)
        self.play(Write(desc1))
        self.wait()
        line_ap2 = Line(pos_a, pos_p2, color=BLUE)
        self.play(FadeOut(text_arc), ShowCreation(line_ap2))

        def update_func1(mob):
            mob[0].become(DashedLine(pos_a, p1))
            mob[1].become(DashedLine(p1.get_center(), p2.get_center()))
            mob[2].become(draw_arc(p1.get_center(), pos_a, pos_p2, color=YELLOW, radius=0.2))
            mob[3].next_to(p1, RIGHT, buff=0.1)

        self.play(
            p1.animate.shift(2 * math.cos(angle / 2) * UP),
            UpdateFromFunc(VGroup(line_ap, line_p, arc_p, text_p), update_func1),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(right_angle), FadeOut(text_points[2:]))

        def update_func2(mob):
            pos2 = pos_a + (p1.get_center() - pos_a)[0] * RIGHT
            mob[0].become(DashedLine(pos_a, p1))
            mob[1].become(DashedLine(p1.get_center(), p2.get_center()))
            mob[2].become(draw_arc(p1.get_center(), pos_a, pos_p2, color=YELLOW, radius=0.2))
            mob[3].next_to(p1, RIGHT, buff=0.1)
            mob[4].move_to(pos2)
            mob[5].next_to(pos2, DOWN, buff=0.1)
            mob[6].become(Line(pos_a, pos2, color=BLUE))

        self.play(
            p1.animate.move_to(pos_c),
            UpdateFromFunc(VGroup(line_ap, line_p, arc_p, text_p, p2, text_p2, line_ap2), update_func2),
            run_time=2,
        )
        self.play(
            Write(Tex("1").scale(0.5).next_to((pos_b + p2.get_center()) / 2, DOWN, buff=0.1).scale(0.7)),
            Write(Tex("2").scale(0.5).next_to((pos_a + pos_b) / 2, DOWN, buff=0.1).scale(0.7))
        )
        desc2 = Tex("-1<", "|\\overrightarrow{AP}| \\cdot \\cos\\angle \\alpha", "<3").scale(0.6).next_to(
            desc1, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(ShowCreation(SurroundingRectangle(subject[3], color=RED, buff=0.1)))
        self.play(Write(desc2[1:]))

        self.wait()
        self.play(
            p1.animate.move_to(pos_d),
            UpdateFromFunc(VGroup(line_ap, line_p, arc_p, text_p, p2, text_p2, line_ap2), update_func2),
        )
        self.play(
            p1.animate.move_to(pos_e),
            UpdateFromFunc(VGroup(line_ap, line_p, arc_p, text_p, p2, text_p2, line_ap2), update_func2),
        )
        self.play(
            p1.animate.move_to(pos_f),
            UpdateFromFunc(VGroup(line_ap, line_p, arc_p, text_p, p2, text_p2, line_ap2), update_func2),
        )
        self.play(Write(Tex("1").scale(0.5).next_to((pos_a + p2.get_center()) / 2, DOWN, buff=0.1).scale(0.7)))
        self.play(Write(desc2[0]))
        desc3 = Tex("-2<", "\\overrightarrow{AP} \\cdot \\overrightarrow{AB}", "<6").scale(0.6).next_to(
            desc2, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(desc3))
        self.wait(5)


class Graphic7(Scene):
    def construct(self) -> None:
        title = Title("数形结合-解析几何-斜率").scale(0.9)
        self.add(title)
        subject = VGroup(
            Text("求"),
            Tex("\\frac{1-\\sin x}{2- \\cos x}"),
            Text("的取值范围"),
            Tex("=[0, \\frac{4}{3}]", color=GREEN)
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(subject[0: 3]))
        self.wait()
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            width=5,
            height=5,
            axis_config={"include_tip": True, "include_ticks": False, "include_numbers": False},
        ).shift(DOWN)
        # text_x = axes.get_x_axis_label("x").scale(0.4)
        # text_y = axes.get_y_axis_label("y", buff=0.2).scale(0.4)
        self.play(ShowCreation(axes), run_time=2)

        desc1 = Tex("(x_1, y_1)", "\\quad", "(x_2, y_2)").scale(0.6).next_to(
            title, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT)
        desc2 = Tex("k=\\frac{y_2-y_1}{x_2-x_1}").scale(0.6).next_to(desc1, DOWN, buff=0.5, aligned_edge=LEFT)
        desc3 = Tex("\\tan \\theta = k", color=YELLOW).scale(0.6).next_to(desc2, DOWN, buff=0.5, aligned_edge=LEFT)
        x1 = -2
        y1 = -1
        x2 = 2
        y2 = 2
        dot1 = Dot(axes.c2p(x1, y1), color=BLUE).scale(0.5)
        dot2 = Dot(axes.c2p(x2, y2), color=BLUE).scale(0.5)
        text_dot1 = Tex("(x_1, y_1)").scale(0.6).next_to(dot1, DL, buff=0.1)
        text_dot2 = Tex("(x_2, y_2)").scale(0.6).next_to(dot2, UR, buff=0.1)
        line = Line(axes.c2p(x1, y1), axes.c2p(x2, y2))
        dash_line1 = DashedLine(axes.c2p(x1, y1), axes.c2p(x2, y1), color=BLUE)
        dash_line2 = DashedLine(axes.c2p(x2, y1), axes.c2p(x2, y2), color=BLUE)
        text_line1 = Tex("x_2-x_1").scale(0.5).next_to(dash_line1, DOWN, buff=0.1)
        text_line2 = Tex("y_2-y_1").scale(0.5).next_to(dash_line2, RIGHT, buff=0.1)
        arc_theta = draw_arc(axes.c2p(x2, y2), axes.c2p(x1, y1), axes.c2p(x2, y1), color=YELLOW, radius=0.3)
        text_theta = Tex("\\theta").scale(0.4).next_to(arc_theta, RIGHT, buff=0.1)
        self.play(Write(desc1))
        self.play(ShowCreation(dot1), ShowCreation(dot2),
                  TransformFromCopy(desc1[0], text_dot1), TransformFromCopy(desc1[1], text_dot2))
        self.play(Write(desc2))
        self.play(ShowCreation(line), ShowCreation(dash_line1), ShowCreation(dash_line2))
        self.play(Write(text_line1), Write(text_line2))
        self.play(ShowCreation(arc_theta), Write(text_theta))
        self.play(Write(desc3))
        self.wait(2)
        self.play(
            FadeOut(VGroup(desc1, dot1, dot2, text_dot1, text_dot2, line, dash_line1, dash_line2,
                           text_line1, text_line2, arc_theta, text_theta)),
            desc2.animate.next_to(title, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT),
            desc3.animate.next_to(desc1, RIGHT, buff=0.1),
            axes.animate.shift(RIGHT * 3),
        )
        self.wait()
        desc4 = Tex("y=\\frac{1-\\sin x}{2- \\cos x}").scale(0.6).next_to(desc2, DOWN, buff=0.5, aligned_edge=LEFT)
        arrow1 = add_right_arrow(desc4, length=0.5)
        desc5 = VGroup(
            Tex("(2,1)\\quad(\\cos x, \\sin x)"),
            Text("的斜率", t2c={"斜率": YELLOW})
        ).arrange(RIGHT).scale(0.6).next_to(arrow1, RIGHT, buff=0.2)
        self.play(Write(desc4))
        self.play(ShowCreation(arrow1))
        self.play(Write(desc5))
        self.wait()
        desc6 = Tex("\\cos x^2 + \\sin x^2 = 1").scale(0.6).next_to(desc4, DOWN, buff=0.5, aligned_edge=LEFT)
        axis_unit = axes.get_x_axis().unit_size
        circle = Circle(radius=axis_unit).move_to(axes.c2p(0, 0))
        self.play(Write(desc6))
        self.play(ShowCreation(circle))
        fix_point = Dot(axes.c2p(2, 1), color=BLUE).scale(0.5)
        text_fix_point = Tex("(2, 1)").scale(0.6).next_to(fix_point, UR, buff=0.1)
        update_group = self.create_update_group(circle.point_from_proportion(0), axes.c2p(2, 1))
        self.play(ShowCreation(update_group[0]))
        self.play(ShowCreation(fix_point), Write(text_fix_point))
        self.play(ShowCreation(update_group[1]))
        self.play(ShowCreation(update_group[2:]))
        self.wait()

        def update_point1(mob, alpha):
            mob.become(self.create_update_group(circle.point_from_proportion(alpha), axes.c2p(2, 1)))

        def update_point2(mob, alpha):
            mob.become(self.create_update_group(circle.point_from_proportion(alpha / 4), axes.c2p(2, 1)))

        def update_point3(mob, alpha):
            theta = math.atan(4 / 3)
            end_angle = PI * 3 / 2 + theta
            proportion = 0.25 + (end_angle / TAU - 0.25) * alpha
            mob.become(self.create_update_group(circle.point_from_proportion(proportion), axes.c2p(2, 1)))

        self.play(UpdateFromAlphaFunc(update_group, update_point1), run_time=4)
        self.wait()
        self.play(UpdateFromAlphaFunc(update_group, update_point2), run_time=2)
        desc7 = VGroup(
            Tex("min=0", color=YELLOW),
            Tex("max=\\frac{4}{3}", color=YELLOW)
        ).arrange(RIGHT, buff=0.3).scale(0.6).next_to(desc6, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc7[0]))
        self.wait()
        self.play(UpdateFromAlphaFunc(update_group, update_point3), run_time=2)
        desc8 = VGroup(
            Text("设切线的斜率为k，那么切线方程为"),
            Tex("y=k(x-2)+1")
        ).arrange(RIGHT).scale(0.6).next_to(desc7, DOWN, buff=0.2, aligned_edge=LEFT)
        desc9 = VGroup(
            Text("点O到切线的距离为"),
            Tex("\\frac{|k-\\frac{4}{3}|}{\\sqrt{k^2+1}}"),
            Tex("=1")
        ).arrange(RIGHT).scale(0.6).next_to(desc8, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc8[0]))
        self.wait()
        self.play(Write(desc8[1]))
        self.wait()
        pos_c = circle.point_from_proportion((PI * 3 / 2 + math.atan(4 / 3)) / TAU)
        self.play(Write(desc9[0]), ShowCreation(DashedLine(axes.c2p(0, 0), pos_c)))
        self.wait()
        self.play(Write(desc9[1:]), run_time=1.5)
        arrow2 = add_right_arrow(desc9, length=0.5)
        self.play(ShowCreation(arrow2))
        desc10 = Tex("k=\\frac{4}{3}").scale(0.6).next_to(arrow2, RIGHT, buff=0.2)
        self.play(Write(desc10))
        self.wait()
        self.play(Write(desc7[1]))
        self.play(ShowCreation(SurroundingRectangle(desc7, color=RED)))
        self.play(Write(subject[-1]))
        self.wait(5)

        # self.add(dot1, dot2, line, dash_line1, dash_line2, text_line1, text_line2)

        # text1 = Tex("(2, 1)")
        # text2 = Tex("(\\cos x, \\sin x)").shift(RIGHT * 3)
        # self.play(TransformFromCopy(subject[1], VGroup(text1, text2)))

    def create_update_group(self, pos: np.ndarray, fix_point: np.ndarray):
        dot = Dot(pos, color=BLUE).scale(0.5)
        line1 = Line(fix_point, pos, color=BLUE)
        dash_line1 = DashedLine(fix_point, np.array([fix_point[0], pos[1], 0]))
        dash_line2 = DashedLine(pos, np.array([fix_point[0], pos[1], 0]))
        arc = draw_arc(fix_point, pos, np.array([fix_point[0], pos[1], 0]), color=YELLOW, radius=0.3)
        return VGroup(dot, line1, dash_line1, dash_line2, arc)


class Graphic8(Scene):
    def construct(self) -> None:
        title = Title("数形结合-解析几何-两点距离").scale(0.9)
        self.add(title)
        subject = VGroup(
            Text("求"),
            Tex("\\sqrt{x^2-2x+2}"),
            Tex("+"),
            Tex("\\sqrt{x^2-6x+13}"),
            Text("的最小值"),
            Tex("5", color=GREEN)
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(subject[0: 5]))
        self.wait()
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            width=5,
            height=5,
            axis_config={"include_tip": True, "include_ticks": False, "include_numbers": False},
        ).shift(DOWN)
        self.play(ShowCreation(axes), run_time=2)
        x1 = -2
        y1 = -1
        x2 = 2
        y2 = 2
        dot1 = Dot(axes.c2p(x1, y1), color=BLUE)
        dot2 = Dot(axes.c2p(x2, y2), color=BLUE)
        text_dot1 = Tex("(x_1, y_1)").scale(0.6).next_to(dot1, DL, buff=0.1)
        text_dot2 = Tex("(x_2, y_2)").scale(0.6).next_to(dot2, UR, buff=0.1)
        desc1 = VGroup(
            Text("两点之间的距离"),
            Tex("d=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}", color=YELLOW)
        ).arrange(RIGHT).scale(0.6).next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT)
        self.play(ShowCreation(dot1), ShowCreation(dot2), Write(text_dot1), Write(text_dot2))
        self.play(Write(desc1[0]))
        line_dots = Line(dot1.get_center(), dot2.get_center())
        self.play(ShowCreation(line_dots), Write(desc1[1]))
        self.wait()
        self.play(
            FadeOut(VGroup(dot1, dot2, text_dot1, text_dot2, line_dots, desc1[0])),
            desc1[1].animate.next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT),
            axes.animate.shift(RIGHT * 3)
        )
        self.wait()
        desc2 = Tex("\\sqrt{x^2-2x+2}").scale(0.6).next_to(desc1[1], DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(TransformFromCopy(subject[1], desc2))
        arrow1 = add_right_arrow(desc2, length=0.5)
        self.play(ShowCreation(arrow1))
        desc3 = Tex("\\sqrt{(x-1)^2+(0-1)^2}").scale(0.6).next_to(arrow1, RIGHT, buff=0.2)
        self.play(Write(desc3))
        self.wait()
        desc4 = Tex("\\sqrt{x^2-6x+13}").scale(0.6).next_to(desc2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(TransformFromCopy(subject[3], desc4))
        arrow2 = add_right_arrow(desc4, length=0.5)
        self.play(ShowCreation(arrow2))
        desc5 = Tex("\\sqrt{(x-3)^2+(0-2)^2}").scale(0.6).next_to(arrow2, RIGHT, buff=0.2)
        self.play(Write(desc5))
        self.wait()
        pos_a = axes.c2p(1, 1)
        pos_b = axes.c2p(3, 2)
        pos_x = axes.c2p(2, 0)
        text_dot_a = Tex("A(1, 1)").scale(0.6).next_to(pos_a, DL, buff=0.1)
        text_dot_b = Tex("B(3, 2)").scale(0.6).next_to(pos_b, UR, buff=0.1)
        self.play(
            ShowCreation(Dot(pos_a, color=BLUE)),
            ShowCreation(Dot(pos_b, color=BLUE)),
            Write(text_dot_a),
            Write(text_dot_b)
        )
        dot_x = Dot(pos_x, color=BLUE)
        text_x = Tex("X(x,0)").scale(0.6).next_to(dot_x, DOWN, buff=0.1)
        line_xa = Line(pos_x, pos_a)
        line_xb = Line(pos_x, pos_b)
        self.play(ShowCreation(VGroup(dot_x, line_xa)), Write(text_x))
        arrow3 = add_right_arrow(desc3, length=0.5)
        desc3_1 = Tex("XA").scale(0.6).next_to(arrow3, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow3))
        self.play(Write(desc3_1), run_time=0.3)

        self.play(ShowCreation(line_xb))
        arrow4 = add_right_arrow(desc5, length=0.5)
        desc5_1 = Tex("XB").scale(0.6).next_to(arrow4, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow4))
        self.play(Write(desc5_1), run_time=0.3)
        desc6 = Tex(
            "d=XA+XB",
            "=XA'+XB",
            "\\ge AB=\\sqrt{3^2+4^2}=",
            "5"
        ).scale(0.6).next_to(desc4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc6[0]))

        def update_func1(mob):
            temp_pos_x = dot_x.get_center()
            mob[0].move_to(temp_pos_x)
            mob[1].put_start_and_end_on(temp_pos_x, pos_a)
            mob[2].put_start_and_end_on(temp_pos_x, pos_b)
            mob[3].next_to(dot_x, DOWN, buff=0.1)

        self.play(
            dot_x.animate.shift(LEFT * axes.get_y_axis().unit_size * 5),
            UpdateFromFunc(VGroup(dot_x, line_xa, line_xb, text_x), update_func1),
            run_time=4,
        )
        self.wait()
        self.play(
            dot_x.animate.shift(RIGHT * axes.get_y_axis().unit_size * 5.5),
            UpdateFromFunc(VGroup(dot_x, line_xa, line_xb, text_x), update_func1),
            run_time=4,
        )
        pos_a_symmetry = axes.c2p(1, -1)
        pos_x = dot_x.get_center()
        self.play(
            ShowCreation(DashedLine(pos_a, pos_a_symmetry)),
            Write(Tex("A'(1,-1)").scale(0.6).next_to(pos_a_symmetry, DOWN, buff=0.1))
        )
        self.wait()
        self.play(
            FadeOut(line_xa),
            ShowCreation(Line(pos_x, pos_a_symmetry, color=BLUE)),
            ShowCreation(Line(pos_x, pos_b, color=BLUE)),
        )
        self.play(Write(desc6[1]))
        self.wait()
        self.play(ShowCreation(Line(pos_b, pos_a_symmetry, color=YELLOW)))
        self.play(Write(desc6[2:]))
        self.play(TransformFromCopy(desc6[-1], subject[-1]))
        self.wait(5)


class Graphic9(Scene):
    def construct(self) -> None:
        title = Title("数形结合-解析几何-点到直线的距离").scale(0.9)
        self.add(title)
        subject = VGroup(
            Tex("x_0^2+y_0^2=1"),
            Text("，求"),
            Tex("|3x_0+4y_0-12|"),
            Text("的取值范围"),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(subject))
        self.wait()
        axes = Axes(
            x_range=[-3, 5, 1],
            y_range=[-3, 5, 1],
            width=5,
            height=5,
            axis_config={"include_tip": True, "include_ticks": True, "include_numbers": False},
        ).shift(DOWN)
        # self.play(ShowCreation(axes), run_time=2)
        # 3x+4y-12=0
        func1 = axes.get_graph(lambda x: (12 - 3 * x) / 4, x_range=[-1, 6])
        self.play(ShowCreation(func1))
        desc1 = VGroup(
            Text("点"), Tex("(x_0,y_0)"),
            Text("到直线"), Tex("Ax+By+C=0"),
            Text("的距离")
        ).arrange(RIGHT).scale(0.6).next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT)
        desc2 = Tex("d=\\frac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}", color=YELLOW).scale(0.6).next_to(
            desc1, DOWN, buff=0.3, aligned_edge=LEFT)
        pos_x = axes.c2p(1, 0)
        dot_x = Dot(pos_x, color=BLUE).scale(0.5)
        text_x = Tex("(x_0,y_0)").scale(0.6).next_to(pos_x, DOWN, buff=0.1)
        text_func1 = Tex("Ax+By+C=0").scale(0.6).move_to(axes.c2p(5, -3 / 4))
        # x到直线3x+4y-12=0的垂线4x-3y-4=0
        func2 = axes.get_graph(lambda x: (4 * x - 4) / 3, x_range=[1, 52 / 25], color=YELLOW)
        self.play(Write(desc1), ShowCreation(dot_x), Write(text_x), Write(text_func1))
        self.play(ShowCreation(func2), Write(desc2))
        self.wait()
        self.play(
            FadeOut(VGroup(desc1, func1, func2, text_func1, text_x, dot_x)),
            desc2.animate.next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT),
        )
        axes.shift(RIGHT * 2)
        self.play(ShowCreation(SurroundingRectangle(subject[0], color=RED)))
        self.play(ShowCreation(axes), run_time=2)
        circle = Circle(radius=axes.get_x_axis().unit_size, color=WHITE).move_to(axes.c2p(0, 0))
        mob_group = self.create_update_group(circle.point_from_proportion(0), axes)
        self.play(ShowCreation(circle), Write(mob_group[0]))
        desc3 = Tex("A=3,B=4,C=-12").scale(0.6).next_to(desc2, DOWN, buff=0.3, aligned_edge=LEFT)
        func3 = axes.get_graph(lambda x: (12 - 3 * x) / 4, x_range=[-2, 5])
        self.play(Write(desc3))
        self.play(ShowCreation(func3), ShowCreation(mob_group[1]),
                  Write(Tex("3x+4y-12").scale(0.6).next_to(func3.get_end(), BOTTOM, buff=0.1)))
        desc4 = Tex("d=\\frac{|3x_0+4y_0-12|}{5}", color=YELLOW).scale(0.6).next_to(
            desc3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc4), ShowCreation(mob_group[2]))
        arrow1 = add_right_arrow(desc4, length=0.5)
        self.play(ShowCreation(arrow1))
        desc5 = Tex("|3x_0+4y_0-12|=5d", color=YELLOW).scale(0.6).next_to(arrow1, RIGHT, buff=0.2)
        self.play(Write(desc5))

        def update_pos1(mob, alpha):
            mob.become(self.create_update_group(circle.point_from_proportion(alpha), axes))

        self.play(UpdateFromAlphaFunc(mob_group, update_pos1), run_time=4, rate_func=smooth)
        self.wait()
        dash_line1 = self.get_line(axes.c2p(0, 0), axes, True)
        self.play(ShowCreation(dash_line1))
        text_o = Tex("O").scale(0.5).next_to(axes.c2p(0, 0), DOWN, buff=0.1)
        text_a = Tex("A").scale(0.5).next_to(
            axes.c2p(0, 0) + dash_line1.get_unit_vector() * axes.get_x_axis().unit_size, OUT, buff=0.1)
        text_b = Tex("B").scale(0.5).next_to(dash_line1.get_end(), OUT, buff=0.1)
        text_c = Tex("C").scale(0.5).next_to(axes.c2p(1, 0), DOWN, buff=0.1)
        text_d = Tex("D").scale(0.5).next_to(mob_group[2].get_end(), UR, buff=0.1)
        self.play(Write(VGroup(text_o, text_a, text_b, text_c, text_d)), FadeOut(mob_group[0]))
        desc6 = Tex("OB<OC+OD\\rightarrow OA+AB<OC+CD\\rightarrow AB<CD").scale(0.5).next_to(
            desc4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc6))
        angle = math.atan(4 / 3)

        def update_pos2(mob, alpha):
            proportion = angle / TAU * alpha
            mob.become(self.create_update_group(circle.point_from_proportion(proportion), axes))

        self.play(UpdateFromAlphaFunc(mob_group, update_pos2), run_time=2, rate_func=smooth)
        desc7 = Tex("d_{min}=AB=\\frac{12}{5}-1=\\frac{7}{5}").scale(0.5).next_to(
            desc6, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(desc7))
        self.wait()

        def update_pos3(mob, alpha):
            proportion = angle / TAU + alpha / 2
            mob.become(self.create_update_group(circle.point_from_proportion(proportion), axes))

        desc8 = Tex("d_{max}=2R+d_{min}=\\frac{17}{5}").scale(0.5).next_to(
            desc7, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(UpdateFromAlphaFunc(mob_group, update_pos3), run_time=3, rate_func=smooth)
        self.play(Write(desc8))
        rect1 = SurroundingRectangle(VGroup(desc7, desc8), color=RED)
        self.play(ShowCreation(rect1))
        self.wait()
        desc9 = Tex("d\\in[\\frac{7}{5},\\frac{17}{5}]").scale(0.6).next_to(desc4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeOut(VGroup(desc6, desc7, desc8, rect1), run_time=0.5), Write(desc9, run_time=1))
        arrow2 = add_right_arrow(desc9, length=0.5)
        self.play(ShowCreation(arrow2))
        desc10 = VGroup(Tex("|3x_0+4y_0-12|\\in"), Tex("[7,17]", color=GREEN)).arrange(RIGHT).scale(0.6).next_to(
            arrow2, RIGHT, buff=0.2)
        self.play(Write(desc10))
        self.wait(5)

    def create_update_group(self, pos_x, axes):
        text_x = Tex("(x_0,y_0)").scale(0.6).next_to(pos_x, DOWN, buff=0.1)
        dot_x = Dot(pos_x, color=BLUE).scale(0.4)
        return VGroup(text_x, dot_x, self.get_line(pos_x, axes, color=YELLOW))

    def get_line(self, pos_x, axes, is_dash=False, **kwargs):
        x = axes.p2c(pos_x)[0]
        y = axes.p2c(pos_x)[1]
        # 点(x,y)到直线3x+4y-12=0的垂线4x-3y-c=0
        c = 4 * x - 3 * y
        x1 = (12 * 3 + 4 * c) / (3 ** 2 + 4 ** 2)
        y1 = (12 * 4 - 3 * c) / (3 ** 2 + 4 ** 2)
        if is_dash:
            return DashedLine(pos_x, axes.c2p(x1, y1), **kwargs)
        else:
            return Line(pos_x, axes.c2p(x1, y1), **kwargs)


class Graphic10(Scene):
    def construct(self) -> None:
        title = Title("数形结合-解析几何-函数").scale(0.9)
        self.add(title)
        subject = VGroup(
            Tex("x"),
            Text("满足"),
            Tex("\\sqrt{4x-x^2}"),
            Tex("\\ge"),
            Tex("x"),
            Text("求"), Tex("x"), Text("的取值范围")
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(subject))
        self.wait()
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-3, 4, 1],
            width=5,
            height=5,
            axis_config={"include_tip": True, "include_ticks": True, "include_numbers": False},
        ).shift(DOWN + RIGHT * 2)
        self.add(axes)
        # self.play(ShowCreation(axes), run_time=2)
        desc1 = VGroup(
            Text("设"),
            Tex("y_1="),
            Tex("\\sqrt{4x-x^2}"),
            Text("则"),
            Tex("y_1^2=4x-x^2"),
            Tex("="),
            Tex("4-(x-2)^2"),
        ).arrange(RIGHT).scale(0.6).next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT)
        self.play(Write(desc1[0:2]))
        self.play(TransformFromCopy(subject[2], desc1[2]))
        self.play(Write(desc1[3:5]))
        self.play(Write(desc1[5:]))
        self.wait()
        desc2 = Tex("y_1^2+(x-2)^2=2^2", "\\quad y>0", color=YELLOW).scale(0.6).next_to(
            desc1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc2[0]))
        unit_size = axes.get_x_axis().unit_size
        circle = Circle(radius=unit_size * 2, color=YELLOW).shift(axes.c2p(2, 0))
        self.play(ShowCreation(circle))
        func1 = axes.get_graph(lambda x: math.sqrt(4 * x - x ** 2), x_range=[0, 4], color=YELLOW)
        self.play(ShowCreation(desc2[1]))
        rect1 = SurroundingRectangle(desc2[1], color=RED, buff=0.1)
        self.play(ShowCreation(rect1), run_time=0.5)
        self.play(FadeOut(circle), ShowCreation(func1))
        self.wait()

        desc3 = VGroup(
            Text("设"),
            Tex("y_2=", color=BLUE),
            Tex("x", color=BLUE)
        ).scale(0.6).arrange(RIGHT).next_to(desc2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(desc3[0:2]))
        self.play(TransformFromCopy(subject[4], desc3[2]))
        func2 = axes.get_graph(lambda x: x, x_range=[0, 4], color=BLUE)
        self.play(ShowCreation(func2))
        desc4 = Tex("y1 \\ge y2").scale(0.6).next_to(desc3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc4))
        func3 = axes.get_graph(lambda x: math.sqrt(4 * x - x ** 2), x_range=[0, 2], color=GREEN)
        self.play(ShowCreation(func3), run_time=2)
        self.play(Write(Tex("(2,2)").scale(0.5).next_to(axes.c2p(2, 2), UP, buff=0.1)))
        self.play(ShowCreation(DashedLine(axes.c2p(2, 2), axes.c2p(2, 0))))
        arrow1 = add_right_arrow(desc4, length=0.5)
        self.play(ShowCreation(arrow1))
        desc5 = Tex("x\\in[0,2]", color=GREEN).scale(0.6).next_to(arrow1, RIGHT, buff=0.2)
        self.play(Write(desc5))
        self.wait(5)


class Graphic11(Scene):
    def construct(self) -> None:
        title = Title("数形结合-抽象函数性质举例-导函数").scale(0.9)
        self.add(title)
        subject1 = VGroup(
            Text("(2022·新高考Ⅰ)", color=BLUE),
            Text("已知函数"),
            Tex("f(x)"),
            Text("及其导函数", t2c={"导函数": YELLOW}),
            Tex("f'(x)"),
            Text("的定义域均为R，记", t2c={"定义域": YELLOW}),
            Tex("g(x)=f'(x)")
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=0.5)
        subject2 = VGroup(
            Text("若"),
            Tex("f(\\frac{3}{2}-2x)"),
            Tex("\\quad"),
            Tex("g(2+x)"),
            Text("均为偶函数，则", t2c={"偶函数": YELLOW}),
            Tex("(\\quad\\quad\\quad)")
        ).arrange(RIGHT).scale(0.5).next_to(subject1, DOWN, buff=0.2, aligned_edge=LEFT)
        self.add(subject1, subject2)
        subject3_1 = Tex("A.\\quad", " f(0)=0").scale(0.5).next_to(subject2, DOWN, buff=0.5, aligned_edge=LEFT)
        subject3_2 = Tex("B.\\quad", " g(-\\frac{1}{2})=0").scale(0.5).next_to(subject3_1, RIGHT, buff=2)
        subject4_1 = Tex("C.\\quad", " f(-1)=f(4)").scale(0.5).next_to(subject3_1, DOWN, buff=0.4, aligned_edge=LEFT)
        subject4_2 = Tex("D.\\quad", " g(-1)=g(2)").scale(0.5).next_to(subject3_2, DOWN, buff=0.4, aligned_edge=LEFT)
        self.add(subject3_1, subject3_2, subject4_1, subject4_2)
        self.wait(2)
        self.play(VGroup(subject3_1, subject3_2, subject4_1, subject4_2).animate.arrange(RIGHT, buff=1).shift(UP * 0.8))
        self.play(FadeOut(VGroup(subject3_1, subject3_2, subject4_1, subject4_2)), run_time=0.5)
        axes1 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-10, 10, 1],
            width=6,
            height=4,
            axis_config={"include_tip": True, "include_numbers": False},
            x_axis_config={"include_ticks": True, },
            y_axis_config={"include_ticks": False, },
        ).shift(DOWN * 1.8 + RIGHT * 2)
        self.add(axes1)
        desc1 = VGroup(
            Tex("f(\\frac{3}{2}-2x)"),
            Text("为偶函数")
        ).arrange(RIGHT).scale(0.4).next_to(title, DOWN, buff=1.8, aligned_edge=LEFT).shift(LEFT)
        self.play(TransformFromCopy(subject2[1], desc1[0]))
        self.play(Write(desc1[1]))
        arrow1 = add_right_arrow(desc1, length=0.5)
        self.play(ShowCreation(arrow1))
        desc1_1 = Tex("f(\\frac{3}{2}-2x)=f(\\frac{3}{2}+2x)").scale(0.4).next_to(arrow1, RIGHT, buff=0.2)
        self.play(Write(desc1_1))
        desc2 = VGroup(
            Tex("f(\\frac{3}{2}-\\frac{1}{2})=f(\\frac{3}{2}+\\frac{1}{2})"),
            Tex("f(\\frac{3}{2}-1)=f(\\frac{3}{2}+1)"),
            Tex("f(\\frac{3}{2}-2)=f(\\frac{3}{2}+2)")
        ).arrange(DOWN).scale(0.4).next_to(desc1, DOWN, buff=0.3, aligned_edge=LEFT)

        def test_func1(x):
            return (x - 3 / 2) ** 2 + 1

        def test_func2(x):
            return 6 + 5 * np.sin(x * PI)

        def test_func3(x):
            # 6 + 5 * np.sin(x * PI)的斜率
            return 5 * PI * np.cos(x * PI)

        self.play(Write(desc2))

        example_dots = VGroup(
            Dot(axes1.c2p(1, test_func1(1)), color=BLUE).scale(0.5),
            Dot(axes1.c2p(2, test_func1(2)), color=BLUE).scale(0.5),
            Dot(axes1.c2p(1 / 2, test_func1(1 / 2)), color=BLUE).scale(0.5),
            Dot(axes1.c2p(3 - 1 / 2, test_func1(3 - 1 / 2)), color=BLUE).scale(0.5),
            Dot(axes1.c2p(-1 / 2, test_func1(-1 / 2)), color=BLUE).scale(0.5),
            Dot(axes1.c2p(3 + 1 / 2, test_func1(3 + 1 / 2)), color=BLUE).scale(0.5),
        )
        self.play(ShowCreation(example_dots))
        self.wait()
        dash_line1 = DashedLine(axes1.c2p(1.5, 6), axes1.c2p(1.5, -6))
        dash_text1 = Tex("x=\\frac{3}{2}", color=YELLOW).scale(0.4).next_to(dash_line1, DOWN, buff=0.1)
        self.play(ShowCreation(dash_line1))
        self.play(Write(dash_text1))
        self.wait()
        func1 = axes1.get_graph(test_func1, x_range=[-1 / 2, 7 / 2], color=BLUE)
        self.play(ShowCreation(func1), run_time=3)
        arrow2 = add_right_arrow(desc2, length=0.5)
        desc2_1 = VGroup(
            Tex("f(x)"),
            Text("关于"),
            Tex("x=\\frac{3}{2}"),
            Text("轴对称", color=YELLOW)
        ).arrange(RIGHT).scale(0.4).next_to(arrow2, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow2))
        self.play(Write(desc2_1))
        self.wait(2)
        self.play(
            FadeOut(VGroup(desc2, desc1_1, arrow2)),
            desc2_1.animate.next_to(arrow1, RIGHT, buff=0.3)
        )
        desc3 = VGroup(
            Tex("g(2+x)"),
            Text("为偶函数")
        ).arrange(RIGHT).scale(0.4).next_to(desc1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc3))
        arrow3 = add_right_arrow(desc3, length=0.5)
        self.play(ShowCreation(arrow3))
        desc3_1 = VGroup(Tex("g(x)"), Text("关于"), Tex("x=2"), Text("轴对称", color=YELLOW)
                         ).arrange(RIGHT).scale(0.4).next_to(arrow3, RIGHT, buff=0.2)
        self.play(Write(desc3_1))
        self.wait()
        desc4 = VGroup(
            Tex("g(x)=f'(x)\\rightarrow g(x)"),
            Text("表示"),
            Tex("(x,f(x))"),
            Text("处的切线斜率", t2c={"切线斜率": YELLOW})
        ).arrange(RIGHT).scale(0.4).next_to(desc3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc4), run_time=2)

        desc5 = VGroup(
            Text("假设", color=GREY),
            Tex("f(x)"),
            Text("在"),
            Tex("[\\frac{3}{2}, 2]"),
            Text("上单调递增", t2c={"单调递增": YELLOW})
        ).arrange(RIGHT).scale(0.4).next_to(desc4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc5))
        func2 = axes1.get_graph(test_func2, x_range=[3 / 2, 2], color=BLUE)
        self.play(FadeOut(VGroup(func1, example_dots), run_time=1), ShowCreation(func2, run_time=2))
        self.wait()
        arrow4 = add_right_arrow(desc5, length=0.5)
        rect1 = SurroundingRectangle(desc3_1, color=RED)
        self.play(ShowCreation(arrow4), ShowCreation(rect1))
        desc5_1 = VGroup(
            Tex("f(x)"),
            Text("在"),
            Tex("[2, \\frac{5}{2}]"),
            Text("上也是单调递增", t2c={"单调递增": YELLOW})
        ).arrange(RIGHT).scale(0.4).next_to(arrow4, RIGHT, buff=0.2)
        self.play(Write(desc5_1))
        desc6 = VGroup(
            Text("由于切线斜率关于", t2c={"切线斜率": YELLOW}),
            Tex("x=2", color=BLUE),
            Text("轴对称", color=YELLOW),
        ).arrange(RIGHT).scale(0.4).next_to(desc5_1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc6))
        dot1 = Dot(axes1.c2p(2, test_func2(2)), color=GREEN).scale(1)
        func3 = axes1.get_graph(test_func2, x_range=[1.99, 5 / 2], color=YELLOW)
        self.play(ShowCreation(dot1))
        self.play(ShowCreation(func3), run_time=2)
        self.wait()
        desc7 = VGroup(
            Tex("f(x)"),
            Text("关于点", t2c={"点": YELLOW}),
            Tex("(2,f(2))"),
            Text("点对称", color=YELLOW)
        ).arrange(RIGHT).scale(0.4).next_to(desc5, DOWN, buff=0.6 + desc5.get_height(), aligned_edge=LEFT)
        self.play(Write(desc7))
        self.wait()
        self.play(
            FadeOut(VGroup(desc3_1, desc4, desc5, arrow4, desc5_1, rect1, desc6)),
            desc7.animate.next_to(arrow3, RIGHT, buff=0.2)
        )
        rect2 = SurroundingRectangle(desc2_1, color=RED)
        rect3 = SurroundingRectangle(desc7, color=RED)
        func4 = axes1.get_graph(test_func2, x_range=[1 / 2, 3 / 2], color=WHITE)
        self.play(ShowCreation(rect2))
        self.play(ShowCreation(func4), run_time=2)
        func5 = axes1.get_graph(test_func2, x_range=[1, 3 / 2], color=BLUE)
        func6 = axes1.get_graph(test_func2, x_range=[5 / 2, 3], color=BLUE)
        self.wait()
        self.play(FadeOut(rect2), ShowCreation(rect3))
        dot2 = Dot(axes1.c2p(1, test_func2(1)), color=GREEN).scale(1)
        self.play(ShowCreation(dot2))
        self.play(Transform(func5, func6), run_time=2)
        self.wait()
        func7 = axes1.get_graph(test_func2, x_range=[0, 1 / 2], color=BLUE)
        self.play(FadeOut(rect3), ShowCreation(rect2))
        self.play(TransformFromCopy(func6, func7), run_time=2)
        self.wait()
        func8 = axes1.get_graph(test_func2, x_range=[0, 1], color=WHITE)
        func9 = axes1.get_graph(test_func2, x_range=[3, 4], color=WHITE)
        dot3 = Dot(axes1.c2p(3, test_func2(3)), color=GREEN).scale(1)
        self.play(FadeOut(rect2), ShowCreation(rect3))
        self.play(Transform(func8, func9), ShowCreation(dot3), run_time=2)
        self.wait()
        func10 = axes1.get_graph(test_func2, x_range=[-1, 0], color=WHITE)
        self.play(FadeOut(rect3), ShowCreation(rect2))
        self.play(TransformFromCopy(func9, func10), run_time=2)
        self.wait()
        desc8 = Text("得到了一个类似正弦函数的图像", t2c={"正弦函数": YELLOW}).scale(0.4).next_to(
            desc3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc8))
        self.wait()
        self.play(
            VGroup(desc1, arrow1, desc2_1, desc3, arrow3, desc7, desc8).animate.shift(DOWN),
            ShowCreation(VGroup(subject3_1, subject3_2, subject4_1, subject4_2)),
            FadeOut(rect2),
        )
        self.wait()
        dot4 = Dot(axes1.c2p(0, test_func2(0)), color=WHITE).scale(1)
        self.play(ShowCreation(dot4))
        no1 = SVGMobject("../assets/no.svg").scale(0.2).move_to(subject3_1.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(no1))
        self.wait()
        dash_line2 = DashedLine(axes1.c2p(0, test_func2(0.5)), axes1.c2p(2, test_func2(0.5)), color=WHITE)
        dot5 = Dot(axes1.c2p(0.5, test_func2(0.5)), color=WHITE).scale(1)
        self.play(ShowCreation(dash_line2), ShowCreation(dot5))
        yes2 = SVGMobject("../assets/yes.svg").scale(0.2).move_to(subject3_2.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(yes2))
        self.wait()
        dash_line3 = DashedLine(axes1.c2p(-1, test_func2(-1)), axes1.c2p(4, test_func2(4)), color=WHITE)
        self.play(
            ShowCreation(Dot(axes1.c2p(-1, test_func2(-1)), color=WHITE).scale(1)),
            ShowCreation(Dot(axes1.c2p(4, test_func2(4)), color=WHITE).scale(1)),
            Write(Tex("(-1,f(-1))", color=WHITE).scale(0.4).next_to(axes1.c2p(-1, test_func2(-1)), LEFT, buff=0.1)),
            Write(Tex("(4,f(4))", color=WHITE).scale(0.4).next_to(axes1.c2p(4, test_func2(4)), RIGHT, buff=0.1)),
        )
        self.play(ShowCreation(dash_line3))
        yes3 = SVGMobject("../assets/yes.svg").scale(0.2).move_to(subject4_1.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(yes3))
        self.wait()
        k1 = test_func3(-1)
        c1 = test_func2(-1) - k1 * (-1)
        func10 = axes1.get_graph(lambda x: k1 * x + c1, x_range=[-1.1, -0.5], color=WHITE)
        k2 = test_func3(2)
        c2 = test_func2(2) - k2 * 2
        func11 = axes1.get_graph(lambda x: k2 * x + c2, x_range=[1.5, 2.1], color=WHITE)
        self.play(ShowCreation(func10), ShowCreation(func11))
        no4 = SVGMobject("../assets/no.svg").scale(0.2).move_to(subject4_2.get_right() + RIGHT * 0.1 + DOWN * 0.2)
        self.play(ShowCreation(no4))
        self.wait()
        result = Tex("B,C", color=GREEN).scale(0.5).next_to(subject2[5], OUT)
        self.play(Write(result))
        self.wait(5)

    class Test(Scene):
        def construct(self) -> None:
            yes = SVGMobject("../assets/yes.svg").scale(0.2)
            self.add(yes)
