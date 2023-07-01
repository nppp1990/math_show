import math
import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.common.math.object_utils import get_right_angle, add_right_arrow, get_rect
from yj.common.utils.math_utils import cal_triangle_angle, cal_dis, get_vertical_point

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


class Cosine2(Scene):
    def construct(self) -> None:
        title = Title("余弦定理-欧几里得证法").scale(0.9)
        self.add(title)
        # 三角形ABC
        origin = ORIGIN
        pos_c = origin + UP * 2
        pos_a = origin + LEFT * 2
        pos_b = origin + RIGHT * 1
        triangle = Polygon(pos_a, pos_b, pos_c).set_stroke(width=4)
        point_a = Tex("A").next_to(pos_a, LEFT, buff=0.1).scale(0.8)
        point_b = Tex("B").next_to(pos_b, RIGHT, buff=0.1).scale(0.8)
        point_c = Tex("C").next_to(pos_c, UP, buff=0.1).scale(0.8)
        self.play(ShowCreation(triangle))
        self.play(Write(point_a), Write(point_b), Write(point_c))

        angle_c = cal_triangle_angle(pos_a, pos_c, pos_b)
        angle_b = cal_triangle_angle(pos_c, pos_b, pos_a)
        arc_c = Arc(
            angle=angle_c,
            start_angle=2 * PI - angle_b - angle_c,
            arc_center=pos_c,
            radius=0.5,
            stroke_width=4,
        )
        alpha_c = Tex("\\alpha").scale(0.8).set_color(YELLOW).next_to(arc_c, DOWN, buff=0.1)
        self.play(ShowCreation(arc_c))
        self.play(Write(alpha_c))
        text_c = Tex("c").set_color(GREEN).next_to((pos_a + pos_b) / 2, DOWN, buff=0.1)
        text_b = Tex("b").set_color(GREEN).next_to((pos_a + pos_c) / 2, LEFT, buff=0.1).shift(UP * 0.1)
        text_a = Tex("a").set_color(GREEN).next_to((pos_b + pos_c) / 2, RIGHT, buff=0.1)
        self.play(ShowCreation(text_a), ShowCreation(text_b), ShowCreation(text_c))

        formula1 = Tex("c^2=a^2+b^2-2ab\\cos\\alpha").scale(0.8).next_to(triangle, DOWN, buff=1)
        self.play(Write(formula1))
        self.wait(2)

        triangle_group = VGroup(triangle, point_a, point_b, point_c, arc_c, alpha_c, text_a, text_b, text_c)
        self.play(
            FadeOut(formula1),
            triangle_group.scale, 0.7,
            triangle_group.shift, RIGHT * 2 + DOWN * 1.2,
        )

        pos_a = triangle_group[0].get_vertices()[0]
        pos_b = triangle_group[0].get_vertices()[1]
        pos_c = triangle_group[0].get_vertices()[2]
        dis_b = cal_dis(pos_a, pos_c)

        pos_d = get_vertical_point(pos_c, pos_a, False, dis_b)
        pos_e = get_vertical_point(pos_a, pos_c, True, dis_b)
        c_square = Polygon(
            pos_a, pos_c, pos_d, pos_e,
        ).set_stroke(width=4).set_color(RED)
        self.play(
            ShowCreation(c_square),
            Write(Tex('D').next_to(pos_d, UP, buff=0.1).scale(0.56)),
            Write(Tex('E').next_to(pos_e, LEFT, buff=0.1).scale(0.56)),
        )

        dis_a = cal_dis(pos_b, pos_c)
        pos_f = get_vertical_point(pos_c, pos_b, True, dis_a)
        pos_g = get_vertical_point(pos_b, pos_c, False, dis_a)
        b_square = Polygon(
            pos_b, pos_c, pos_f, pos_g,
        ).set_stroke(width=4).set_color(GREEN)
        self.play(
            ShowCreation(b_square),
            Write(Tex('F').next_to(pos_f, UP, buff=0.1).scale(0.56)),
            Write(Tex('G').next_to(pos_g, RIGHT, buff=0.1).scale(0.56)),
        )

        dis_c = cal_dis(pos_a, pos_b)
        pos_h = get_vertical_point(pos_b, pos_a, True, dis_c)
        pos_i = get_vertical_point(pos_a, pos_b, False, dis_c)
        a_square = Polygon(
            pos_a, pos_b, pos_h, pos_i,
        ).set_stroke(width=4).set_color(BLUE)
        self.play(
            ShowCreation(a_square),
            Write(Tex('H').next_to(pos_h, RIGHT, buff=0.1).scale(0.56)),
            Write(Tex('I').next_to(pos_i, LEFT, buff=0.1).scale(0.56)),
        )

        pos_x = pos_f + Line(pos_f, pos_g).get_unit_vector() * dis_b * math.cos(angle_c)
        pos_y = pos_d + Line(pos_d, pos_e).get_unit_vector() * dis_c * math.cos(angle_c)
        pos_z = pos_h + Line(pos_h, pos_i).get_unit_vector() * dis_a * math.cos(angle_b)

        self.wait()
        self.play(ShowCreation(DashedLine(pos_a, pos_x, stroke_width=4)))
        self.play(Write(Tex('X').next_to(pos_x, RIGHT, buff=0.01).scale(0.56), run_time=0.5))
        self.play(ShowCreation(DashedLine(pos_b, pos_y, stroke_width=4)))
        self.play(Write(Tex('Y').next_to(pos_y, LEFT, buff=0.01).scale(0.56), run_time=0.5))
        self.play(ShowCreation(DashedLine(pos_c, pos_z, stroke_width=4)))
        self.play(Write(Tex('Z').next_to(pos_z, DOWN, buff=0.01).scale(0.56), run_time=0.5))
        self.wait()

        area1 = Polygon(pos_a, pos_i, pos_z).set_fill(color=YELLOW, opacity=1)
        self.play(ShowCreation(area1))
        self.wait(0.5)
        self.play(Transform(
            area1, Polygon(pos_i, pos_a, pos_c).set_fill(color=YELLOW, opacity=1)
        ))
        self.wait(0.5)
        self.play(Transform(
            area1, Polygon(pos_b, pos_a, pos_e).set_fill(color=YELLOW, opacity=1)
        ))
        temp1 = pos_y + Line(pos_y, pos_b).get_unit_vector() * dis_b
        temp2 = pos_x + Line(pos_x, pos_a).get_unit_vector() * dis_a
        temp3 = pos_z + Line(pos_z, pos_c).get_unit_vector() * dis_c
        self.wait(0.5)
        self.play(Transform(
            area1,
            Polygon(pos_e, pos_a, temp1).set_fill(color=YELLOW, opacity=1)
        ))
        self.wait()
        self.remove(area1)
        self.play(
            ShowCreation(Polygon(pos_a, pos_e, pos_y, temp1).set_fill(color=YELLOW, opacity=1)),
            ShowCreation(Polygon(pos_a, pos_i, pos_z, temp3).set_fill(color=YELLOW, opacity=1)),
        )

        self.wait()
        area2 = Polygon(pos_b, pos_h, pos_z).set_fill(color=PURPLE, opacity=1)
        self.play(ShowCreation(area2))
        self.wait(0.5)
        self.play(Transform(
            area2, Polygon(pos_h, pos_b, pos_c).set_fill(color=PURPLE, opacity=1)
        ))
        self.wait(0.5)
        self.play(Transform(
            area2, Polygon(pos_a, pos_b, pos_g).set_fill(color=PURPLE, opacity=1)
        ))
        self.wait(0.5)
        self.play(Transform(
            area2,
            Polygon(pos_b, pos_g, temp2).set_fill(color=PURPLE, opacity=1)
        ))
        self.wait()
        self.remove(area2)
        self.play(
            ShowCreation(Polygon(pos_z, pos_h, pos_b, temp3).set_fill(color=PURPLE, opacity=1)),
            ShowCreation(Polygon(pos_b, pos_g, pos_x, temp2).set_fill(color=PURPLE, opacity=1)),
        )

        line1 = Line(pos_c, temp1, color=BLACK).set_stroke(width=6)
        # bc * cosalpha
        desc1 = Tex('BC\\cos\\alpha=CP').scale(0.7).next_to(title, DOWN, buff=1).shift(LEFT * 4)
        self.play(
            Write(desc1),
            Write(Tex("P", color=BLACK).scale(0.56).move_to(temp1 + LEFT * 0.3)),
            Indicate(line1),
        )
        desc2 = Tex('AC\\cdot BC\\cos\\alpha=CD\\cdot CP').scale(0.7).next_to(desc1, DOWN, buff=0.5, aligned_edge=RIGHT)
        line2 = Line(pos_c, pos_d, color=BLACK).set_stroke(width=6)
        self.play(
            Write(desc2),
            Indicate(line2)
        )
        self.wait()
        poly1 = Polygon(pos_c, temp1, pos_y, pos_d).set_fill(color=BLACK, opacity=1)
        self.play(
            ShowCreation(poly1),
        )

        self.wait()
        line3 = Line(pos_c, temp2, color=BLACK).set_stroke(width=6)
        desc3 = Tex('AC\\cos\\alpha=CQ').scale(0.7).next_to(desc2, DOWN, buff=0.5, aligned_edge=RIGHT)
        self.play(
            Write(desc3),
            Write(Tex("Q", color=BLACK).scale(0.56).move_to(temp2 + RIGHT * 0.3)),
            Indicate(line3),
        )
        self.wait()
        poly2 = Polygon(pos_c, temp2, pos_x, pos_f).set_fill(color=BLACK, opacity=1)
        self.play(
            ShowCreation(poly2),
        )

        self.wait()

        desc4 = Tex("S_{\\square CPYD}=S_{\\square CQXF}=AC\\cdot BC\\cos\\alpha").scale(0.7).next_to(
            desc3, DOWN, buff=0.5, aligned_edge=RIGHT).shift(RIGHT * 1.5)
        self.play(Write(desc4))

        self.wait()

        # 所以c^2=a^2+b^2-2ab\\cos\\alpha
        desc = Tex("c^2", "=", "a^2", "+", "b^2", "-", "2ab\\cos\\alpha").scale(0.7).next_to(
            desc4, DOWN, buff=0.5, aligned_edge=RIGHT
        ).shift(LEFT * 1.5)
        show_c = Tex("c").scale(0.6).next_to((pos_a + pos_i) / 2, LEFT, buff=0.1)
        self.play(ShowCreation(show_c, run_time=0.5))
        self.wait(0.5)
        self.play(Transform(show_c, desc[0], run_time=2))
        self.play(Write(desc[1], run_time=0.5))

        show_a = Tex("a").scale(0.6).next_to((pos_b + pos_g) / 2, DOWN, buff=0.1)
        self.play(ShowCreation(show_a, run_time=0.5))
        self.wait(0.5)
        self.play(Transform(show_a, desc[2], run_time=2))
        self.play(Write(desc[3], run_time=0.3))

        show_b = Tex("b").scale(0.6).next_to((pos_a + pos_e) / 2, LEFT, buff=0.1)
        self.play(ShowCreation(show_b, run_time=0.5))
        self.wait(0.5)
        self.play(Transform(show_b, desc[4], run_time=2))
        self.play(Write(desc[5], run_time=0.3))

        self.play(TransformFromCopy(
            VGroup(poly1, poly2), desc[6], run_time=2
        ))

        self.wait(5)
