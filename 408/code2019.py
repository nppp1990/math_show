import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from yj.math_show.common.utils.utils import get_rect2
from manimlib import *


class Subject19(Scene):
    def construct(self) -> None:
        # self.show_subject()
        data1, data2 = self.init_data()
        data_list1, arrow_list1, link_group1 = self.draw_link(["head", *data1])
        data_list2, arrow_list2, link_group2 = self.draw_link(["head", *data2])
        link_group2.shift(DOWN)
        link_group1.shift(UP)
        arrow = Line(UP * 0.7, DOWN * 0.7, stroke_width=25, color=YELLOW).add_tip(width=0.8, length=0.4).scale(0.7)
        # self.add(link_group1)
        self.play(ShowCreation(link_group1, run_time=2))
        self.wait(2)
        self.play(Transform(link_group1.copy(), link_group2), run_time=2)
        self.add(arrow)
        self.wait(2)
        rect1 = get_rect2(VGroup(data_list2[1], data_list2[2]), stroke_color=ORANGE, stroke_width=3, buff=0.1)
        rect2 = get_rect2(VGroup(data_list2[3], data_list2[4]), stroke_color=ORANGE, stroke_width=3, buff=0.1)
        rect3 = get_rect2(VGroup(data_list2[5], data_list2[6]), stroke_color=ORANGE, stroke_width=3, buff=0.1)
        self.play(ShowCreation(rect1))
        self.play(ShowCreation(rect2))
        self.play(ShowCreation(rect3))
        self.wait(4)
        arrow1 = Line(ORIGIN, UP * 0.7, color=YELLOW).add_tip(width=0.2, length=0.2).scale(0.7).next_to(
            data_list1[1], DOWN, buff=0.1)
        arrow2 = Line(ORIGIN, UP * 0.7, color=YELLOW).add_tip(width=0.2, length=0.2).scale(0.7).next_to(
            data_list1[7], DOWN, buff=0.1)
        # self.add(arrow1, arrow2)
        self.play(ShowCreation(arrow1), ShowCreation(arrow2))
        self.wait(1)
        self.play(Indicate(data_list2[1][1], scale_factor=1.6, color=GREEN))
        data_list2[1][1].set_color(GREEN)
        self.play(Indicate(data_list2[2][1], scale_factor=1.6, color=GREEN))
        data_list2[2][1].set_color(GREEN)
        self.wait(2)

        space = data_list1[2].get_center()[0] - data_list1[1].get_center()[0]
        self.play(
            arrow1.shift, RIGHT * space,
            arrow2.shift, LEFT * space
        )
        self.wait(1)
        self.play(Indicate(data_list2[3][1], scale_factor=1.6, color=GREEN))
        data_list2[3][1].set_color(GREEN)
        self.play(Indicate(data_list2[4][1], scale_factor=1.6, color=GREEN))
        data_list2[4][1].set_color(GREEN)

        self.wait(1)
        self.play(
            arrow1.shift, RIGHT * space,
            arrow2.shift, LEFT * space
        )
        self.wait(1)
        self.play(Indicate(data_list2[5][1], scale_factor=1.6, color=GREEN))
        data_list2[5][1].set_color(GREEN)
        self.play(Indicate(data_list2[6][1], scale_factor=1.6, color=GREEN))
        data_list2[6][1].set_color(GREEN)

        self.play(
            arrow1.shift, RIGHT * space,
            arrow2.shift, LEFT * space
        )
        self.play(Indicate(data_list2[7][1], scale_factor=1.6, color=GREEN))
        data_list2[7][1].set_color(GREEN)

        # self.wait(4)
        self.remove(rect1, rect2, rect3, arrow1, arrow2, arrow, link_group2)

        rect4 = get_rect2(VGroup(data_list1[5], data_list1[6], data_list1[7]),
                          stroke_color=ORANGE, stroke_width=3, buff=0.1)
        self.play(ShowCreation(rect4))
        # self.wait(2)
        arrow1 = Line(ORIGIN, UP * 0.7, color=GREEN).add_tip(width=0.2, length=0.2).scale(0.7).next_to(
            data_list1[0], DOWN, buff=0.1)
        text1 = Tex("p").set_color(GREEN).scale(0.7).next_to(arrow1, DOWN, buff=0.08)
        arrow2 = Line(ORIGIN, UP * 0.7, color=BLUE).add_tip(width=0.2, length=0.2).scale(0.7).next_to(
            data_list1[0], DOWN, buff=0.1)
        text2 = Tex("q").set_color(BLUE).scale(0.7).next_to(arrow2, DOWN, buff=0.08)
        self.add(arrow1, arrow2)
        self.wait(2)
        self.play(
            VGroup(arrow1, text1).shift, RIGHT * space,
            VGroup(arrow2, text2).shift, RIGHT * space * 2,
        )
        self.wait(1)
        self.play(
            VGroup(arrow1, text1).shift, RIGHT * space,
            VGroup(arrow2, text2).shift, RIGHT * space * 2,
        )
        self.wait(1)
        self.play(
            VGroup(arrow1, text1).shift, RIGHT * space,
            VGroup(arrow2, text2).shift, RIGHT * space * 2,
        )
        self.wait(1)
        self.play(
            VGroup(arrow2, text2).shift, RIGHT * space * 2,
        )
        self.wait(2)

    # def show_prove(self):

    def show_subject(self):
        title = Title("2019年408算法题").scale(0.9)
        self.add(title)
        subject = Text(
            "设线性表L=(A1，A2，A3，...，An-2，An-1，An)采用带头结点的单链表保存\n"
            "请设计一个空间复杂度为O(1)且时间上尽可能高效的算法，重新排列L中的各结点\n"
            "得到线性表L’ =(A1，An，A2，An-1，A3，An-2，...)")
        subject.scale(0.7)
        subject.set_color_by_text_to_color_map({
            "A1，A2，A3，...，An-2，An-1，An": "#449C47",
            "A1，An，A2，An-1，A3，An-2，...": "#449C47",
            "O(1)": YELLOW,
            "头结点": BLUE,
            # "单链表": BLUE,
            # "尽可能高效": BLUE
        })
        # self.play(Write(subject), run_time=10)
        self.add(subject)
        # self.wait(3)
        self.play(FadeOut(title),
                  subject.shift, UP * 3 + LEFT * 3,
                  subject.scale, 0.7)

    def init_data(self):
        data1 = ["A" + str(i + 1) for i in range(7)]
        i = 1
        data2 = []
        for i in range(1, 4):
            data2.append("A" + str(i))
            data2.append("A" + str(8 - i))
        data2.append("A4")
        return data1, data2

    def draw_link(self, link_data: []):
        pre = None
        link_list = []
        data_list = []
        arrow_list = []
        for data in link_data:
            data_item = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8,
                                         fill_opacity=1, fill_color=WHITE),
                               Text(data, color=BLACK, font="Menlo", font_size=30))
            if pre is not None:
                data_item.next_to(pre, buff=0)
            arrow = Line(ORIGIN, ORIGIN + RIGHT * 0.8).next_to(data_item, buff=0).add_tip(width=0.2, length=0.2)
            pre = arrow
            link_list.append(data_item)
            data_list.append(data_item)
            link_list.append(arrow)
            arrow_list.append(arrow)
        null_item = Text('NULL', font="Menlo", font_size=30).next_to(pre, buff=0)
        link_list.append(null_item)

        link_group = VGroup(*link_list).scale(0.7).shift(LEFT * 8.7)
        return data_list, arrow_list, link_group


class Test(Scene):
    def construct(self) -> None:
        data_item = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8,
                                     fill_opacity=1, fill_color=WHITE),
                           Text("xxxx", color=BLACK, font="Menlo", font_size=30))
        self.add(data_item)
        self.wait(1)
        data_item[0].set_fill(BLUE)
        p = Tex("p").set_color(GREEN).scale(0.8).next_to(data_item, DOWN, buff=0.07)
        self.add(p)
