import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.common.utils.math_utils import cal_dis, cal_triangle_angle
from yj.common.math.object_utils import get_rect


class Bisector1(Scene):
    def construct(self) -> None:
        title = Title('角平分线定理').scale(0.9)
        self.add(title)
        # 三角形ABC
        origin = ORIGIN + UP * 0.5
        pos_a = origin + UP * 2 * 4 / 5
        pos_b = origin + LEFT * 3 * 4 / 5
        pos_c = origin + RIGHT * 1 * 4 / 5

        triangle = Polygon(pos_a, pos_b, pos_c).set_stroke(width=4)
        point_a = Tex('A').next_to(pos_a, UP, buff=0.1).scale(0.8)
        point_b = Tex('B').next_to(pos_b, LEFT, buff=0.1).scale(0.8)
        point_c = Tex('C').next_to(pos_c, RIGHT, buff=0.1).scale(0.8)

        self.play(ShowCreation(triangle), Write(point_a), Write(point_b), Write(point_c))

        dis_ab = cal_dis(pos_a, pos_b)
        dis_ac = cal_dis(pos_a, pos_c)
        dis_bc = cal_dis(pos_c, pos_b)

        dis_bd = dis_bc * dis_ab / (dis_ab + dis_ac)
        pos_d = pos_b + RIGHT * dis_bd

        point_d = Tex('D').next_to(pos_d, DOWN, buff=0.1).scale(0.8)
        mid_line = Line(pos_a, pos_d, stroke_width=4)
        self.play(ShowCreation(mid_line))

        # formula = Tex("AB^2+AC^2=2(AD^2+BD^2)").scale(0.8).next_to(mid_line, DOWN, buff=1).shift(LEFT * 0.6)
        self.play(Write(point_d))
        # self.play(Write(formula))

        angle_bac = cal_triangle_angle(pos_b, pos_a, pos_c)
        angle_ac = math.atan2(pos_a[1] - pos_c[1], pos_c[0] - pos_a[0])
        print(angle_ac, angle_bac)
        arc1 = Sector(
            angle=angle_bac / 2,
            start_angle=(-angle_ac - angle_bac),
            fill_color=YELLOW, fill_opacity=0.5,
            arc_center=pos_a
        )
        theta1 = Tex('\\theta').scale(0.8).next_to(arc1, OUT).shift(DOWN * 0.3 + LEFT * 0.1)
        self.play(
            ShowCreation(arc1),
            Write(theta1)
        )

        arc2 = Sector(
            angle=angle_bac / 2,
            start_angle=(-angle_ac - angle_bac / 2),
            fill_color=YELLOW, fill_opacity=0.5,
            arc_center=pos_a
        )
        theta2 = Tex('\\theta').scale(0.8).next_to(arc2, OUT).shift(DOWN * 0.3)
        self.play(
            ShowCreation(arc2),
            Write(theta2)
        )

        # ∠bad ∠dac
        desc1 = Tex('\\angle BAD=\\angle DAC').scale(0.8).next_to(mid_line, DOWN, buff=1.5).shift(LEFT * 2.5)
        self.play(Write(desc1))
        arrow = Line(desc1.get_right() + RIGHT * 0.2, desc1.get_right() + RIGHT)
        arrow.add_tip(width=0.16, length=0.16)
        self.play(ShowCreation(arrow))
        # AB/AC=BD/DC
        desc2 = Tex('\\frac{AB}{AC}=\\frac{BD}{DC}').scale(0.8).next_to(arrow, RIGHT, buff=0.2)
        self.play(Write(desc2))

        self.wait()
        self.play(FadeOut(VGroup(desc1, arrow, desc2)))

        triangle_group = VGroup(triangle, point_a, point_b, point_c, point_d, mid_line, arc1, arc2, theta1, theta2)

        left_offset = 3 * LEFT
        pos_a += left_offset
        pos_b += left_offset
        pos_c += left_offset
        pos_d += left_offset
        self.play(triangle_group.shift, left_offset)

        dis_ad = cal_dis(pos_a, pos_d)
        dis_dc = cal_dis(pos_d, pos_c)
        dis_de = dis_bd * dis_ad / dis_dc
        pos_e = Line(pos_a, pos_d).get_unit_vector() * dis_de + pos_d

        dash_de = DashedLine(pos_d, pos_e).set_stroke(width=4)
        dash_be = DashedLine(pos_b, pos_e).set_stroke(width=4)
        self.play(
            ShowCreation(dash_de),
            ShowCreation(dash_be)
        )
        self.play(Write(Tex('E').next_to(pos_e, DOWN, buff=0.1).scale(0.8)))

        arc3 = Sector(
            angle=angle_bac / 2,
            start_angle=(PI - angle_ac - angle_bac / 2),
            fill_color=YELLOW, fill_opacity=0.5,
            arc_center=pos_e
        )
        theta3 = Tex('\\theta').scale(0.8).next_to(arc3, OUT).shift(UP * 0.5)
        self.play(ShowCreation(arc3), Write(theta3))

        # BE平行于AC
        desc3 = Tex('BE\\parallel AC').scale(0.8).next_to(pos_c, RIGHT, buff=3).shift(UP)
        self.play(Write(desc3))
        # ∠bed ∠dac ∠bad theta
        desc4 = Tex('\\angle BED=\\angle DAC=\\angle BAD=\\theta').scale(0.8).next_to(desc3, DOWN, buff=0.5)
        self.wait()
        self.play(Write(desc4))
        desc5 = Tex('AB=BE').scale(0.8).next_to(desc4, DOWN, buff=0.5, aligned_edge=LEFT)
        self.wait()
        self.play(Write(desc5))

        triangle_bde = Polygon(pos_b, pos_d, pos_e).set_stroke(width=4).set_fill(color=BLUE_A, opacity=0.5)
        triangle_cda = Polygon(pos_c, pos_d, pos_a).set_stroke(width=4).set_fill(color=BLUE_A, opacity=0.5)
        self.play(
            ShowCreation(triangle_bde),
            ShowCreation(triangle_cda)
        )
        # 三角形bde和三角形cda相似
        desc6 = Tex('\\triangle BDE\\sim\\triangle CDA').scale(0.8).next_to(desc5, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(desc6))
        # 所以ab/ac = be/ac=bd/dc
        desc7 = Tex('\\frac{AB}{AC}', '=\\frac{BE}{AC}=', '\\frac{BD}{DC}').scale(0.8).next_to(
            desc6, DOWN, buff=0.5, aligned_edge=LEFT)
        self.wait()
        self.play(Write(desc7))
        self.play(ShowCreation(get_rect(desc7[0], color=GREEN)))
        self.play(ShowCreation(get_rect(desc7[2], color=GREEN)))
        self.wait(5)
