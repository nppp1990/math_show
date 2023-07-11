import math
import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.math_show.common.utils.math_utils import draw_arc, draw_polygon_line, get_lines_vertices, cal_triangle_angle, cal_dis
from yj.math_show.common.math.object_utils import add_right_arrow, get_rect, get_right_angle, get_right_angle_by_points

from manimlib import *


class InscribedAngle1(Scene):
    def construct(self) -> None:
        title = Title("圆周角定理").scale(0.9)
        self.add(title)

        # 画圆
        circle = Circle(radius=2, color=WHITE).set_stroke(width=4)
        self.play(ShowCreation(circle))
        # 画圆心
        pos_o = ORIGIN.copy()
        dot_o = Dot(pos_o, color=WHITE)
        text_o = Tex("O").next_to(dot_o, DOWN, buff=0.1).scale(0.8)
        self.play(ShowCreation(dot_o), Write(text_o))
        # 画圆上的点A、B
        pos_a = circle.point_from_proportion(0.65)
        pos_b = circle.point_from_proportion(0.85)

        # 圆弧AB
        angle_ab = (0.85 - 0.65) * TAU
        arc_ab = ArcBetweenPoints(pos_a, pos_b, angle=angle_ab).set_color(RED)
        self.play(ShowCreation(arc_ab))

        point_a = Dot(circle.point_from_proportion(0.65)).set_color(RED)
        point_b = Dot(circle.point_from_proportion(0.85)).set_color(RED)
        text_a = Tex("A").next_to(point_a, DOWN, buff=0.1).scale(0.8)
        text_b = Tex("B").next_to(point_b, DOWN, buff=0.1).scale(0.8)
        self.play(
            ShowCreation(point_a), ShowCreation(point_b),
            Write(text_a),
            Write(text_b)
        )

        point_x = Dot().move_to(pos_a).set_color(RED)
        text_x = Tex("X").next_to(point_x, DOWN, buff=0.1).scale(0.8)
        group_triangle = VGroup(point_x, Line(pos_a, pos_a), Line(pos_a, pos_b), text_x)

        def update_x(mob, alpha):
            # alpha: 0~1, 0.9~1,0~0.6
            alpha = alpha * 0.7
            x = 0.9 + alpha
            if x > 1:
                x -= 1
            pos = circle.point_from_proportion(x)
            mob[0].move_to(pos)
            mob[1].put_start_and_end_on(pos, pos_a)
            mob[2].put_start_and_end_on(pos, pos_b)
            mob[3].next_to(pos, DOWN, buff=0.1)

        self.wait(2)
        desc1 = VGroup(
            Text("弧"),
            Tex("AB"),
            Text("对应的圆周角"),
            Tex("\\angle AXB ="),
            Text("圆心角"),
            Tex("\\angle AOB"),
            Text("的一半"),
        ).arrange().scale(0.7).next_to(circle, DOWN, buff=0.4)

        line_oab = VGroup(Line(pos_o, pos_a), Line(pos_o, pos_b))
        self.play(
            UpdateFromAlphaFunc(group_triangle, update_x, run_time=4),
            ShowCreation(line_oab),
            Write(desc1)
        )
        cur_x = 0.6

        desc1_temp = Tex("\\angle AXB = \\frac{1}{2} \\angle AOB").scale(0.8).next_to(title, DOWN, buff=1).shift(
            LEFT * 5)
        self.play(Transform(desc1, desc1_temp))

        self.wait()
        left_offset = LEFT * 1.8
        pos_a += left_offset
        pos_b += left_offset
        pos_o += left_offset
        circle_group = VGroup(circle, point_a, point_b, text_a, text_b,
                              arc_ab, dot_o, text_o, group_triangle, line_oab)
        self.play(circle_group.shift, left_offset)

        self.wait()
        # o在dac的一边时
        sub_title = VGroup(
            Text("当O在"),
            Tex("\\angle AXB"),
            Text("的一边时")
        ).set_color(BLUE).arrange(RIGHT).scale(0.8).next_to(title, DOWN, buff=0.8, aligned_edge=RIGHT).shift(LEFT)
        self.play(Write(sub_title))
        self.move_x(group_triangle, cur_x, 0.65 - 0.5, circle, pos_a, pos_b, 1.5)
        cur_x = 0.65 - 0.5
        self.wait()
        temp_desc1 = Tex("OX=OB \\Rightarrow \\angle XOB = \\angle XBO").scale(0.65).next_to(
            sub_title, DOWN, buff=1, aligned_edge=LEFT)
        temp_ox = Line(pos_o, point_x)
        temp_ob = Line(pos_o, pos_b)
        self.play(
            Indicate(temp_ox, scale_factor=1.1, run_time=2),
            Indicate(temp_ob, scale_factor=1.1, run_time=2),
            Write(temp_desc1)
        )
        arc1 = draw_arc(pos_o, point_x.get_center(), pos_b, radius=0.5, color=YELLOW)
        arc2 = draw_arc(pos_o, pos_b, point_x.get_center(), radius=0.5, color=YELLOW)
        arc_aob = draw_arc(pos_a, pos_o, pos_b, radius=0.5, color=BLUE)
        self.play(ShowCreation(arc1), ShowCreation(arc2))
        temp_desc2 = Tex("\\angle OXB = \\angle AXB = \\frac{1}{2} \\angle AOB").scale(0.65).next_to(
            temp_desc1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(temp_desc2), ShowCreation(arc_aob))
        self.wait(2)
        sub_title_tmep = VGroup(
            Text("当O在"),
            Tex("\\angle AXB"),
            Text("的内部时")
        ).set_color(BLUE).arrange(RIGHT).scale(0.8).next_to(title, DOWN, buff=0.8, aligned_edge=RIGHT)
        self.remove(arc1, arc2, arc_aob, temp_ox, temp_ob)
        self.play(
            Transform(sub_title, sub_title_tmep),
            FadeOut(temp_desc1),
            FadeOut(temp_desc2),
        )
        self.move_x(group_triangle, cur_x, 0.3, circle, pos_a, pos_b, 1.5)
        cur_x = 0.3
        self.wait()
        pos_c = circle.point_from_proportion(cur_x + 0.5)
        point_c = Dot(pos_c).set_color(RED)
        text_c = Tex("C").next_to(point_c, DOWN, buff=0.1).scale(0.8)
        dash_line_xc = DashedLine(point_x.get_center(), pos_c)
        self.play(ShowCreation(dash_line_xc))
        self.play(Write(text_c), ShowCreation(point_c), run_time=0.5)

        temp_desc1 = Tex("OX=OA").scale(0.65).next_to(sub_title, DOWN, buff=1, aligned_edge=LEFT)
        temp_oa = Line(pos_o, pos_a)
        temp_ox = Line(pos_o, point_x.get_center())
        self.play(
            Indicate(temp_ox, scale_factor=1.1, run_time=2),
            Indicate(temp_oa, scale_factor=1.1, run_time=2),
            Write(temp_desc1),
        )
        self.wait()
        temp_arrow1 = add_right_arrow(temp_desc1)
        self.play(ShowCreation(temp_arrow1))
        arc_oxa = draw_arc(pos_o, point_x.get_center(), pos_a, radius=0.5, color=YELLOW)
        arc_oax = draw_arc(pos_o, pos_a, point_x.get_center(), radius=0.5, color=YELLOW)
        temp_desc2 = Tex("\\angle OXA = \\angle OAX").scale(0.65).next_to(temp_arrow1, RIGHT, buff=0.2)
        self.play(
            ShowCreation(arc_oax),
            ShowCreation(arc_oxa),
            Write(temp_desc2),
        )

        temp_desc3 = Tex("OX=OB").scale(0.65).next_to(temp_desc1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(
            Indicate(temp_ox, scale_factor=1.1, run_time=2),
            Indicate(temp_ob, scale_factor=1.1, run_time=2),
            Write(temp_desc3),
        )
        self.wait()
        temp_arrow2 = add_right_arrow(temp_desc3)
        self.play(ShowCreation(temp_arrow2))
        arc_oxb = draw_arc(pos_o, point_x.get_center(), pos_b, radius=0.5, color=RED)
        arc_obx = draw_arc(pos_o, pos_b, point_x.get_center(), radius=0.5, color=RED)
        temp_desc4 = Tex("\\angle OXB = \\angle OBX").scale(0.65).next_to(temp_arrow2, RIGHT, buff=0.2)
        self.play(
            ShowCreation(arc_oxb),
            ShowCreation(arc_obx),
            Write(temp_desc4),
        )
        temp_desc5 = Tex("\\angle AOB = \\angle AOC + \\angle COB").scale(0.65).next_to(
            temp_desc3, DOWN, buff=0.4, aligned_edge=LEFT)
        temp_desc6 = Tex("\\angle AOC", "= \\angle AXO + \\angle XAO=", "2\\angle AXO").scale(0.65).next_to(
            temp_desc5, DOWN, buff=0.4, aligned_edge=LEFT)
        temp_desc7 = Tex("\\angle COB", "= \\angle BXO + \\angle XBO=", "2\\angle BXO").scale(0.65).next_to(
            temp_desc6, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(temp_desc5))
        self.play(Write(temp_desc6))
        self.play(Write(temp_desc7))

        rect1 = get_rect(temp_desc5, buff=0.1, color=RED)
        rect2 = VGroup(get_rect(temp_desc6[0], buff=0.1, color=RED), get_rect(temp_desc6[2], buff=0.1, color=RED))
        rect3 = VGroup(get_rect(temp_desc7[0], buff=0.1, color=RED), get_rect(temp_desc7[2], buff=0.1, color=RED))
        self.play(
            ShowCreation(rect1),
            ShowCreation(rect2),
            ShowCreation(rect3),
        )
        temp_desc8 = Tex("\\angle AOB = 2\\angle AXO + 2\\angle BXO = 2\\angle AXB").scale(0.65).next_to(
            temp_desc7, DOWN, buff=0.4, aligned_edge=RIGHT)
        self.play(Write(temp_desc8))
        self.wait(2)

        sub_title_tmep = VGroup(
            Text("当O在"),
            Tex("\\angle AXB"),
            Text("的外部时")
        ).set_color(BLUE).arrange(RIGHT).scale(0.8).next_to(title, DOWN, buff=0.8, aligned_edge=RIGHT)
        self.remove(arc1, arc2, arc_aob, temp_ox, temp_ob)
        self.play(
            Transform(sub_title, sub_title_tmep),
            FadeOut(VGroup(
                temp_desc1, temp_desc2, temp_desc3, temp_desc4, temp_desc5, temp_desc6, temp_desc7, temp_desc8,
                temp_arrow1, temp_arrow2, rect1, rect2, rect3, arc_oxa, arc_oax, arc_oxb, arc_obx,
                dash_line_xc, point_c, text_c
            )),
        )
        self.move_x(group_triangle, cur_x, 0.05, circle, pos_a, pos_b, 1.5)
        cur_x = 0.05
        pos_c = circle.point_from_proportion(cur_x + 0.5)
        point_c = Dot(pos_c).set_color(RED)
        text_c = Tex("C").next_to(point_c, DOWN, buff=0.1).scale(0.8)
        dash_line_xc = DashedLine(point_x, pos_c)
        self.play(ShowCreation(dash_line_xc))
        self.play(ShowCreation(point_c), Write(text_c), run_time=0.5)

        self.wait()
        temp_desc1 = Tex("OX=OB").scale(0.65).next_to(sub_title, DOWN, buff=1, aligned_edge=LEFT)
        temp_ox = Line(pos_o, point_x.get_center())
        self.play(
            Indicate(temp_ox, scale_factor=1.1, run_time=2),
            Indicate(temp_ob, scale_factor=1.1, run_time=2),
            Write(temp_desc1),
        )
        self.wait()
        temp_arrow1 = add_right_arrow(temp_desc1)
        temp_desc2 = Tex("\\angle COB", "=", "2\\angle OXB").scale(0.65).next_to(temp_arrow1, RIGHT, buff=0.2)
        self.play(ShowCreation(temp_arrow1))
        arc_cob = draw_arc(pos_c, pos_o, pos_b, radius=0.8, color=YELLOW)
        arc_oxb = draw_arc(pos_o, point_x.get_center(), pos_b, radius=0.8, color=YELLOW)
        self.play(Write(temp_desc2), ShowCreation(arc_cob), ShowCreation(arc_oxb))

        self.wait()
        temp_desc3 = Tex("OX=OA").scale(0.65).next_to(temp_desc1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(
            Indicate(temp_ox, scale_factor=1.1, run_time=2),
            Indicate(temp_oa, scale_factor=1.1, run_time=2),
            Write(temp_desc3),
        )
        self.wait()
        temp_arrow2 = add_right_arrow(temp_desc3)
        temp_desc4 = Tex("\\angle COA", "=", "2\\angle OXA").scale(0.65).next_to(temp_arrow2, RIGHT, buff=0.2)
        self.play(ShowCreation(temp_arrow2))
        arc_coa = draw_arc(pos_c, pos_o, pos_a, radius=0.5, color=PURPLE)
        arc_oxa = draw_arc(pos_o, point_x.get_center(), pos_a, radius=0.5, color=PURPLE)
        self.play(Write(temp_desc4), ShowCreation(arc_coa), ShowCreation(arc_oxa))
        self.wait()
        rect1 = get_rect(VGroup(temp_desc2[0], temp_desc4[0]), buff=0.1, color=BLUE_A)
        rect2 = get_rect(VGroup(temp_desc2[2], temp_desc4[2]), buff=0.1, color=BLUE_C)
        self.play(ShowCreation(rect1), ShowCreation(rect2))
        temp_desc5 = Tex("\\angle AOB = 2\\angle AXB").scale(0.65).next_to(
            temp_desc3, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(temp_desc5))
        self.wait(4)

    def move_x(self, group_triangle, start_proportion, end_proportion, circle, pos_a, pos_b, run_time=2.0):
        def update_x(mob, alpha):
            x = start_proportion + alpha * (end_proportion - start_proportion)
            pos = circle.point_from_proportion(x)
            mob[0].move_to(pos)
            mob[1].put_start_and_end_on(pos, pos_a)
            mob[2].put_start_and_end_on(pos, pos_b)
            mob[3].next_to(pos, DOWN, buff=0.1)

        self.play(
            UpdateFromAlphaFunc(group_triangle, update_x, run_time=run_time),
        )


class InscribedAngle2(Scene):
    def construct(self) -> None:
        title = Title("圆周角定理逆定理").scale(0.9)
        self.add(title)
        circle = Circle(radius=1.5, color=YELLOW)
        # self.play(ShowCreation(circle))
        pos_a = circle.point_from_proportion(0.7)
        pos_b = circle.point_from_proportion(0.9)
        pos_c = circle.point_from_proportion(0.05)
        pos_d = circle.point_from_proportion(0.45)

        text_a = Tex("A").next_to(pos_a, DOWN, buff=0.1).scale(0.7)
        text_b = Tex("B").next_to(pos_b, DOWN, buff=0.1).scale(0.7)
        text_c = Tex("C").next_to(pos_c, UP, buff=0.1).scale(0.7)
        text_d = Tex("D").next_to(pos_d, UP, buff=0.1).scale(0.7)
        polygon = draw_polygon_line(pos_a, pos_b, pos_c, pos_d)
        self.play(ShowCreation(polygon), Write(text_a), Write(text_b), Write(text_c), Write(text_d))
        line_ca = Line(pos_c, pos_a)
        line_db = Line(pos_d, pos_b)
        self.play(ShowCreation(line_ca), ShowCreation(line_db))
        self.wait()
        arc_acb = draw_arc(pos_a, pos_c, pos_b, radius=0.5, color=YELLOW)
        arc_adb = draw_arc(pos_a, pos_d, pos_b, radius=0.5, color=YELLOW)
        bottom_desc = VGroup(
            Text("如果"),
            Tex("\\angle ACB", "=", "\\angle ADB"),
            Text("，则"),
            Tex("\\square ABCD"),
            Text("有外接圆", t2c={"外接圆": YELLOW}),
        ).arrange(RIGHT).scale(0.7).next_to(circle, DOWN, buff=1.5)
        tips = VGroup(
            Tex("\\angle ACB", "=", "\\angle ADB \\rightarrow \\square ABCD"),
            Text("有外接圆", t2c={"外接圆": YELLOW}).scale(0.9),
        ).arrange(RIGHT).scale(0.5).next_to(title, DOWN, buff=1, aligned_edge=LEFT).shift(LEFT)

        self.play(ShowCreation(arc_acb), ShowCreation(arc_adb), Write(bottom_desc[0:2]))
        self.wait()
        self.play(ShowCreation(circle), Write(bottom_desc[2:]))

        self.wait()

        group_temp = VGroup(polygon, text_a, text_b, text_c, text_d, line_ca, line_db, arc_acb, arc_adb)
        self.play(FadeOut(bottom_desc), group_temp.animate.shift(LEFT * 2.5 + DOWN * 0.5), FadeOut(circle),
                  ShowCreation(tips))
        circle.set_color(WHITE).shift(LEFT * 2.5 + DOWN * 0.5)
        pos_a = get_lines_vertices(polygon)[0]
        pos_b = get_lines_vertices(polygon)[1]
        pos_c = get_lines_vertices(polygon)[2]
        pos_d = get_lines_vertices(polygon)[3]
        point_o = Dot(circle.get_center()).scale(0.7)
        text_o = Tex("O").next_to(point_o, UP, buff=0.1).scale(0.7)
        bottom_desc = VGroup(
            Text("对"),
            Tex("ABD"),
            Text("作外接圆O"),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(ShowCreation(circle), Write(bottom_desc), Write(point_o), Write(text_o))
        self.wait()
        self.play(FadeOut(bottom_desc), run_time=0.5)
        bottom_desc = VGroup(
            Text("由正弦定理可得", t2c={"正弦定理": YELLOW}),
            Tex("\\sin \\angle ACB=", "\\sin \\angle ADB =", "\\frac{AB}{2R}"),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(Write(bottom_desc))

        desc1 = Tex("\\sin \\angle ACB", "=\\frac{AB}{2R}").scale(0.6).next_to(
            title, DOWN, buff=0.5, aligned_edge=RIGHT).shift(LEFT * 3.5)
        self.play(
            TransformFromCopy(bottom_desc[1][0], desc1[0]),
            TransformFromCopy(bottom_desc[1][2], desc1[1]),
        )
        self.wait()
        self.play(FadeOut(bottom_desc))
        self.play(FadeOut(VGroup(polygon[2], polygon[3], text_d, arc_adb, line_db)))
        pos_e = circle.point_from_proportion(0.9 - 0.5)
        bottom_desc = VGroup(
            Text("过BO作直线和圆O的交点为E，"),
            Text("BE是直径所以"),
            Tex("\\angle EAB=90^{\\circ}"),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(Write(bottom_desc[0]), ShowCreation(DashedLine(pos_b, pos_e)))
        self.play(Write(Tex("E").next_to(pos_e, UP, buff=0.1).scale(0.7)), run_time=0.5)
        right_angle_eab = get_right_angle_by_points(pos_e, pos_a, pos_b)
        self.play(Write(bottom_desc[1:]), ShowCreation(DashedLine(pos_e, pos_a)), ShowCreation(right_angle_eab))
        self.wait()
        desc2 = Tex("\\angle EAB=90^{\\circ}").scale(0.6).next_to(
            desc1, RIGHT, buff=0.5)
        self.play(TransformFromCopy(bottom_desc[2], desc2))
        self.play(FadeOut(bottom_desc))
        self.wait()
        bottom_desc = VGroup(
            Text("此时只需要证明"),
            Tex("\\angle ECB=90^{\\circ}", color=YELLOW),
            Text("即可得到点"),
            Tex("C"),
            Text("在圆O上")
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(Write(bottom_desc), Write(Line(pos_e, pos_c, color=YELLOW)), Write(Line(pos_c, pos_b, color=YELLOW)))
        desc3 = bottom_desc.copy().scale(0.5 / 0.7).next_to(desc1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(TransformFromCopy(bottom_desc, desc3))
        self.remove(bottom_desc)
        angle_acb = cal_triangle_angle(pos_a, pos_c, pos_b)
        pos_f = pos_c + cal_dis(pos_c, pos_b) * math.cos(angle_acb) * Line(pos_c, pos_a).get_unit_vector()
        dash_line_bf = DashedLine(pos_b, pos_f)
        bottom_desc = VGroup(
            Text("过"),
            Tex("B"),
            Text("作"),
            Tex("AC"),
            Text("的垂线交于点"),
            Tex("F"),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(Write(bottom_desc), ShowCreation(dash_line_bf))
        right_angle_bfc = get_right_angle_by_points(pos_b, pos_f, pos_c, size=0.15)
        self.play(ShowCreation(Tex("F").next_to(pos_f, UP, buff=0.1).scale(0.7)), ShowCreation(right_angle_bfc))
        self.wait()
        self.play(FadeOut(bottom_desc))
        arc_aeb = draw_arc(pos_a, pos_e, pos_b, color=YELLOW, radius=0.5)
        bottom_desc = VGroup(
            Tex("\\angle EAB=90^{\\circ}"),
            Tex("\\rightarrow"),
            Tex("\\sine \\angle AEB"),
            Tex("=\\frac{AB}{EB}=\\frac{AB}{2R}="),
            Tex("\\sin \\angle ACB"),
        ).arrange(RIGHT).scale(0.7).move_to(bottom_desc)
        self.play(TransformFromCopy(desc2, bottom_desc[0]))
        self.play(Write(bottom_desc[1:4]))
        self.play(TransformFromCopy(desc1[0], bottom_desc[4]))
        angle_text1 = Tex("1", color=BLUE).scale(0.4).next_to(arc_aeb, DOWN, buff=0.1).shift(RIGHT * 0.2)
        angle_text2 = Tex("1", color=BLUE).scale(0.4).next_to(arc_acb, DOWN, buff=0.1).shift(LEFT * 0.1)
        self.play(ShowCreation(arc_aeb), Write(angle_text1), ShowCreation(arc_acb), Write(angle_text2))
        self.wait()
        desc4 = Tex(
            "\\sine \\angle AEB",
            "=",
            "\\sin \\angle ACB",
            "\\rightarrow \\angle AEB=\\angle ACB \\rightarrow ",
            "\\angle EBA=\\angle EBF",
        ).scale(0.5).next_to(desc3, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(TransformFromCopy(bottom_desc[2], desc4[0]))
        self.play(Write(desc4[1], run_time=0.2))
        self.play(TransformFromCopy(bottom_desc[4], desc4[2]))
        self.play(Write(desc4[3:]))
        self.wait()
        self.play(FadeOut(VGroup(desc4[0:4])))
        self.play(desc4[4].next_to, desc3, DOWN, {"buff": 0.4, "aligned_edge": LEFT})
        desc5 = Tex("\\rightarrow", "\\angle ABF=\\angle EBC").scale(0.5).next_to(desc4[4], RIGHT, buff=0.1)
        self.play(Write(desc5))
        self.wait()
        desc6 = Tex("BF = BC \\cdot \\sin 1").scale(0.5).next_to(desc4[4], DOWN, buff=0.4, aligned_edge=LEFT)
        desc7 = Tex("AB = BE \\cdot \\sin 1").scale(0.5).next_to(desc6, DOWN, buff=0.4, aligned_edge=LEFT)
        brace = Brace(VGroup(desc6, desc7), RIGHT, buff=0.1)
        desc8 = Tex("\\frac{BF}{AB} = \\frac{BC}{BE}").scale(0.5)
        brace.put_at_tip(desc8)
        self.play(Write(desc6))
        self.play(Write(desc7))
        self.play(GrowFromCenter(brace))
        self.play(Write(desc8))
        self.wait()
        self.play(ShowCreation(SurroundingRectangle(desc5[1], color=BLUE, buff=0.1)))
        self.play(ShowCreation(SurroundingRectangle(desc8, color=BLUE, buff=0.1)))
        desc9 = Tex("\\triangle ABF \\sim \\triangle EBC").scale(0.5).next_to(desc7, DOWN, buff=0.4, aligned_edge=LEFT)
        triangle_abf = Polygon(pos_a, pos_b, pos_f, color=BLUE)
        triangle_ebc = Polygon(pos_e, pos_b, pos_c, color=BLUE)
        self.play(ShowCreation(triangle_abf))
        self.play(ShowCreation(triangle_ebc))
        self.play(Write(desc9))
        self.wait()
        desc10 = Tex("\\rightarrow \\angle ECB=\\angle AFB=90^{\\circ}").scale(0.5).next_to(desc9, RIGHT, buff=0.1)
        self.play(Write(desc10))
        self.play(ShowCreation(SurroundingRectangle(desc3, color=BLUE, buff=0.1)))
        self.wait()
        self.remove(triangle_abf, triangle_ebc)
        desc11 = VGroup(
            Tex("\\therefore \\square ABCD"),
            Text("有外接圆", t2c={"外接圆": YELLOW}),
            Tex("O")
        ).arrange(RIGHT).scale(0.5).next_to(desc9, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(ShowCreation(
            VGroup(Line(pos_a, pos_b), Line(pos_b, pos_c), Line(pos_c, pos_d), Line(pos_d, pos_a)).set_color(BLUE)),
            Write(Tex("D").next_to(pos_d, UP, buff=0.1).scale(0.7))
        )
        self.play(Write(desc11))
        self.wait(5)
