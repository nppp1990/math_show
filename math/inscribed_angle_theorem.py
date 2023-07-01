import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.common.utils.math_utils import draw_arc
from yj.common.math.object_utils import add_right_arrow, get_rect

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
