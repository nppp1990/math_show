import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.math_show.common.math.object_utils import get_right_angle
from manimlib import *


class Topic2(Scene):
    def construct(self) -> None:
        title = Title('求x值').scale(0.9)
        self.add(title)
        topic = VGroup(
            Text("若"),
            Tex("\\sqrt{16-x^2}", "+", "\\sqrt{9-x^2}", "=", "5"),
            Text("，求"),
            Tex("x"),
            Text("的值"),
        ).arrange(RIGHT).scale(0.8)
        self.play(Write(topic))
        x_value = 12 / 5
        self.wait(5)
        tip1 = Tex("16=", "4", "^2", color=YELLOW).scale(0.7).next_to(topic[1][0], DOWN, buff=0.4)
        tip2 = Tex("9=", "3", "^2", color=BLUE).scale(0.7).next_to(topic[1][2], DOWN, buff=0.4)
        self.play(Write(tip1), Write(tip2))
        tip3 = VGroup(
            Tex("3"),
            Tex("4"),
            Tex("5"),
        ).scale(0.6).arrange(RIGHT, buff=0.5).next_to(VGroup(tip1, tip2), DOWN, buff=0.5)
        self.play(TransformFromCopy(tip1[1], tip3[1]))
        self.play(TransformFromCopy(tip2[1], tip3[0]))
        self.play(TransformFromCopy(topic[1][4], tip3[2]))
        tip4 = Text("这是一对勾股数", t2c={"勾股数": RED}).scale(0.6).next_to(tip3, RIGHT, buff=0.5)
        self.play(Write(tip4))
        self.wait(2)
        self.play(
            FadeOut(VGroup(tip1, tip2, tip3, tip4)),
            topic.shift, UP * 2,
        )

        pos1 = topic.get_left() + DOWN
        pos2 = pos1 + x_value * DOWN
        pos3 = pos2 + LEFT * math.sqrt(16 - x_value ** 2)
        triangle1 = Polygon(pos1, pos2, pos3).scale(0.7).shift(RIGHT * 2)
        # 三角形三个点的坐标
        pos1 = triangle1.get_vertices()[0]
        pos2 = triangle1.get_vertices()[1]
        pos3 = triangle1.get_vertices()[2]
        right_angle1 = get_right_angle(pos2, LEFT * 0.3, UP * 0.3)
        self.play(ShowCreation(triangle1))
        self.play(ShowCreation(right_angle1))
        text_4 = Tex("4").scale(0.7).move_to((pos1 + pos3) / 2).shift(LEFT * 0.2 + UP * 0.1)
        text_x1 = Tex("x", color=BLUE).scale(0.7).next_to(Line(pos1, pos2), LEFT, buff=0.1)
        self.play(Write(text_4), Write(text_x1))

        pos4 = topic.get_right() + DOWN
        pos5 = pos4 + x_value * DOWN
        pos6 = pos5 + RIGHT * math.sqrt(9 - x_value ** 2)
        triangle2 = Polygon(pos4, pos5, pos6).scale(0.7).shift(LEFT * 4)
        # 三角形三个点的坐标
        pos4 = triangle2.get_vertices()[0]
        pos5 = triangle2.get_vertices()[1]
        pos6 = triangle2.get_vertices()[2]
        right_angle2 = get_right_angle(pos5, RIGHT * 0.3, UP * 0.3)
        self.play(ShowCreation(triangle2))
        self.play(ShowCreation(right_angle2))
        text_3 = Tex("3").scale(0.7).move_to((pos4 + pos6) / 2).shift(RIGHT * 0.2 + UP * 0.1)
        text_x2 = Tex("x", color=BLUE).scale(0.7).next_to(Line(pos4, pos5), RIGHT, buff=0.1)
        self.play(Write(text_3), Write(text_x2))
        offset = pos4 - pos1
        self.play(
            VGroup(triangle1, text_4, text_x1, right_angle1).shift, offset / 2,
            VGroup(triangle2, text_3, text_x2, right_angle2).shift, -offset / 2,
        )
        l_text = Tex("\\sqrt{16-x^2}").scale(0.6).next_to(Line(pos2, pos3), DOWN, buff=0.1).shift(offset / 2)
        r_text = Tex("\\sqrt{9-x^2}").scale(0.6).next_to(Line(pos5, pos6), DOWN, buff=0.1).shift(-offset / 2)
        self.play(TransformFromCopy(topic[1][0], l_text))
        self.play(TransformFromCopy(topic[1][2], r_text))
        brace = Brace(Line(pos3 + offset / 2, pos6 - offset / 2), DOWN, buff=0.5)
        self.play(ShowCreation(brace))
        text_5 = Tex("5").scale(0.7).next_to(brace, DOWN, buff=0.1)
        self.play(Write(text_5))
        self.play(
            Indicate(text_3, scale_factor=1.2),
            Indicate(text_4, scale_factor=1.2),
            Indicate(text_5, scale_factor=1.2),
        )
        right_angle3 = get_right_angle(pos1 + offset / 2,
                                       Line(pos1, pos3).get_unit_vector() * 0.3,
                                       Line(pos4, pos6).get_unit_vector() * 0.3).set_color(YELLOW)
        self.play(ShowCreation(right_angle3))
        self.wait()
        desc = VGroup(
            Tex("S=\\frac{3\\times 4}{2}=\\frac{5x}{2}"),
            Tex("\\downarrow"),
            Tex("x=\\frac{12}{5}"),
        ).arrange(DOWN).scale(0.7).next_to(triangle2, RIGHT, buff=0.5).shift(RIGHT + DOWN * 0.5)
        self.play(Write(desc[0]))
        self.play(Write(desc[1]), run_time=0.5)
        self.play(Write(desc[2]))
