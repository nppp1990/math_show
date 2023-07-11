import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.math_show.common.utils.math_utils import get_cross_point
from yj.math_show.common.math.object_utils import get_right_angle


def create_triangle(pos1, pos2, pos3, **kwargs):
    line1 = Line(pos1, pos2, **kwargs)
    line2 = Line(pos2, pos3, **kwargs)
    line3 = Line(pos3, pos1, **kwargs)
    return VGroup(line1, line2, line3)


def get_vertices(triangle_group):
    return [triangle_group[0].get_start(), triangle_group[1].get_start(), triangle_group[2].get_start()]


class Topic3(Scene):
    def construct(self) -> None:
        title = Title('求最小值').scale(0.9)
        self.add(title)
        topic = VGroup(
            Text("求"),
            Tex("\\sqrt{x^2 + 9}", "+", "\\sqrt{(12-x)^2 + 4"),
            Text("的最小值"),
        ).arrange(RIGHT, buff=0.1).scale(0.8)
        self.play(Write(topic))
        self.wait(2)
        self.play(topic.shift, UP * 2)
        # tip1 = Tex("\\sqrt{x^2 + 3^2}").scale(0.7).next_to(topic[1][0], DOWN, buff=0.4)
        # tip2 = Tex("\\sqrt{(12-x)^2 + 2^2}").scale(0.7).next_to(topic[1][2], DOWN, buff=0.4)
        # self.play(TransformFromCopy(topic[1][0], tip1), TransformFromCopy(topic[1][2], tip2))

        x = 2
        scale_triangle = 0.4
        pos1 = topic.get_left() + DOWN * 1.5
        pos2 = pos1 + 3 * DOWN * scale_triangle
        pos3 = pos2 + x * RIGHT * scale_triangle
        bottom_desc = VGroup(
            Text("利用勾股定理，构造三角形得到", t2c={'勾股定理': YELLOW}),
            Tex("\\sqrt{x^2 + 9}"),
        ).arrange(RIGHT, buff=0.3).scale(0.7).move_to(ORIGIN + DOWN * 3)
        triangle1 = create_triangle(pos1, pos2, pos3)
        self.play(ShowCreation(triangle1), Write(bottom_desc))
        text_3 = Tex("3").scale(0.7).next_to(Line(pos1, pos2), LEFT, buff=0.1)
        text_x = Tex("x").scale(0.7).next_to(Line(pos2, pos3), DOWN, buff=0.1)
        self.play(Write(text_3), Write(text_x))

        pos4 = topic.get_center() + DOWN * 1.5
        pos5 = pos4 + 2 * DOWN * scale_triangle
        pos6 = pos5 + (12 - x) * RIGHT * scale_triangle
        triangle2 = create_triangle(pos4, pos5, pos6)
        bottom_desc = self.update_tips(bottom_desc, VGroup(
            Text("利用勾股定理，构造三角形得到", t2c={'勾股定理': YELLOW}),
            Tex("\\sqrt{(12-x)^2 + 4}"),
        ).arrange(RIGHT))
        self.play(ShowCreation(triangle2), Write(bottom_desc))
        text_2 = Tex("2").scale(0.7).next_to(Line(pos4, pos5), LEFT, buff=0.1)
        text_12_x = Tex("12-x").scale(0.7).next_to(Line(pos5, pos6), DOWN, buff=0.1)
        self.play(Write(text_2), Write(text_12_x))

        self.wait()
        self.play(FadeOut(VGroup(text_2, text_3, text_12_x, text_x)))
        self.play(ApplyMethod(triangle2.rotate, PI, axis=OUT, about_point=pos5))
        self.wait()
        offset = (get_vertices(triangle2)[2] - get_vertices(triangle1)[2]) / 2
        self.play(
            ApplyMethod(triangle1.shift, offset),
            ApplyMethod(triangle2.shift, -offset),
        )
        bottom_desc = self.update_tips(bottom_desc, VGroup(
            Text("修改三角形的位置，使"),
            Tex("x"),
            Text("和"),
            Tex("12-x"),
            Text("在同一直线上"),
        ).arrange(RIGHT))
        self.play(Write(bottom_desc))
        pos1 = get_vertices(triangle1)[0]
        pos2 = get_vertices(triangle1)[1]
        pos3 = get_vertices(triangle1)[2]
        pos4 = get_vertices(triangle2)[0]
        pos5 = get_vertices(triangle2)[1]
        pos6 = get_vertices(triangle2)[2]
        text_3 = Tex("3").scale(0.7).next_to(Line(pos1, pos2), LEFT, buff=0.1)
        text_x = Tex("x").scale(0.7).next_to(Line(pos2, pos3), DOWN, buff=0.1)
        text_2 = Tex("2").scale(0.7).next_to(Line(pos4, pos5), RIGHT, buff=0.1)
        text_12_x = Tex("12-x").scale(0.7).next_to(Line(pos5, pos6), UP, buff=0.1)
        self.play(Write(text_3), Write(text_x), Write(text_2), Write(text_12_x))
        constant_objs = VGroup(text_3, text_2, Line(pos2, pos5), triangle1[0], triangle2[0])
        self.play(
            ApplyMethod(constant_objs.set_color, GREEN),
        )
        self.play(
            ShowCreation(Tex("A").scale(0.6).next_to(pos1, LEFT, buff=0.1)),
            ShowCreation(Tex("B").scale(0.6).next_to(pos2, LEFT, buff=0.1)),
            ShowCreation(Tex("C").scale(0.6).next_to(pos5, RIGHT, buff=0.1)),
            ShowCreation(Tex("D").scale(0.6).next_to(pos4, RIGHT, buff=0.1)),
        )
        self.wait()
        line1 = triangle1[2]
        line2 = triangle2[2]
        text_p = Tex("P", color=YELLOW).scale(0.6).next_to(pos3, DOWN, buff=0.1)
        bottom_desc = self.update_tips(bottom_desc, VGroup(
            Text("此时结果等于"),
            Tex("AP+PD"),
        ).arrange(RIGHT))
        self.play(ApplyMethod(line1.set_color, YELLOW),
                  ApplyMethod(line2.set_color, YELLOW),
                  Write(text_p, run_time=0.5), Write(bottom_desc, run_time=1.5))

        changed_obj = VGroup(line1, line2, text_p)
        self.wait(2)
        bottom_desc = self.update_tips(bottom_desc, VGroup(
            Tex("A"), Text(" "),
            Tex("B"), Text(" "),
            Tex("C"), Text(" "),
            Tex("D"), Text("的位置固定", t2c={'固定': YELLOW}),
            Tex("P"), Text("的位置变化，并且在直线"),
            Tex("BC"), Text("上"),
        ).arrange(RIGHT))
        self.play(Write(bottom_desc))

        def update_p(mob, alpha):
            if alpha < 0.25:
                cur_x = 2 - alpha * 16
            else:
                cur_x = -6 + alpha * 16
            cur_pos = pos2 + cur_x * RIGHT * scale_triangle
            mob[0].put_start_and_end_on(pos1, cur_pos)
            mob[1].put_start_and_end_on(pos4, cur_pos)
            mob[2].next_to(cur_pos, DOWN, buff=0.1)

        self.remove(text_x, text_12_x)
        self.add(text_x)
        self.play(
            UpdateFromAlphaFunc(changed_obj, update_p),
            run_time=4
        )
        pos_x = get_cross_point(pos1, pos4, pos2, pos5)
        dash_line_ad = DashedLine(pos1, pos4)
        bottom_desc = self.update_tips(bottom_desc, VGroup(
            Text("两点之间直线最短，所以", t2c={'直线': YELLOW}),
            Tex("AD\\leq AP+PD"),
        ).arrange(RIGHT))
        self.wait()
        self.play(ShowCreation(dash_line_ad),
                  Write(Tex("X").scale(0.6).next_to(pos_x, DOWN, buff=0.1), run_time=0.5)
                  , Write(bottom_desc, run_time=1.5))
        self.wait()
        pos_e = pos2 + DOWN * 2 * scale_triangle
        line3 = DashedLine(pos2, pos_e)
        line4 = DashedLine(pos_e, pos4)
        self.play(Transform(Line(pos5, pos4), line3))
        self.play(Transform(Line(pos2, pos5), line4))
        self.play(ShowCreation(get_right_angle(pos_e, RIGHT * 0.25, UP * 0.25)))
        brace1 = Brace(Line(pos1, pos_e), LEFT, buff=0.3)
        brace2 = Brace(Line(pos_e, pos4), DOWN, buff=0.3)
        self.play(ShowCreation(brace1), ShowCreation(brace2),
                  Write(brace1.get_tex("5").scale(0.6)), Write(brace2.get_tex("12").scale(0.6)))
        self.wait()
        bottom_desc = self.update_tips(bottom_desc, VGroup(
            Text("最小值为"),
            Tex("AD=\\sqrt{5^2+12^2}=13", color=GREEN),
        ).arrange(RIGHT))
        self.play(ApplyMethod(dash_line_ad.set_color, GREEN), Write(bottom_desc))
        self.wait(5)

    def update_tips(self, desc, obj):
        self.play(FadeOut(desc, run_time=0.5))
        return obj.scale(0.7).move_to(desc)
