import numpy as np

from manimlib import *

# 定义常量scale
tangle_scale = 0.5


def init_tangle():
    a = Line(
        np.array([0, 3, 0]),
        np.array([0, 0, 0]),
        color=BLACK
    )
    text1 = Tex("a").set_color(BLUE).next_to(a, LEFT * 0.6)

    b = Line(
        np.array([0, 0, 0]),
        np.array([4, 0, 0]),
        color=BLACK
    )
    text2 = Tex("b").set_color(RED).next_to(b, DOWN * 0.6)

    c = Line(
        np.array([4, 0, 0]),
        np.array([0, 3, 0]),
        color=BLACK
    )
    text3 = Tex("c").set_color(GREEN).next_to(c, OUT).shift(RIGHT * 0.4)

    size = 0.4
    square1 = Line(
        np.array([0, size, 0]),
        np.array([size, size, 0]),
        color=BLACK
    )
    square2 = Line(
        np.array([size, 0, 0]),
        np.array([size, size, 0]),
        color=BLACK)

    tangle = VGroup(text1, text2, text3, a, b, c, square1, square2).shift(LEFT + DOWN)
    real_tangle = VGroup(a, b, c, square1, square2)
    formula1 = Tex("a²", "+", "b²", "=", "c²").next_to(tangle, DOWN * 2)

    return tangle, real_tangle, a, b, c, text1, text2, text3, formula1


def init_tangle_with_number(number1, number2):
    a = Line(
        np.array([0, number1, 0]),
        np.array([0, 0, 0]),
        color=BLACK
    )
    text1 = Tex("a").set_color(BLUE).next_to(a, LEFT * 0.6)

    b = Line(
        np.array([0, 0, 0]),
        np.array([number2, 0, 0]),
        color=BLACK
    )
    text2 = Tex("b").set_color(RED).next_to(b, DOWN * 0.6)

    c = Line(
        np.array([number2, 0, 0]),
        np.array([0, number1, 0]),
        color=BLACK
    )
    text3 = Tex("c").set_color(GREEN).next_to(c, OUT).shift(RIGHT * 0.4)

    size = 0.4
    square1 = Line(
        np.array([0, size, 0]),
        np.array([size, size, 0]),
        color=BLACK
    )
    square2 = Line(
        np.array([size, 0, 0]),
        np.array([size, size, 0]),
        color=BLACK)

    tangle = VGroup(text1, text2, text3, a, b, c, square1, square2).shift(LEFT + DOWN)
    real_tangle = VGroup(a, b, c, square1, square2)
    formula1 = Tex("a²", "+", "b²", "=", "c²").next_to(tangle, DOWN * 2)

    return tangle, real_tangle, a, b, c, text1, text2, text3, formula1


def add_indicator(tangle):
    text1 = Tex("a").set_color(BLUE).next_to(tangle[0], OUT).scale(0.6)
    text2 = Tex("b").set_color(RED).next_to(tangle[1], OUT).scale(0.6)
    text3 = Tex("c").set_color(GREEN).next_to(tangle[2], OUT).scale(0.6)
    return text1, text2, text3


class Test1(Scene):
    def construct(self) -> None:
        # 画一个直角三角形
        # 三边长分别为3,4,5
        # 三条边长度a、b、c
        #
        tangle, real_tangle, a, b, c, text1, text2, text3, formula1 = init_tangle()
        self.wait(1)
        self.play(ShowCreation(tangle))
        self.wait(1)
        self.play(FadeIn(formula1))
        self.wait(1)

        copy_a = a.copy().set_stroke(width=5).set_color(BLUE_A)
        self.play(Write(copy_a))
        self.play(Indicate(formula1[0], scale_factor=1.5))

        copy_b = b.copy().set_stroke(width=5).set_color(BLUE_A)
        self.play(Write(copy_b))
        self.play(Indicate(formula1[2], scale_factor=1.5))

        copy_c = c.copy().set_stroke(width=5).set_color(BLUE_A)
        self.play(Write(copy_c))
        self.play(Indicate(formula1[4], scale_factor=1.5))

        self.wait()
        self.remove(copy_a, copy_b, copy_c)
        group1 = VGroup(tangle, formula1)
        self.play(
            group1.scale, 0.6,
            group1.shift, LEFT * 6 + UP * 2)
        # self.wait()
        copy1 = real_tangle.copy().shift(RIGHT * 3)
        copy2 = real_tangle.copy().shift(RIGHT * 6)
        copy3 = real_tangle.copy().shift(RIGHT * 9)

        self.play(ShowCreation(copy1), ShowCreation(copy2), ShowCreation(copy3))

        self.play(
            Rotate(copy1, angle=PI / 2),
            Rotate(copy2, angle=PI),
            Rotate(copy3, angle=PI * 3 / 2),
        )

        tangle.shift(DOWN * 3 + RIGHT * 2.5)

        copy11 = copy1.copy()
        copy11.shift(UP * (real_tangle[1].get_bottom()[1] - copy11[0].get_bottom()[1]))
        copy11.shift(RIGHT * (real_tangle[1].get_right()[0] - copy11[0].get_left()[0]))

        copy22 = copy2.copy()
        copy22.shift(UP * (copy11[1].get_top()[1] - copy22[0].get_bottom()[1]))
        copy22.shift(RIGHT * (copy11[1].get_right()[0] - copy22[0].get_right()[0]))
        # self.add(copy2)
        #
        # copy3 = real_tangle.copy().rotate(angle=PI * 3 / 2)
        copy33 = copy3.copy()
        copy33.shift(UP * (copy22[1].get_top()[1] - copy33[0].get_top()[1]))
        copy33.shift(RIGHT * (copy22[1].get_left()[0] - copy33[0].get_right()[0]))
        # self.add(copy3)

        self.play(
            Transform(copy1, copy11),
            Transform(copy2, copy22),
            Transform(copy3, copy33),
        )
        self.add_indicator(copy1)
        self.add_indicator(copy2)
        self.add_indicator(copy3)

        self.show_square_area(real_tangle, copy1, copy2, copy3)

    def add_indicator(self, tangle):
        text1 = Tex("a").set_color(BLUE).next_to(tangle[0], OUT).scale(0.6)
        text2 = Tex("b").set_color(RED).next_to(tangle[1], OUT).scale(0.6)
        text3 = Tex("c").set_color(GREEN).next_to(tangle[2], OUT).scale(0.6)
        self.play(
            Write(text1),
            Write(text2),
            Write(text3),
        )

    def show_square_area(self, tangle1, tangle2, tangle3, tangle4):
        # tangle1[0]的长度
        size = tangle1[0].get_length() + tangle1[1].get_length()
        origin = (tangle1[1].get_start() + tangle3[1].get_start()) / 2
        square1 = Square(side_length=size).set_stroke(width=5).set_color(BLUE_A).move_to(origin)
        square1.set_fill(BLUE_A, opacity=0.5)
        self.play(ShowCreation(square1))
        square_text = Tex("(a+b)²", " = a² + 2ab + b²").set_color(BLUE_A).scale(0.6).next_to(square1, RIGHT * 2)
        self.play(Write(square_text[0]))
        self.play(square_text.shift, UP * 1)
        self.remove(square1)

        formula2 = Tex("ab/2 ", "+ ab/2 ", "+ ab/2", "+ ab/2 ", "+ c² ", "= 2ab + c²").set_color(BLUE_A).scale(
            0.6).next_to(square1, RIGHT * 2)

        self.show_area(tangle1, formula2[0])
        self.show_area(tangle2, formula2[1])
        self.show_area(tangle3, formula2[2])
        self.show_area(tangle4, formula2[3])
        self.show_mid_area(tangle1, tangle2, tangle3, tangle4, formula2[4])
        self.play(Write(formula2[5]))
        self.play(formula2.shift, UP * 0.3)

        arrow = Line(formula2.get_bottom() + DOWN * 0.2, formula2.get_bottom() + DOWN * 0.8)
        arrow.add_tip(width=0.16, length=0.16)
        self.play(ShowCreation(arrow))
        formula3 = Tex("c² = a² + b²").set_color(BLUE_A).scale(0.6).next_to(arrow, DOWN * 0.2)
        self.play(Write(formula3))

    def show_area(self, tangle, text) -> None:
        area = Polygon(
            tangle[0].get_start(),
            tangle[1].get_start(),
            tangle[2].get_start(),
        ).set_stroke(width=5).set_color(BLUE_A).set_fill(BLUE_A, opacity=0.5)
        area_text = Tex("ab/2").set_color(YELLOW).move_to(
            (tangle[0].get_center() + tangle[1].get_center()) / 2).scale(0.6)
        self.play(ShowCreation(area))
        self.play(Write(area_text), Write(text))
        self.wait()
        # self.remove(area)

    def show_mid_area(self, tangle1, tangle2, tangle3, tangle4, text):
        area = Polygon(
            tangle1[0].get_start(),
            tangle2[0].get_start(),
            tangle3[0].get_start(),
            tangle4[0].get_start(),
        ).set_stroke(width=5).set_color(BLUE_A).set_fill(BLUE_A, opacity=0.5)
        area_text = Tex("c²").set_color(YELLOW).move_to(area.get_center()).scale(0.6)
        self.play(ShowCreation(area))
        self.play(Write(area_text), Write(text))
        self.wait()
        # self.remove(area)


class Test2(Scene):
    def construct(self):
        title = Title("赵爽弦图证法").scale(0.9)
        self.add(title)
        x = 2
        y = 3.6
        tangle, real_tangle, a, b, c, text1, text2, text3, formula1 = init_tangle_with_number(x, y)
        self.play(ShowCreation(tangle))
        self.play(Write(formula1))
        self.remove(text1, text2, text3, formula1)
        self.play(
            real_tangle.scale, 0.8,
            real_tangle.shift, LEFT * 4 + DOWN * 0.5,
        )
        self.play(
            Rotate(
                real_tangle, angle=(PI / 2 + math.atan(x / y)),
            )
        )
        tex = add_indicator(real_tangle)
        self.play(Write(tex[0]), Write(tex[1]), Write(tex[2]))

        copy1 = self.show_copy(real_tangle)
        copy2 = self.show_copy(copy1)
        copy3 = self.show_copy(copy2)
        tex1 = add_indicator(copy1)
        tex2 = add_indicator(copy2)
        tex3 = add_indicator(copy3)
        self.play(
            Write(tex1[0]), Write(tex1[1]), Write(tex1[2]),
            Write(tex2[0]), Write(tex2[1]), Write(tex2[2]),
            Write(tex3[0]), Write(tex3[1]), Write(tex3[2]),
        )
        formula1 = Tex("c²").set_color(BLUE_A).next_to(copy2, RIGHT * 2)
        self.show_square_area(real_tangle, copy2, formula1)
        self.play(formula1.shift, UP * 0.8)
        formula2 = Tex("ab/2 ", "+ ab/2 ", "+ ab/2", "+ ab/2 ", "+ (b-a)² ", "= a² + b²").set_color(BLUE_A).scale(
            0.6).next_to(copy2, RIGHT * 2)
        self.show_tangle_area(real_tangle, formula2[0])
        self.show_tangle_area(copy1, formula2[1])
        self.show_tangle_area(copy2, formula2[2])
        self.show_tangle_area(copy3, formula2[3])
        self.show_mid_area(real_tangle, copy1, copy2, copy3, formula2[4])
        self.play(Write(formula2[5]))
        self.play(formula2.shift, UP * 0.1)

        arrow = Line(formula2.get_bottom() + DOWN * 0.2, formula2.get_bottom() + DOWN * 0.8)
        arrow.add_tip(width=0.16, length=0.16)
        self.play(ShowCreation(arrow))
        formula3 = Tex("c² = a² + b²").set_color(BLUE_A).next_to(arrow, DOWN * 0.2)
        self.play(Write(formula3))

    def show_copy(self, last_tangle):
        copy_tangle = last_tangle.copy().set_stroke(width=4).set_color(BLUE_A)
        self.play(ShowCreation(copy_tangle))
        temp = copy_tangle.copy()
        temp.rotate(PI / 2)
        temp.shift(last_tangle[0].get_start() - temp[1].get_end())
        temp.set_color(BLACK)
        self.play(Transform(copy_tangle, temp))
        return copy_tangle

    def show_square_area(self, tangle1, tangle3, text):
        size = tangle1[2].get_length()
        origin = (tangle1[1].get_start() + tangle3[1].get_start()) / 2
        square = Square(side_length=size).set_stroke(width=5).set_color(BLUE_A).move_to(origin)
        square.set_fill(BLUE_A, opacity=0.5)
        self.play(ShowCreation(square))
        square_text = Tex("c²").set_color(YELLOW).move_to(origin)
        self.play(Write(square_text), Write(text))
        self.remove(square, square_text)

    def show_tangle_area(self, tangle, text) -> None:
        area = Polygon(
            tangle[0].get_start(),
            tangle[1].get_start(),
            tangle[2].get_start(),
        ).set_stroke(width=5).set_color(BLUE_A).set_fill(BLUE_A, opacity=0.5)
        area_text = Tex("ab/2").set_color(YELLOW).move_to(
            (tangle[0].get_center() + tangle[1].get_center()) / 2).scale(0.6)
        self.play(ShowCreation(area))
        self.play(Write(area_text), Write(text))
        self.wait()
        # self.remove(area)

    def show_mid_area(self, tangle1, tangle2, tangle3, tangle4, text):
        area = Polygon(
            tangle1[0].get_end(),
            tangle2[0].get_end(),
            tangle3[0].get_end(),
            tangle4[0].get_end(),
        ).set_stroke(width=5).set_color(BLUE_A).set_fill(BLUE_A, opacity=0.5)
        area_text = Tex("(b-a)²").set_color(YELLOW).scale(0.6).move_to(area.get_center())
        self.play(ShowCreation(area))
        self.play(Write(area_text), Write(text))
        self.wait()
        # self.remove(area)


class Test3(Scene):
    def construct(self):
        title = Title("刘徽证法").scale(0.9)
        self.add(title)

        tangle, real_tangle, a, b, c, text1, text2, text3, formula1 = init_tangle_with_number(1.5, 4.5)
        self.play(ShowCreation(tangle))
        self.play(Write(formula1))
        group = VGroup(tangle, formula1)
        self.play(
            group.shift, LEFT * 6 + UP * 2,
            group.scale, 0.7,
        )

        x = real_tangle[0].get_length()
        y = real_tangle[1].get_length()

        square_y = Square(side_length=y).set_stroke(width=5).set_color(BLACK).shift(DOWN)
        self.play(ShowCreation(square_y))
        self.play(
            Write(Tex("b").set_color(RED).scale(0.7).next_to(square_y, UP * 0.1)),
            Write(Tex("b").set_color(RED).scale(0.7).next_to(square_y, DOWN * 0.1)),
            Write(Tex("b").set_color(RED).scale(0.7).next_to(square_y, LEFT * 0.1)),
            Write(Tex("b").set_color(RED).scale(0.7).next_to(square_y, RIGHT * 0.1)),
        )

        origin_x = square_y.get_center() + LEFT * (y - x) / 2 + UP * (x + y) / 2
        square_x = Square(side_length=x).set_stroke(width=5).set_color(BLACK).move_to(origin_x)
        self.play(ShowCreation(square_x))
        self.play(
            Write(Tex("a").set_color(BLUE).scale(0.7).next_to(square_x, UP * 0.1)),
            Write(Tex("a").set_color(BLUE).scale(0.7).next_to(square_x, DOWN * 0.1)),
            Write(Tex("a").set_color(BLUE).scale(0.7).next_to(square_x, LEFT * 0.1)),
            Write(Tex("a").set_color(BLUE).scale(0.7).next_to(square_x, RIGHT * 0.1)),
        )

        left_up_point = square_x.get_corner(UL)
        right_up_point = square_y.get_corner(UR)
        dash_line1 = DashedLine(left_up_point, right_up_point).set_color(BLUE_A)
        self.play(ShowCreation(dash_line1))
        dash_line2 = DashedLine(right_up_point, square_y.get_corner(DR) + LEFT * x).set_color(BLUE_A)
        self.play(ShowCreation(dash_line2))
        dash_line3 = DashedLine(square_y.get_corner(DR) + LEFT * x,
                                square_y.get_corner(DL) + LEFT * x + UP * x).set_color(BLUE_A)
        self.play(ShowCreation(dash_line3))
        dash_line4 = DashedLine(square_y.get_corner(DL) + LEFT * x + UP * x, left_up_point).set_color(BLUE_A)
        self.play(ShowCreation(dash_line4))

        self.play(
            Write(Tex("c").set_color(YELLOW).scale(0.7).next_to(dash_line1, OUT)),
            Write(Tex("c").set_color(YELLOW).scale(0.7).next_to(dash_line2, OUT)),
            Write(Tex("c").set_color(YELLOW).scale(0.7).next_to(dash_line3, OUT)),
            Write(Tex("c").set_color(YELLOW).scale(0.7).next_to(dash_line4, OUT)),
        )

        angle1 = math.atan(x / y)
        arc1 = Sector(outer_radius=0.8, angle=angle1, start_angle=3 / 2 * PI - angle1,
                      fill_color=YELLOW, fill_opacity=0.5,
                      arc_center=square_x.get_corner(UL))
        self.play(ShowCreation(arc1))
        arc2 = Sector(outer_radius=0.8, angle=angle1, start_angle=3 / 2 * PI - angle1,
                      fill_color=YELLOW, fill_opacity=0.5,
                      arc_center=square_y.get_corner(UR))
        self.play(ShowCreation(arc2))

        area1 = Polygon(
            square_x.get_corner(UL),
            square_y.get_corner(DL) + LEFT * x + UP * x,
            square_y.get_corner(DL) + UP * x
        ).set_fill(GREEN_A, opacity=0.5).set_stroke(width=5)
        self.play(ShowCreation(area1))
        area2 = Polygon(
            square_y.get_corner(UR),
            square_y.get_corner(DR) + LEFT * x,
            square_y.get_corner(DR)
        ).set_fill(GREEN_A, opacity=0.5).set_stroke(width=5)
        self.play(ShowCreation(area2))
        self.wait()

        area3 = Polygon(
            square_y.get_corner(DL) + LEFT * x + UP * x,
            square_y.get_corner(DL) + UP * x,
            square_y.get_corner(DL) + UP * x + DOWN * x * x / y,
        ).set_fill(GREY_A, opacity=0.5).set_stroke(width=5)
        self.play(ShowCreation(area3))
        area4 = Polygon(
            square_x.get_corner(UL),
            square_x.get_corner(UL) + RIGHT * x,
            square_x.get_corner(UL) + RIGHT * x + DOWN * x * x / y,
        ).set_fill(GREY_A, opacity=0.5).set_stroke(width=5)
        self.play(ShowCreation(area4))

        area5 = Polygon(
            square_x.get_corner(UL) + RIGHT * x + DOWN * x * x / y,
            square_x.get_corner(DR),
            square_y.get_corner(UR),
        ).set_fill(RED_A, opacity=0.5).set_stroke(width=5)
        self.play(ShowCreation(area5))
        area6 = Polygon(
            square_y.get_corner(DL) + UP * x + DOWN * x * x / y,
            square_y.get_corner(DL),
            square_y.get_corner(DL) + RIGHT * (y - x),
        ).set_fill(RED_A, opacity=0.5).set_stroke(width=5)
        self.play(ShowCreation(area6))

        formula2 = Tex("a^2+b^2=c^2").scale(0.8).next_to(square_y, RIGHT * 2).shift(UP * 0.5)
        self.play(Write(formula2))


class Test4(Scene):
    def construct(self):
        title = Title("毕达哥斯拉证法").scale(0.9)
        self.add(title)
        tangle = init_tangle_with_number(3.6, 2)[1]
        tangle.rotate(math.atan(3.6 / 2) + PI).move_to(ORIGIN)
        self.play(ShowCreation(tangle))

        self.play(
            tangle.scale, 0.65,
            tangle.shift, LEFT * 2 + DOWN * 0.4,
        )

        point_b = tangle[0].get_start()
        point_a = tangle[1].get_end()
        point_c = tangle[1].get_start()
        self.play(
            Write(Tex("B").scale(0.6).next_to(point_b, OUT)),
            Write(Tex("A").scale(0.6).next_to(point_a, OUT)),
            Write(Tex("C").scale(0.6).next_to(point_c, OUT))
        )
        a = tangle[1].get_length()
        b = tangle[0].get_length()

        print(a, b)

        point_h = point_c + tangle[0].get_vector() * a / b
        point_f = point_a + tangle[0].get_vector() * a / b
        area1 = Polygon(
            point_a,
            point_c,
            point_h,
            point_f,
        ).set_fill(GREEN_A, opacity=0.5).set_stroke(width=3)
        self.play(ShowCreation(area1))
        self.play(
            Write(Tex("H").scale(0.6).move_to(point_h)),
            Write(Tex("F").scale(0.6).move_to(point_f))
        )

        point_g = point_b - tangle[1].get_vector() * b / a
        point_k = point_c - tangle[1].get_vector() * b / a

        area2 = Polygon(
            point_c,
            point_b,
            point_g,
            point_k,
        ).set_fill(YELLOW, opacity=1).set_stroke(width=3)
        self.play(ShowCreation(area2))
        self.play(
            Write(Tex("G").scale(0.6).move_to(point_g)),
            Write(Tex("K").scale(0.6).move_to(point_k))
        )

        point_d = point_b + DOWN * math.sqrt(a ** 2 + b ** 2)
        point_e = point_a + DOWN * math.sqrt(a ** 2 + b ** 2)
        area3 = Polygon(
            point_a,
            point_b,
            point_d,
            point_e,
        ).set_fill(RED, opacity=1).set_stroke(width=3)
        self.play(ShowCreation(area3))
        self.play(
            Write(Tex("D").scale(0.6).move_to(point_d)),
            Write(Tex("E").scale(0.6).move_to(point_e))
        )

        point_l = np.array((point_c[0], point_e[1], 0))
        dash_line1 = DashedLine(point_c, point_l).set_color(BLUE)
        self.play(ShowCreation(dash_line1))
        self.play(Write(Tex("L").scale(0.6).move_to(point_l)))

        bottom_angle_point = point_l + RIGHT * 0.2 + UP * 0.2
        self.play(
            ShowCreation(Line(bottom_angle_point, point_l + RIGHT * 0.2, color=BLACK)),
            ShowCreation(Line(bottom_angle_point, point_l + UP * 0.2, color=BLACK)),
        )

        point_m = np.array((point_c[0], point_a[1], 0))
        self.play(Write(Tex("M").scale(0.6).move_to(point_m)))

        text = Text("因为高度相等，所以面积相等").set_color(BLACK).scale(0.6).next_to(point_d, RIGHT * 2)
        self.play(Write(text))

        formula1 = Text("S∆AEL=S∆AML=S∆ACE").scale(0.7).next_to(point_g, RIGHT * 2)
        s_area = Polygon(
            point_a,
            point_e,
            point_l,
        ).set_fill(BLUE_C, opacity=1).set_stroke(width=3)
        area_cae = Polygon(
            point_c,
            point_a,
            point_e
        ).set_fill(BLUE_C, opacity=1).set_stroke(width=3)

        self.play(
            Write(formula1),
            FadeOut(text),
            ShowCreation(s_area),
        )

        self.play(Transform(s_area, area_cae))

        angle1 = math.atan(b / a)
        arc1 = Sector(outer_radius=0.4, angle=angle1 + PI / 2, start_angle=-PI / 2,
                      fill_color=YELLOW, fill_opacity=0.5,
                      arc_center=point_a)
        self.play(ShowCreation(arc1))

        arc2 = Sector(outer_radius=0.4, angle=angle1 + PI / 2, start_angle=0,
                      fill_color=YELLOW, fill_opacity=0.5,
                      arc_center=point_a)
        self.play(
            FadeOut(arc1, run_time=0.5),
            ShowCreation(arc2, run_time=1),
        )
        formula2 = Text("∠CAE = ∠EAB").scale(0.7).next_to(formula1, DOWN)
        self.play(Write(formula2))

        area_fab = Polygon(
            point_f,
            point_a,
            point_b
        ).set_fill(BLUE_C, opacity=1).set_stroke(width=3)

        self.play(Transform(s_area, area_fab), FadeOut(formula2), FadeOut(arc2))
        self.wait()

        area_afc = Polygon(
            point_a,
            point_f,
            point_c
        ).set_fill(BLUE_C, opacity=1).set_stroke(width=3)
        self.play(Transform(s_area, area_afc))

        self.wait()
        self.play(FadeOut(s_area))

        area_ael = Polygon(
            point_a,
            point_e,
            point_l
        ).set_fill(BLUE_C, opacity=1).set_stroke(width=3)

        self.play(
            ShowCreation(area_afc),
            ShowCreation(area_ael),
        ),

        area_aelm = Polygon(
            point_a,
            point_e,
            point_l,
            point_m,
        ).set_fill(GREEN, opacity=1).set_stroke(width=3)

        area_fach = Polygon(
            point_f,
            point_a,
            point_c,
            point_h,
        ).set_fill(GREEN, opacity=1).set_stroke(width=3)

        self.wait()
        self.play(
            Transform(area_afc, area_fach),
            Transform(area_ael, area_aelm),
        )

        formula3 = Text("S FACH=S AELM").scale(0.7).next_to(formula2, DOWN)
        self.play(Write(formula3))

        area_lmbd = Polygon(
            point_l,
            point_m,
            point_b,
            point_d,
        ).set_fill(YELLOW, opacity=1).set_stroke(width=3)
        self.play(ShowCreation(area_lmbd))
        formula4 = Text("S LMBD=S CBGK").scale(0.7).next_to(formula3, DOWN)
        self.play(Write(formula4))

        self.play(Write(Tex("a").scale(0.7).move_to((point_f + point_h) / 2)))
        self.play(Write(Tex("b").scale(0.7).move_to((point_k + point_g) / 2)))
        self.play(Write(Tex("c").scale(0.7).move_to((point_e + point_d) / 2)))

        arrow = Line(formula4.get_bottom() + DOWN * 0.2, formula4.get_bottom() + DOWN * 0.8)
        arrow.add_tip(width=0.16, length=0.16)
        self.play(ShowCreation(arrow))
        formula5 = Tex("c² = a² + b²").set_color(BLUE_A).scale(0.7).next_to(arrow, DOWN * 0.2)
        self.play(Write(formula5))
