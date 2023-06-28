import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.common.math.object_utils import get_right_angle, add_right_arrow, get_rect
from yj.common.utils.math_utils import cal_triangle_angle

from manimlib import *


class Cosine1(Scene):
    def construct(self) -> None:
        title = Title("余弦定理").scale(0.9)
        self.add(title)
        # 三角形ABC
        origin = ORIGIN
        pos_b = origin + UP * 2
        pos_a = origin + LEFT * 3
        pos_c = origin + RIGHT * 1
        triangle = Polygon(pos_a, pos_b, pos_c).set_stroke(width=4)
        point_a = Tex("A").next_to(pos_a, LEFT, buff=0.1).scale(0.8)
        point_b = Tex("B").next_to(pos_b, UP, buff=0.1).scale(0.8)
        point_c = Tex("C").next_to(pos_c, RIGHT, buff=0.1).scale(0.8)
        self.play(ShowCreation(triangle))
        self.play(Write(point_a), Write(point_b), Write(point_c))

        angle_c = cal_triangle_angle(pos_a, pos_c, pos_b)
        arc_c = Arc(
            angle=angle_c,
            start_angle=PI - angle_c,
            arc_center=pos_c,
            radius=0.5,
            stroke_width=4,
        )
        alpha_c = Tex("\\alpha").scale(0.8).set_color(YELLOW).next_to(arc_c, OUT).shift(LEFT * 0.2 + UP * 0.1)
        self.play(ShowCreation(arc_c))
        self.play(Write(alpha_c))
        text_c = Tex("c").set_color(GREEN).next_to((pos_a + pos_b) / 2, LEFT, buff=0.1).shift(UP * 0.1)
        text_b = Tex("b").set_color(GREEN).next_to((pos_a + pos_c) / 2, DOWN, buff=0.1)
        text_a = Tex("a").set_color(GREEN).next_to((pos_b + pos_c) / 2, RIGHT, buff=0.1)
        self.play(ShowCreation(text_a), ShowCreation(text_b), ShowCreation(text_c))

        formula1 = Tex("c^2=a^2+b^2-2ab\\cos\\alpha").scale(0.8).next_to(triangle, DOWN, buff=1)
        self.play(Write(formula1))

        angle_a = cal_triangle_angle(pos_b, pos_a, pos_c)
        arc_a = Arc(
            angle=angle_a,
            start_angle=0,
            arc_center=pos_a,
            radius=0.5,
            stroke_width=4,
        )
        beta_a = Tex("\\beta").scale(0.8).set_color(YELLOW).next_to(arc_a, RIGHT).shift(LEFT * 0.2 + UP * 0.1)
        self.play(ShowCreation(arc_a), Write(beta_a))
        formula2 = Tex("a^2=b^2+c^2-2bc\\cos\\beta").scale(0.8).next_to(formula1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(formula2))

        angle_b = cal_triangle_angle(pos_c, pos_b, pos_a)
        arc_b = Arc(
            angle=angle_b,
            start_angle=2 * PI - angle_b - angle_c,
            arc_center=pos_b,
            radius=0.5,
            stroke_width=4,
        )
        gamma_b = Tex("\\gamma").scale(0.8).set_color(YELLOW).next_to(arc_b, DOWN, buff=0.1)
        self.play(ShowCreation(arc_b), Write(gamma_b))
        formula3 = Tex("b^2=a^2+c^2-2ac\\cos\\gamma").scale(0.8).next_to(formula2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(formula3))

        self.wait()
        self.play(
            FadeOut(VGroup(
                arc_a, arc_b, beta_a, gamma_b,
                formula2, formula3
            )),
        )
        self.wait()
        left_offset = LEFT * 3
        pos_a += left_offset
        pos_b += left_offset
        pos_c += left_offset
        self.play(
            VGroup(
                triangle, point_a, point_b, point_c, text_a, text_b, text_c,
                alpha_c, arc_c, formula1
            ).shift, left_offset
        )

        pos_d = pos_b + DOWN * (pos_b[1] - pos_c[1])
        point_d = Tex("D").scale(0.8).next_to(pos_d, DOWN, buff=0.1)
        self.play(ShowCreation(DashedLine(pos_b, pos_d, stroke_width=4)))
        # 画直角符号
        right_angle = get_right_angle(pos_d, LEFT * 0.25, UP * 0.25)
        self.play(ShowCreation(right_angle))
        self.play(Write(point_d))

        # BD=x AD=y DC=z
        desc1 = Tex("BD=x, AD=y, DC=z").scale(0.7).next_to(title, DOWN, buff=1, aligned_edge=RIGHT).shift(LEFT * 2)
        self.play(Write(desc1))
        text_x = Tex("x").scale(0.7).set_color(RED).next_to((pos_b + pos_d) / 2, OUT, buff=0.1)
        text_y = Tex("y").scale(0.7).set_color(RED).next_to((pos_a + pos_d) / 2, OUT, buff=0.1)
        text_z = Tex("z").scale(0.7).set_color(RED).next_to((pos_c + pos_d) / 2, OUT, buff=0.1)
        self.play(ShowCreation(text_x), ShowCreation(text_y), ShowCreation(text_z))

        desc2 = Tex("c^2=x^2+y^2").scale(0.7).next_to(desc1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc2))
        desc3 = Tex("b^2=(y+z)^2=y^2+z^2+2yz").scale(0.7).next_to(desc2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc3))
        desc4 = Tex("a^2=x^2+z^2").scale(0.7).next_to(desc3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc4))
        self.wait()
        desc5 = Tex("a^2+b^2=x^2+y^2+2z^2+2yz").scale(0.7).next_to(desc4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc5))
        desc6 = Tex("\\cos\\alpha=\\frac{z}{a}").scale(0.7).next_to(desc5, DOWN, buff=0.3, aligned_edge=LEFT)
        arrow = add_right_arrow(desc6)
        self.wait()
        self.play(Write(desc6))
        self.play(ShowCreation(arrow))
        # 2ab cos aloha = 2b dot a cos alpha=2b 乘 z
        desc7 = Tex("2ab\\cos\\alpha=2ba\\cos\\alpha=2bz").scale(0.7).next_to(arrow, RIGHT, buff=0.2)
        self.play(Write(desc7))
        desc8 = Tex("2ab\\cos\\alpha=2(y+z)z=2yz + 2z^2").scale(0.7).next_to(desc6, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(desc8))

        self.wait()
        self.play(ShowCreation(get_rect(desc2, buff=0.1, color=RED)))
        self.play(ShowCreation(get_rect(desc5, buff=0.1, color=RED)))
        self.play(ShowCreation(get_rect(desc8, buff=0.1, color=RED)))
        self.play(ShowCreation(get_rect(formula1, buff=0.1, color=GREEN)))
        self.wait(5)
