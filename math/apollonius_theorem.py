import math

from manimlib import *


def cal_triangle_angle(point1, point2, point3):
    vector1 = point1 - point2
    vector2 = point3 - point2
    return np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))


def cal_dis(point1, point2):
    return np.linalg.norm(point1 - point2)


# def draw_arc(point1, point2, point3, start_angle=0, radius=0.3):
#     angle = cal_triangle_angle(point1, point2, point3)
#     arc = Sector(outer_radius=radius, angle=angle, start_angle=start_angle,
#                  fill_color=YELLOW, fill_opacity=0.5,
#                  arc_center=point2)
#     return arc


def init_triangle(self):
    # 三角形ABC
    pos_a = ORIGIN + UP * 2
    pos_b = ORIGIN + LEFT * 3
    pos_c = ORIGIN + RIGHT * 1
    pos_d = (pos_b + pos_c) / 2

    triangle = Polygon(pos_a, pos_b, pos_c).set_stroke(width=4)
    point_a = Tex('A').next_to(pos_a, UP, buff=0.1).scale(0.8)
    point_b = Tex('B').next_to(pos_b, LEFT, buff=0.1).scale(0.8)
    point_c = Tex('C').next_to(pos_c, RIGHT, buff=0.1).scale(0.8)

    self.play(ShowCreation(triangle), Write(point_a), Write(point_b), Write(point_c))
    point_d = Tex('D').next_to(pos_d, DOWN, buff=0.1).scale(0.8)
    mid_line = Line(pos_a, pos_d, stroke_width=4)
    self.play(ShowCreation(mid_line))

    formula = Tex("AB^2+AC^2=2(AD^2+BD^2)").scale(0.8).next_to(mid_line, DOWN, buff=1).shift(LEFT * 0.6)
    self.play(Write(point_d))
    self.play(Write(formula))

    triangle_group = VGroup(triangle, point_a, point_b, point_c, point_d, mid_line)

    left_offset = LEFT * 2
    pos_a += left_offset
    pos_b += left_offset
    pos_c += left_offset
    pos_d += left_offset
    self.play(
        triangle_group.shift, LEFT * 2,
        formula.shift, LEFT * 2 + DOWN * 2,
    )
    return pos_a, pos_b, pos_c, pos_d, mid_line


class MidLine1(Scene):
    def construct(self):
        title = Title("中线定理-超简单").scale(0.9)
        self.add(title)
        pos_a, pos_b, pos_c, pos_d, mid_line = init_triangle(self)

        ab_length = cal_dis(pos_a, pos_b)
        ae_length = ab_length * math.cos(cal_triangle_angle(pos_b, pos_a, pos_d))
        pos_e = pos_a + mid_line.get_unit_vector() * ae_length
        dash_line_de = DashedLine(pos_d, pos_e, stroke_width=4)
        dash_line_be = DashedLine(pos_b, pos_e, stroke_width=4)
        self.play(ShowCreation(dash_line_de))
        self.play(ShowCreation(dash_line_be))

        # 画直角line1
        angle_line1 = Line(
            pos_e - mid_line.get_unit_vector() * 0.3,
            pos_e - mid_line.get_unit_vector() * 0.3 - dash_line_be.get_unit_vector() * 0.3,
        )
        # 画直角line2
        angle_line2 = Line(
            pos_e - mid_line.get_unit_vector() * 0.3 - dash_line_be.get_unit_vector() * 0.3,
            pos_e - dash_line_be.get_unit_vector() * 0.3,
        )
        self.play(ShowCreation(angle_line1, run_time=0.5))
        self.play(ShowCreation(angle_line2, run_time=0.5))

        point_e = Tex('E').set_color(BLUE_A).set_opacity(0.3).next_to(pos_e, DOWN, buff=0.1).scale(0.8)
        self.play(Write(point_e))

        ac_length = cal_dis(pos_a, pos_c)
        af_length = ac_length * math.cos(cal_triangle_angle(pos_d, pos_a, pos_c))
        pos_f = pos_a + mid_line.get_unit_vector() * af_length
        dash_line_cf = DashedLine(pos_c, pos_f, stroke_width=4)
        self.play(ShowCreation(dash_line_cf))
        # 画直角line3
        angle_line3 = Line(
            pos_f + mid_line.get_unit_vector() * 0.3,
            pos_f + mid_line.get_unit_vector() * 0.3 - dash_line_cf.get_unit_vector() * 0.3,
        )
        # 画直角line4
        angle_line4 = Line(
            pos_f + mid_line.get_unit_vector() * 0.3 - dash_line_cf.get_unit_vector() * 0.3,
            pos_f - dash_line_cf.get_unit_vector() * 0.3,
        )
        self.play(ShowCreation(angle_line3, run_time=0.5))
        self.play(ShowCreation(angle_line4, run_time=0.5))
        point_f = Tex('F').set_color(BLUE_A).set_opacity(0.3).next_to(pos_f, LEFT, buff=0.1).scale(0.8)
        self.play(Write(point_f))

        triangle_bde = Polygon(pos_b, pos_d, pos_e).set_stroke(width=4).set_fill(BLUE_A, opacity=0.3)
        triangle_cdf = Polygon(pos_c, pos_d, pos_f).set_stroke(width=4).set_fill(BLUE_A, opacity=0.3)
        self.play(
            ShowCreation(triangle_bde),
            ShowCreation(triangle_cdf),
        )

        desc1 = Text("△BDE与△CDF为全等三角形",
                     t2c={"△BDE": BLUE_A, "△CDF": BLUE_A, "全等三角形": BLUE}
                     )
        desc2 = Text("所以BE=CF=x，DE=DF=y", )
        desc3 = Tex("AB^2 = BE^2 + AE^2 = x^2 + (AD + y)^2")
        desc4 = Tex("AC^2 = CF^2 + AF^2 = x^2 + (AD - y)^2")

        desc_group = VGroup(
            desc1,
            desc2,
            desc3,
            desc4,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.7).next_to(title, DOWN, buff=0.5).shift(RIGHT * 3)
        desc5 = Tex("AB^2 + AC^2 = 2(AD^2 + x^2 + y^2) = 2(AD^2 + BD^2)").scale(0.7).next_to(desc_group,
                                                                                             DOWN * 2.5).shift(LEFT)

        self.play(Write(desc1))
        self.play(
            FadeOut(triangle_bde, run_time=0.5),
            FadeOut(triangle_cdf, run_time=0.5),
            Write(desc2),
        )

        text_x1 = Tex("x").set_color(YELLOW).scale(0.7).next_to(dash_line_be, OUT)
        text_x2 = Tex("x").set_color(YELLOW).scale(0.7).next_to(dash_line_cf, OUT)
        self.play(FadeIn(text_x1), FadeIn(text_x2))

        text_y1 = Tex("y").set_color(YELLOW).scale(0.7).next_to(dash_line_de, OUT)
        text_y2 = Tex("y").set_color(YELLOW).scale(0.7).next_to(Line(pos_d, pos_f), OUT)
        self.play(FadeIn(text_y1), FadeIn(text_y2))

        self.play(Write(desc3))
        self.play(Write(desc4))
        self.play(Write(desc5))
        self.wait(3)


class MidLine2(Scene):
    def construct(self):
        title = Title("中线定理-余弦定理证法").scale(0.9)
        self.add(title)

        pos_a, pos_b, pos_c, pos_d, mid_line = init_triangle(self)
        angle = cal_triangle_angle(pos_a, pos_d, pos_b)
        arc1 = Sector(outer_radius=0.3, angle=angle, start_angle=PI - angle,
                      fill_color=YELLOW, fill_opacity=1, arc_center=pos_d)
        angle_text1 = Text("x").set_color(BLUE).next_to(arc1, OUT, buff=0.1).scale(0.7).shift(LEFT * 0.1 + UP * 0.15)
        self.play(ShowCreation(arc1))
        self.play(Write(angle_text1))
        # α,β,θ
        text1 = Tex("AB^2 = AD^2 + BD^2 - 2AD·BD · COS x").scale(0.7).next_to(title, DOWN, buff=1).shift(RIGHT * 3)
        self.play(Write(text1))

        arc2 = Sector(outer_radius=0.3, angle=PI - angle, start_angle=0,
                      fill_color=BLUE, fill_opacity=1, arc_center=pos_d)
        angle_text2 = Text("y").set_color(YELLOW).next_to(arc2, OUT, buff=0.1).scale(0.7).shift(RIGHT * 0.15 + UP * 0.1)
        self.play(ShowCreation(arc2))
        self.play(Write(angle_text2))

        text2 = Tex("AC^2 = AD^2 + DC^2 - 2AD·CD · COS y").scale(0.7).next_to(text1, DOWN, buff=0.5)
        self.play(Write(text2))

        text3 = Tex("x + y = 180°").scale(0.7).next_to(text2, DOWN, buff=0.5, aligned_edge=LEFT)

        arrow1 = Line(text3.get_right() + RIGHT * 0.2, text3.get_right() + RIGHT)
        arrow1.add_tip(width=0.16, length=0.16)
        self.play(Write(text3))
        self.play(ShowCreation(arrow1))

        text4 = Tex("COS x = -COS y").scale(0.7).next_to(arrow1, RIGHT, buff=0.2)
        self.play(Write(text4))

        text5 = Tex("BD = CD").scale(0.7).next_to(text3, DOWN, buff=0.5, aligned_edge=LEFT).shift(LEFT)
        arrow2 = Line(text5.get_right() + RIGHT * 0.2, text5.get_right() + RIGHT)
        arrow2.add_tip(width=0.16, length=0.16)
        self.play(Write(text5))
        self.play(ShowCreation(arrow2))
        text6 = Tex("AB^2 + AC^2 = 2(AD^2 + BD^2)").scale(0.7).next_to(arrow2, RIGHT, buff=0.2)
        self.play(Write(text6))
        self.wait(3)
