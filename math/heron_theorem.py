import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.common.math.object_utils import get_right_angle, add_right_arrow, get_rect, add_arrow_from_to
from manimlib import *


class Heron(Scene):
    def construct(self) -> None:
        title = Title('海伦公式').scale(0.9)
        self.add(title)
        # 三角形ABC
        origin = ORIGIN + RIGHT
        pos_a = origin + UP * 2
        pos_b = origin + LEFT * 2
        pos_c = origin + RIGHT * 1
        triangle = Polygon(pos_a, pos_b, pos_c)
        point_a = Tex('A').next_to(pos_a, UP, buff=0.1).scale(0.8)
        point_b = Tex('B').next_to(pos_b, LEFT, buff=0.1).scale(0.8)
        point_c = Tex('C').next_to(pos_c, RIGHT, buff=0.1).scale(0.8)
        self.play(ShowCreation(triangle), Write(point_a), Write(point_b), Write(point_c))
        text_a = Tex('a').scale(0.8).next_to((pos_b + pos_c) / 2, DOWN, buff=0.1)
        text_b = Tex('b').scale(0.8).next_to((pos_a + pos_c) / 2, RIGHT, buff=0.1)
        text_c = Tex('c').scale(0.8).next_to((pos_a + pos_b) / 2, LEFT, buff=0.1)
        self.play(Write(text_a), Write(text_b), Write(text_c))
        self.wait()

        desc1 = VGroup(
            Text("设"),
            Tex("p = \\frac{a+b+c}{2}"),
        ).scale(0.7).arrange(RIGHT).next_to(triangle, DOWN, buff=1).shift(LEFT)
        # 三角形abc
        formula = Tex("\\triangle ABC=\\sqrt{p(p-a)(p-b)(p-c)}").scale(0.7)
        formula_s = Tex("S").next_to(formula, LEFT, buff=0).scale(1.1).shift(UP * 0.05)
        formula_group = VGroup(formula_s, formula).next_to(desc1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(desc1))
        self.play(Write(formula_group))
        self.wait()
        self.play(FadeOut(desc1), FadeOut(formula_group))
        self.wait()
        right_offset = RIGHT * 2
        pos_a += right_offset
        pos_b += right_offset
        pos_c += right_offset
        triangle_group = VGroup(triangle, point_a, point_b, point_c, text_a, text_b, text_c)
        self.play(
            triangle_group.shift, right_offset,
            desc1.shift, right_offset + RIGHT
        )
        self.wait()
        pos_d = pos_a + DOWN * 2
        point_d = Tex('D').next_to(pos_d, DOWN, buff=0.1).scale(0.8)
        dash_line_ad = DashedLine(pos_a, pos_d)
        right_angle = get_right_angle(pos_d, LEFT * 0.2, UP * 0.2)
        self.play(ShowCreation(dash_line_ad))
        self.play(Write(point_d), ShowCreation(right_angle), run_time=0.5)
        text_h = Tex('h', color=GREEN).scale(0.8).next_to((pos_a + pos_d) / 2, LEFT, buff=0.1)
        self.play(Write(text_h))
        self.wait()

        text_x = Tex('x', color=BLUE).scale(0.8).next_to((pos_b + pos_d) / 2, DOWN, buff=0.1)
        text_y = Tex('y', color=BLUE).scale(0.8).next_to((pos_d + pos_c) / 2, DOWN, buff=0.1)

        bottom_desc = VGroup(
            Tex("BD=x,DC=y"),
            Text("由勾股定理可知", t2c={'勾股定理': YELLOW}),
        ).arrange(RIGHT, buff=0.3).scale(0.7).move_to(ORIGIN + DOWN * 3)
        self.play(Write(bottom_desc[0]), ShowCreation(text_x), ShowCreation(text_y))
        self.play(Write(bottom_desc[1]))
        self.wait()

        derivation1 = VGroup(
            Tex("x^2", "+", "h^2", "=", "c^2"),
            Tex("y^2", "+", "h^2", "=", "b^2"),
        ).arrange(DOWN, buff=0.4).scale(0.6).next_to(title, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT * 0.5)

        self.play(TransformFromCopy(Line(pos_b, pos_d, color=BLUE), derivation1[0][0]), run_time=2)
        self.play(Write(derivation1[0][1]), run_time=0.5)
        self.play(TransformFromCopy(Line(pos_d, pos_a, color=BLUE), derivation1[0][2]), run_time=2)
        self.play(Write(derivation1[0][3]), run_time=0.5)
        self.play(TransformFromCopy(Line(pos_a, pos_b, color=BLUE), derivation1[0][4]), run_time=2)
        self.wait()

        self.play(
            TransformFromCopy(Line(pos_c, pos_d, color=BLUE), derivation1[1][0], run_time=2),
            Write(derivation1[1][1], run_time=0.5),
            TransformFromCopy(Line(pos_d, pos_a, color=BLUE), derivation1[1][2], run_time=2),
            Write(derivation1[1][3], run_time=0.5),
            TransformFromCopy(Line(pos_a, pos_c, color=BLUE), derivation1[1][4], run_time=2),
        )
        self.play(FadeOut(bottom_desc))

        arrow1 = add_right_arrow(derivation1)
        temp_rect1 = get_rect(VGroup(derivation1[0][2], derivation1[1][2]), buff=0.1, color=RED)
        derivation2 = Tex("x^2-y^2=c^2-b^2").scale(0.6).next_to(arrow1, RIGHT, buff=0.15)
        self.play(ShowCreation(temp_rect1))
        self.play(ShowCreation(arrow1))
        self.play(Write(derivation2))

        derivation3 = Tex("(x+y)", "(x-y)=c^2-b^2").scale(0.6).next_to(derivation1, DOWN, buff=0.4, aligned_edge=LEFT)
        arrow2 = add_arrow_from_to(derivation2.get_center() + DOWN * 0.2, derivation3.get_center() + UP * 0.2)
        self.play(ShowCreation(arrow2))
        self.play(Write(derivation3))
        derivation4 = Tex("x", "+y", "=a").scale(0.6).next_to(derivation3, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(TransformFromCopy(Line(pos_b, pos_c, color=BLUE), derivation4, run_time=2))

        brace1 = Brace(VGroup(derivation3, derivation4), LEFT)
        self.play(ShowCreation(brace1))
        temp_rect2 = get_rect(VGroup(derivation3[0], derivation4[0], derivation4[1]), buff=0.1, color=RED)
        self.play(ShowCreation(temp_rect2))
        self.wait()

        temp_derivation3 = Tex("x", "-y", "=\\frac{c^2-b^2}{a}").scale(0.6).next_to(
            derivation1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Transform(derivation3, temp_derivation3))
        temp_rect3 = get_rect(VGroup(derivation3[1], derivation4[1]), buff=0.1, color=RED)
        self.play(ShowCreation(temp_rect3), FadeOut(temp_rect2))
        arrow3 = add_right_arrow(VGroup(derivation3, derivation4))
        derivation5 = Tex("x", "=\\frac{c^2-b^2+a^2}{2a}").scale(0.6).next_to(arrow3, RIGHT, buff=0.15)
        self.wait()
        self.play(ShowCreation(arrow3))
        self.play(Write(derivation5))
        self.play(FadeOut(VGroup(
            temp_rect1, temp_rect3, brace1, derivation1, derivation2, derivation3, derivation4, arrow1, arrow2, arrow3
        )))
        self.wait()
        self.play(derivation5.move_to, derivation1.get_center() + UP * 0.5)
        derivation6 = Tex("h", "=\\sqrt{c^2-x^2}").scale(0.6).next_to(
            derivation5, DOWN, buff=0.4, aligned_edge=LEFT)
        arrow4 = add_right_arrow(derivation6)
        derivation7 = Tex("h", "=\\sqrt{c^2-(\\frac{c^2-b^2+a^2}{2a})^2}").scale(0.6).next_to(arrow4, RIGHT, buff=0.15)
        self.play(Write(derivation6))
        self.play(ShowCreation(arrow4))
        self.play(Write(derivation7))
        derivation8 = Tex("h=\\frac{\\sqrt{4a^2c^2-(c^2-b^2+a^2)^2}}{2a}").scale(0.6).next_to(
            derivation6, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(derivation8))
        self.play(FadeOut(VGroup(derivation6, arrow4, derivation7)),
                  derivation8.next_to, derivation5, RIGHT, {"buff": 1})
        derivation9 = Tex("S=\\frac{ah}{2}", "=\\frac{\\sqrt{4a^2c^2-(c^2-b^2+a^2)^2}}{4}").scale(0.6).next_to(
            derivation5, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(derivation9))
        derivation10 = Tex("=\\frac{\\sqrt{(2ac)^2-(c^2-b^2+a^2)^2}}{4}").scale(0.6).next_to(
            derivation9[1], DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(derivation10))
        derivation11 = Tex("=\\frac{\\sqrt{(2ac+c^2-b^2+a^2)(2ac-c^2+b^2-a^2)}}{4}").scale(0.6).next_to(
            derivation10, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(derivation11))
        derivation12 = Tex("=\\frac{\\sqrt{(2ac+c^2+a^2-b^2)(b^2-(c^2+a^2-2ac))}}{4}").scale(0.6).next_to(
            derivation11, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(derivation12))
        derivation13 = Tex("=\\frac{\\sqrt{((a+c)^2-b^2)(b^2-(a-c)^2)}}{4}").scale(0.6).next_to(
            derivation12, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(derivation13))
        derivation14 = Tex("=\\frac{\\sqrt{(a+c+b)(a+c-b)(b+a-c)(b-a+c)}}{4}").scale(0.6).next_to(
            derivation13, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(derivation14))
        self.wait(3)
        self.play(
            FadeOut(VGroup(derivation9[1], derivation10, derivation11, derivation12, derivation13)),
            derivation14.next_to, derivation9[0], RIGHT
        )

        desc1 = Tex("p-a=\\frac{a+b+c-2a}{2}", "=\\frac{b+c-a}{2}").scale(0.6).next_to(
            derivation9, DOWN, buff=0.4, aligned_edge=LEFT)
        desc2 = Tex("p-b=\\frac{a+b+c-2b}{2}", "=\\frac{a+c-b}{2}").scale(0.6).next_to(
            desc1, DOWN, buff=0.4, aligned_edge=LEFT)
        desc3 = Tex("p-c=\\frac{a+b+c-2c}{2}", "=\\frac{a+b-c}{2}").scale(0.6).next_to(
            desc2, DOWN, buff=0.4, aligned_edge=LEFT)
        brace2 = Brace(VGroup(derivation9, desc1, desc2, desc3), LEFT)
        self.play(TransformFromCopy(desc1[1], desc1[0]))
        self.play(Write(desc1[1]))
        self.play(Write(desc2))
        self.play(Write(desc3))
        self.play(ShowCreation(brace2))
        derivation16 = Tex("S=\\frac{\\sqrt{2p \\cdot 2(p-a) \\cdot 2(p-b) \\cdot 2(p-c)}}{4}",
                           "=\\sqrt{p(p-a)(p-b)(p-c)}").scale(0.6).next_to(
            desc3, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(derivation16[0]))
        self.play(Write(derivation16[1]))
        self.wait(4)
