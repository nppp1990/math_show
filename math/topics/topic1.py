from manimlib import *


class Topic1(Scene):
    def construct(self) -> None:
        title = Title('比较大小').scale(0.9)
        self.add(title)
        formula = VGroup(
            Tex("1000^{1001}", color=BLUE),
            Tex("<"),
            Tex("1001^{1000}", color=GREEN),
        ).arrange(RIGHT, buff=0.2)
        bottom_desc = VGroup(
            Tex("1001^{1000}", color=GREEN),
            Text("比较大"),
        ).scale(0.7).arrange(RIGHT).move_to(ORIGIN + DOWN * 3)
        desc_temp = VGroup(
            Text("还是"),
            Tex("1000^{1001}", color=BLUE),
            Text("比较大"),
        ).scale(0.7).arrange(RIGHT).move_to(ORIGIN + DOWN * 3)
        self.play(Write(formula[0]), Write(formula[2]))
        self.play(Write(formula[1]), Write(bottom_desc))
        temp = Tex(">").next_to(formula[0], RIGHT)
        self.play(Transform(formula[1], temp), Transform(bottom_desc, desc_temp))
        self.wait(2)
        self.remove(bottom_desc)
        bottom_desc = VGroup(
            Text("用瞪眼法可知", t2c={"瞪眼法": YELLOW}),
            Tex("1000^{1001}", color=BLUE),
            Text("比较大，下面咱们证明一下"),
        ).scale(0.7).arrange(RIGHT).move_to(ORIGIN + DOWN * 3)
        self.play(Write(bottom_desc))
        temp = Tex("\\frac {1000^{1001}}{1001^{1000}}", ">1").move_to(formula)
        self.wait()
        self.play(Transform(formula, temp))
        self.play(formula.next_to, title, DOWN, {"buff": 0.5})
        desc1 = Tex("\\frac {1000^{1001}}{1001^{1000}}").scale(0.6).next_to(
            title, DOWN, buff=2, aligned_edge=LEFT).shift(LEFT)
        temp = Tex("(\\frac{1000}{1001})^{1000}\\cdot 1000", ).scale(0.6).next_to(
            title, DOWN, buff=2, aligned_edge=LEFT).shift(LEFT)
        # self.play(Write(desc1))
        desc1 = temp
        self.play(Write(desc1))
        # self.play(TransformFromCopy(formula[0], desc1))
        # self.play(Transform(desc1, temp))
        self.wait()
        desc2 = Tex("=(1-\\frac{1}{1001})^{1000}\\cdot 1000", ).scale(0.6).next_to(desc1, RIGHT, buff=0.1)
        self.play(Write(desc2))
        desc3 = Tex(
            ">(1-\\frac{1}{1001})",
            "\\cdot",
            "(1-\\frac{1}{1000})",
            "\\cdot",
            "(1-\\frac{1}{999})",
            "\\cdot\\cdot\\cdot",
            "(1-\\frac{1}{2})",
            "\\cdot 1000", ).scale(0.6).next_to(desc2, RIGHT, buff=0.1)
        self.play(Write(desc3))
        desc4 = VGroup(
            Tex("\\frac{1000}{1001}").scale(0.6).next_to(desc3[0], DOWN, buff=0.3),
            Tex("\\times", ).scale(0.6).next_to(desc3[1], DOWN, buff=0.8),
            Tex("\\frac{999}{1000}").scale(0.6).next_to(desc3[2], DOWN, buff=0.3),
            Tex("\\times", ).scale(0.6).next_to(desc3[3], DOWN, buff=0.8),
            Tex("\\frac{998}{999}").scale(0.6).next_to(desc3[4], DOWN, buff=0.3),
            Tex("\\cdot\\cdot\\cdot", ).scale(0.6).next_to(desc3[5], DOWN, buff=0.8),
            Tex("\\frac{1}{2}").scale(0.6).next_to(desc3[6], DOWN, buff=0.3),
            Tex("\\times 1000", ).scale(0.6).next_to(desc3[7], DOWN, buff=0.7)
        )
        self.play(Write(desc4))
        del_line1 = Line(desc4[0].get_left(), desc4[0].get_right(), color=RED).shift(UP * 0.2)
        del_line2 = Line(desc4[2].get_left(), desc4[2].get_right(), color=RED).shift(DOWN * 0.2)
        self.play(ShowCreation(del_line1), ShowCreation(del_line2))
        del_line3 = Line(desc4[2].get_left(), desc4[2].get_right(), color=RED).shift(UP * 0.2)
        del_line4 = Line(desc4[4].get_left(), desc4[4].get_right(), color=RED).shift(DOWN * 0.2)
        self.play(ShowCreation(del_line3), ShowCreation(del_line4))
        del_line5 = Line(desc4[4].get_left(), desc4[4].get_right(), color=RED).shift(UP * 0.2)
        del_line6 = Line(desc4[6].get_left(), desc4[6].get_right(), color=RED).shift(DOWN * 0.2)
        self.play(ShowCreation(del_line5), ShowCreation(del_line6))
        desc5 = Tex(">\\frac{1000}{1001}").scale(0.6).next_to(desc4[7], DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(desc5))
        self.play(FadeOut(
            VGroup(desc3, desc4, del_line1, del_line2, del_line3, del_line4, del_line5, del_line6, bottom_desc)))
        self.play(desc5.next_to, desc2, RIGHT, {"buff": 0.1})
        bottom_desc = VGroup(
            Tex("\\frac{1000}{1001}<1", color=GREEN),
            Text("所以不能证明大于1", t2c={"不能证明大于1": RED}),
            Text("但是可以修改下上面的式子"),
        ).scale(0.7).arrange(RIGHT).move_to(ORIGIN + DOWN * 3)
        self.play(Write(bottom_desc[0]))
        self.play(Write(bottom_desc[1]))
        self.play(Write(bottom_desc[2]))
        self.wait()
        desc6 = Tex(">\\frac{1000}{1001}\\cdot\\frac{999}{1000}\\cdot\\cdot\\cdot\\frac{2}{3}",
                    "\\cdot\\frac{1000}{1001}\\cdot 1000").scale(0.6).next_to(desc2, RIGHT, buff=0.1)
        self.play(FadeOut(desc5), Write(desc6))
        self.remove(bottom_desc)
        brace = Brace(desc6[0], DOWN, color=GREEN)
        brace_desc = Text("一共999个").scale(0.6).next_to(brace, DOWN, buff=0.1)
        self.play(Write(brace), ShowCreation(brace_desc))
        bottom_desc = Text("少化简一个连乘，这样就不会小于1了").scale(0.7).move_to(ORIGIN + DOWN * 3)
        self.play(Write(bottom_desc))
        desc7 = Tex("=\\frac{2\\times1000\\times1000}{1001\\times1001}", ">1").scale(0.6).next_to(
            desc6, RIGHT, buff=0.1)
        self.play(Write(desc7[0]))
        self.play(Write(desc7[1]))
        self.wait(5)
