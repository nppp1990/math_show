from manimlib import *


class Heron(Scene):
    def construct(self) -> None:
        title = Title('海伦公式').scale(0.9)
        self.add(title)
        # 三角形ABC
        origin = ORIGIN + DOWN
        pos_a = origin + UP * 2
        pos_b = origin + LEFT * 3
        pos_c = origin + RIGHT * 2
        triangle = Polygon(pos_a, pos_b, pos_c).set_stroke(width=4)
        point_a = Tex('A').next_to(pos_a, UP, buff=0.1).scale(0.8)
        point_b = Tex('B').next_to(pos_b, LEFT, buff=0.1).scale(0.8)
        point_c = Tex('C').next_to(pos_c, RIGHT, buff=0.1).scale(0.8)
        self.play(ShowCreation(triangle), Write(point_a), Write(point_b), Write(point_c))
        text_a = Tex('a').scale(0.8).next_to((pos_b + pos_c) / 2, DOWN, buff=0.1)
        text_b = Tex('b').scale(0.8).next_to((pos_a + pos_c) / 2, RIGHT, buff=0.1)
        text_c = Tex('c').scale(0.8).next_to((pos_a + pos_b) / 2, LEFT, buff=0.1)
        self.play(Write(text_a), Write(text_b), Write(text_c))
        self.wait()

        # 三角形abc
        formula = Tex("\\triangle ABC=\\sqrt{p(p-a)(p-b)(p-c)}").scale(0.7).next_to(triangle, DOWN, buff=1)
        formula_s = Tex("S").next_to(formula, LEFT, buff=0).scale(1.1).shift(UP * 0.05)
        self.play(Write(formula_s, run_time=0.2))
        self.play(Write(formula))
