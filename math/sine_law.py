import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')


from yj.common.utils.math_utils import get_circle_center_from_triangle, cal_dis, draw_arc
from yj.common.math.object_utils import get_right_angle

from manimlib import *


class Sine1(Scene):
    def construct(self) -> None:
        title = Title("正弦定理").scale(0.9)
        self.add(title)
        # 三角形ABC
        origin = ORIGIN + DOWN + 2 * RIGHT
        pos_b = origin + UP * 3
        pos_a = origin + LEFT * 3
        pos_c = origin + RIGHT * 1
        triangle = Polygon(pos_a, pos_b, pos_c).set_stroke(width=4)
        point_a = Tex("A").next_to(pos_a, LEFT, buff=0.1).scale(0.8)
        point_b = Tex("B").next_to(pos_b, UP, buff=0.1).scale(0.8)
        point_c = Tex("C").next_to(pos_c, RIGHT, buff=0.1).scale(0.8)
        self.play(ShowCreation(triangle))
        self.play(Write(point_a), Write(point_b), Write(point_c))
        line_ab = Line(pos_a, pos_b)
        line_bc = Line(pos_b, pos_c)
        line_ca = Line(pos_c, pos_a)
        text_a = Tex("a", color=YELLOW).next_to(line_bc, OUT).scale(0.9)
        text_b = Tex("b", color=GREEN).next_to(line_ca, OUT).scale(0.9)
        text_c = Tex("c", color=BLUE).next_to(line_ab, OUT).scale(0.9)
        arc_a = draw_arc(pos_b, pos_a, pos_c, radius=0.5, color=YELLOW)
        arc_b = draw_arc(pos_c, pos_b, pos_a, radius=0.5, color=GREEN)
        arc_c = draw_arc(pos_a, pos_c, pos_b, radius=0.5, color=BLUE)
        # 正弦定理
        formula1 = Tex(
            "\\frac{a}{\\sin A}",
            " = \\frac{b}{\\sin B}",
            " = \\frac{c}{\\sin C}",
            " = 2R"
        ).scale(0.7).next_to(title, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT)
        self.play(Write(text_a), ShowCreation(arc_a))
        self.play(Write(formula1[0]))
        self.wait()
        self.play(Write(text_b), ShowCreation(arc_b))
        self.play(Write(formula1[1]))
        self.wait()
        self.play(Write(text_c), ShowCreation(arc_c))
        self.play(Write(formula1[2]))

        self.wait()
        pos_o = get_circle_center_from_triangle(pos_a, pos_b, pos_c)
        radius = cal_dis(pos_o, pos_a)
        circle = Circle(radius=radius, color=WHITE).move_to(pos_o)
        dot_0 = Dot(pos_o)
        point_o = Tex("O").next_to(pos_o, DOWN, buff=0.1).scale(0.8)
        self.add(point_o, dot_0)
        self.play(ShowCreation(circle))

        self.wait()
        line_oc = Line(pos_c, pos_o)
        text_r = Tex("R").next_to(line_oc, OUT).scale(0.7)
        self.play(ShowCreation(line_oc), Write(text_r))
        self.play(Write(formula1[3]))

        pos_d = pos_o + line_oc.get_unit_vector() * radius
        dash_line_od = DashedLine(pos_o, pos_d)
        point_d = Tex("D").next_to(pos_d, LEFT, buff=0.1).scale(0.8)
        dash_line_da = DashedLine(pos_d, pos_a)
        self.wait()
        self.play(ShowCreation(dash_line_od), Write(point_d))
        self.play(ShowCreation(dash_line_da))
        desc = VGroup(
            Text("通过圆周角定理得到", t2c={'圆周角': YELLOW}, ),
            Tex("\\angle ABC = \\angle ADC"),
        ).arrange(RIGHT).scale(0.7).next_to(circle, DOWN, buff=1)
        self.play(Write(desc[0]))

        # 圆弧AC
        angle_aoc = angle_between_vectors(pos_a - pos_o, pos_c - pos_o)
        arc_ac = ArcBetweenPoints(pos_a, pos_c, angle=angle_aoc).set_color(RED)
        self.play(ShowCreation(arc_ac))
        arc_adc = draw_arc(pos_a, pos_d, pos_c, radius=0.5, color=RED)
        self.play(ShowCreation(arc_adc), Write(desc[1]))
        self.wait()
        formula2 = Tex(
            "\\frac{b}{\\sin B} = \\frac{b}{\\sin \\angle ADC}",
            " = CD = 2R"
        ).scale(0.7).next_to(formula1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(formula2[0]))

        desc_temp = VGroup(
            Tex("CD"),
            Text("是直径", t2c={'直径': YELLOW}, ),
            Tex("\\Rightarrow \\angle DAC = 90^{\\circ}"),
        ).arrange(RIGHT).scale(0.7).next_to(circle, DOWN, buff=1)
        right_angle_a = get_right_angle(pos_a, RIGHT * 0.25, UP * 0.25)
        self.play(Transform(desc, desc_temp), ShowCreation(right_angle_a))
        self.wait()
        self.play(Write(formula2[1]))
        self.wait(5)

