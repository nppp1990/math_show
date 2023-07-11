import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.math_show.common.utils.math_utils import draw_arc, cal_dis, cal_triangle_angle
from yj.math_show.common.math.object_utils import add_right_arrow, get_rect


class Ptolemy(Scene):
    def construct(self) -> None:
        title = Title('托勒密定理').scale(0.9)
        self.add(title)
        circle = Circle(radius=1.5).shift(UP * 0.5)
        self.play(ShowCreation(circle))
        pos_a = circle.point_from_proportion(0.1)
        pos_b = circle.point_from_proportion(0.4)
        pos_c = circle.point_from_proportion(0.7)
        pos_d = circle.point_from_proportion(0.9)
        polygon = Polygon(pos_a, pos_b, pos_c, pos_d)
        text_a = Tex('A').scale(0.6).next_to(pos_a, UP, buff=0.1)
        text_b = Tex('B').scale(0.6).next_to(pos_b, LEFT, buff=0.1)
        text_c = Tex('C').scale(0.6).next_to(pos_c, DOWN, buff=0.1)
        text_d = Tex('D').scale(0.6).next_to(pos_d, RIGHT, buff=0.1)
        line_ac = Line(pos_a, pos_c)
        line_bd = Line(pos_b, pos_d)
        self.play(ShowCreation(polygon), ShowCreation(VGroup(text_a, text_b, text_c, text_d, line_ac, line_bd)))

        formula = Tex('AC\\cdot BD=AB\\cdot CD+BC\\cdot AD').scale(0.7).next_to(circle, DOWN, buff=1.5)
        self.play(Write(formula))
        bottom_desc = Text("圆内接凸四边形两对对边乘积的和始终等于两条对角线的乘积",
                           t2c={"内接凸四边形": BLUE, "两对对边乘积": YELLOW, "对角线": YELLOW}).scale(0.7).next_to(
            formula, DOWN, buff=0.5)
        self.play(Write(bottom_desc))

        def update_points1(mob, alpha):
            pos1 = circle.point_from_proportion(0.1 + 0.1 * alpha)
            pos2 = circle.point_from_proportion(0.4 - 0.1 * alpha)
            pos3 = circle.point_from_proportion(0.7 - 0.2 * alpha)
            pos4 = circle.point_from_proportion(0.9 - 0.1 * alpha)
            mob[0].become(Polygon(pos1, pos2, pos3, pos4))
            mob[1].next_to(pos1, UP, buff=0.1)
            mob[2].next_to(pos2, LEFT, buff=0.1)
            mob[3].next_to(pos3, DOWN, buff=0.1)
            mob[4].next_to(pos4, RIGHT, buff=0.1)
            mob[5].become(Line(pos1, pos3))
            mob[6].become(Line(pos2, pos4))

        self.play(UpdateFromAlphaFunc(
            VGroup(polygon, text_a, text_b, text_c, text_d, line_ac, line_bd), update_points1, run_time=1))

        def update_points2(mob, alpha):
            pos1 = circle.point_from_proportion(0.2 - 0.15 * alpha)
            pos2 = circle.point_from_proportion(0.3 + 0.15 * alpha)
            pos3 = circle.point_from_proportion(0.5 + 0.2 * alpha)
            pos4 = circle.point_from_proportion(0.8 + 0.1 * alpha)
            mob[0].become(Polygon(pos1, pos2, pos3, pos4))
            mob[1].next_to(pos1, UP, buff=0.1)
            mob[2].next_to(pos2, LEFT, buff=0.1)
            mob[3].next_to(pos3, DOWN, buff=0.1)
            mob[4].next_to(pos4, RIGHT, buff=0.1)
            mob[5].become(Line(pos1, pos3))
            mob[6].become(Line(pos2, pos4))

        self.wait()
        self.play(UpdateFromAlphaFunc(
            VGroup(polygon, text_a, text_b, text_c, text_d, line_ac, line_bd), update_points2, run_time=1))
        self.wait(2)
        self.play(
            FadeOut(VGroup(bottom_desc)),
            VGroup(polygon, text_a, text_b, text_c, text_d, line_ac, line_bd, circle).animate.shift(RIGHT * 3),
            formula.animate.next_to(title, DOWN, buff=1.5, aligned_edge=LEFT).shift(LEFT * 1).scale(0.8),
        )

        pos_a = polygon.get_vertices()[0]
        pos_b = polygon.get_vertices()[1]
        pos_c = polygon.get_vertices()[2]
        pos_d = polygon.get_vertices()[3]
        bottom_desc = VGroup(
            Text("过"), Tex("C"), Text("作", ), Tex("CP"), Text("和", ), Tex("BD"), Text("相交于", ),
            Tex("P", color=BLUE), Text("使"), Tex("\\angle BCP=\\angle ACD="), Tex("\\angle 1", color=BLUE),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        dis_bp = cal_dis(pos_a, pos_d) * cal_dis(pos_b, pos_c) / cal_dis(pos_a, pos_c)
        pos_p = pos_b + Line(pos_b, pos_d).get_unit_vector() * dis_bp
        dash_line_cp = DashedLine(pos_c, pos_p)
        self.play(Write(bottom_desc[0:7]), ShowCreation(dash_line_cp))
        text_p = Tex("P").scale(0.6).next_to(pos_p, UP, buff=0.1)
        self.play(Write(text_p), Write(bottom_desc[7]))

        angle_dca = draw_arc(pos_d, pos_c, pos_a, radius=0.5, color=YELLOW)
        text_dca = Tex("1", color=BLUE).scale(0.45).next_to(angle_dca, RIGHT, buff=0.1).shift(UP * 0.1)
        angle_bcp = draw_arc(pos_b, pos_c, pos_p, radius=0.5, color=YELLOW)
        text_bcp = Tex("1", color=BLUE).scale(0.45).next_to(angle_bcp, UP, buff=0.1)
        self.play(ShowCreation(angle_dca), Write(text_dca), ShowCreation(angle_bcp), Write(text_bcp),
                  Write(bottom_desc[8:]))
        self.wait()
        self.play(FadeOut(bottom_desc), run_time=0.5)
        bottom_desc = VGroup(
            Text("由圆周角定理可得", t2c={"圆周角定理": YELLOW}),
            Tex("\\angle CBP=\\angle CAD="),
            Tex("\\angle 2", color=BLUE),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        angle_cbp = draw_arc(pos_c, pos_b, pos_p, radius=0.5, color=YELLOW)
        text_cbp = Tex("2", color=BLUE).scale(0.45).next_to(angle_cbp, DOWN, buff=0.1).shift(RIGHT * 0.2)
        angle_cad = draw_arc(pos_c, pos_a, pos_d, radius=0.5, color=YELLOW)
        text_cad = Tex("2", color=BLUE).scale(0.45).next_to(angle_cad, DOWN, buff=0.1).shift(LEFT * 0.1)
        self.play(Write(bottom_desc[0]))
        self.play(ShowCreation(angle_cbp), Write(text_cbp), ShowCreation(angle_cad), Write(text_cad),
                  Write(bottom_desc[1:]))
        self.wait()
        triangle_bcp = Polygon(pos_b, pos_c, pos_p).set_fill(color=BLUE, opacity=0.3)
        self.play(ShowCreation(triangle_bcp))
        self.play(FadeOut(bottom_desc), run_time=0.5)
        bottom_desc = VGroup(
            Text("由于"),
            Tex("\\angle BCP=\\angle ACD=\\angle 1"),
            Text(" "),
            Tex("\\angle CBP=\\angle CAD=\\angle 2"),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(Write(bottom_desc),
                  triangle_bcp.animate.rotate(-cal_triangle_angle(pos_p, pos_c, pos_d), about_point=pos_c))
        self.wait()
        self.play(FadeOut(triangle_bcp), run_time=0.5)
        triangle_bcp = Polygon(pos_b, pos_c, pos_p).set_fill(color=BLUE, opacity=0.3)
        triangle_acd = Polygon(pos_a, pos_c, pos_d).set_fill(color=BLUE, opacity=0.3)
        desc1 = Tex("\\triangle BCP\\cong\\triangle ACD").scale(0.56).next_to(
            formula, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT)
        self.play(Write(desc1), ShowCreation(triangle_bcp), ShowCreation(triangle_acd))
        arrow1 = add_right_arrow(desc1, 0.4)
        desc2 = Tex("\\frac{AC}{BC}=\\frac{AD}{BP}").scale(0.56).next_to(arrow1, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow1))
        self.play(Write(desc2))
        arrow2 = add_right_arrow(desc2, 0.4)
        desc3 = Tex("BC \\cdot AD", "=", "AC \\cdot BP").scale(0.56).next_to(arrow2, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow2))
        self.play(Write(desc3))
        self.wait()
        self.play(FadeOut(bottom_desc), FadeOut(triangle_bcp), FadeOut(triangle_acd))
        bottom_desc = VGroup(
            Text("同理可得"),
            Tex("\\angle PCD = \\angle BCA"),
            Text(" "),
            Tex("\\angle PDC = \\angle BAC"),
            Tex("\\rightarrow \\triangle PCD\\cong\\triangle BCA"),
        ).scale(0.7).arrange(RIGHT).move_to(bottom_desc)
        triangle_pcd = Polygon(pos_p, pos_c, pos_d).set_color(BLUE)
        triangle_bca = Polygon(pos_b, pos_c, pos_a).set_color(YELLOW)
        self.play(Write(bottom_desc[0:4]), ShowCreation(triangle_pcd), ShowCreation(triangle_bca))

        desc4 = Tex("\\triangle PCD\\cong\\triangle BCA").scale(0.56).next_to(
            desc1, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(Write(desc4), Write(bottom_desc[4]))
        arrow3 = add_right_arrow(desc4, 0.4)
        desc5 = Tex("\\frac{AC}{CD}=\\frac{AB}{PD}").scale(0.56).next_to(arrow3, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow3))
        self.play(Write(desc5))
        arrow4 = add_right_arrow(desc5, 0.4)
        desc6 = Tex("AB \\cdot CD", "= AC", "\\cdot PD").scale(0.56).next_to(arrow4, RIGHT, buff=0.2)
        self.play(ShowCreation(arrow4))
        self.play(Write(desc6))
        self.wait()
        rect = get_rect(VGroup(desc3, desc6), buff=0.1, color=RED)
        self.play(ShowCreation(rect))
        self.wait()
        self.play(FadeOut(VGroup(triangle_pcd, triangle_bca, bottom_desc)), run_time=0.5)
        bottom_desc = Text("两式相加可得").scale(0.7).move_to(bottom_desc)
        desc7 = Tex("AB\\cdot CD",
                    "+",
                    "BC\\cdot AD",
                    "=",
                    "AC \\cdot BP",
                    "+",
                    " AC \\cdot PD",
                    "=AC \\cdot (BP+PD)=AC\\cdot BD"
                    ).scale(0.56).next_to(desc4, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(Write(bottom_desc), run_time=0.5)
        self.play(
            TransformFromCopy(desc3[0], desc7[2]),
            TransformFromCopy(desc6[0], desc7[0]),
            Write(desc7[1])
        )
        self.play(Write(desc7[3], run_time=0.2))
        self.play(
            TransformFromCopy(desc3[2], desc7[4]),
            TransformFromCopy(desc6[2], desc7[6]),
            Write(desc7[5])
        )
        self.play(Write(desc7[7:]))
        self.wait(5)


def create_mob(pos_offset):
    circle = Circle(radius=1.5).shift(UP * 0.5)
    pos_a = circle.point_from_proportion(0.1)
    pos_b = circle.point_from_proportion(0.35)
    pos_c = circle.point_from_proportion(0.6) + pos_offset
    pos_d = circle.point_from_proportion(0.95)
    polygon = Polygon(pos_a, pos_b, pos_c, pos_d)
    text_a = Tex('A').scale(0.6).next_to(pos_a, UP, buff=0.1)
    text_b = Tex('B').scale(0.6).next_to(pos_b, LEFT, buff=0.1)
    text_c = Tex('C').scale(0.6).next_to(pos_c, DOWN, buff=0.1)
    text_d = Tex('D').scale(0.6).next_to(pos_d, RIGHT, buff=0.1)
    line_ac = Line(pos_a, pos_c)
    line_bd = Line(pos_b, pos_d)
    return VGroup(circle, polygon, text_a, text_b, text_c, text_d, line_ac, line_bd)


class Ptolemy2(Scene):
    def construct(self) -> None:
        title = Title('托勒密不等式').scale(0.9)
        self.add(title)
        mob = create_mob(LEFT)
        self.play(ShowCreation(mob[1]))
        self.play(ShowCreation(mob[0]))
        self.play(Write(mob[2:]))
