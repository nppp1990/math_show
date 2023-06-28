import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.common.scene.link import create_link
from yj.common.utils.utils import get_rect2

color_map_quick = {
    "1.": "#A0A0A0",
    "2.": "#A0A0A0",
    "3.": "#A0A0A0",
    "4.": "#A0A0A0",
    "5.": "#A0A0A0",
    "6.": "#A0A0A0",
    "7.": "#A0A0A0",
    "8.": "#A0A0A0",
    "9.": "#A0A0A0",
    "10.": "#A0A0A0",
    "11.": "#A0A0A0",
    "12.": "#A0A0A0",
    "13.": "#A0A0A0",
    "14.": "#A0A0A0",
    "15.": "#A0A0A0",
    "16.": "#A0A0A0",
    "17.": "#A0A0A0",
    "18.": "#A0A0A0",
    "19.": "#A0A0A0",
    "20.": "#A0A0A0",
    "21.": "#A0A0A0",
    "22.": "#A0A0A0",
    "23.": "#A0A0A0",
    "24.": "#A0A0A0",
    "25.": "#A0A0A0",
    "26.": "#A0A0A0",
    "27.": "#A0A0A0",
    "28.": "#A0A0A0",
    "29.": "#A0A0A0",

    "/": "#808080",
    "node的next指向第一个元素": "#808080",
    "带结点为head的单链表插入node": "#808080",
    "删除单链表结点p": "#808080",
    "p存储结点1": "#808080",
    "需要获取p的前驱结点pre": "#808080",
    "pre的next指向p的next": "#808080",
    "LinkNode": "#803690",
    "next": "#803690",
    "NULL": "#2B5D39",
    "bool": "#000080",
    "while": "#000080",
    "int": "#000080",
    "if": "#000080",
    "else": "#000080",
    "return": "#000080",
    ";": "#000080",
    "void": "#000080",
    "delete": "#000080",
}


def create_code(text):
    code = Text(text, color=BLACK,
                font_size=30,
                slant=ITALIC,
                t2c=color_map_quick,
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map_quick)
    return code


class ErrorLink1(Scene):
    def construct(self) -> None:
        self.insert_tail()

    def insert_tail(self):
        title = Title("错误代码-单链表(带头结点)尾插").scale(0.9)
        self.add(title)

        code1 = create_code("1.  LinkNode *p = head->next;")
        code2 = create_code("2.  while (p) {")
        code3 = create_code("3.      p = p->next;")
        code4 = create_code("4.  }")
        code5 = create_code("5.  p->next = node;")

        code21 = create_code("1.  LinkNode *p = head->next;")
        code22 = create_code("2.  while (p->next) {")
        code23 = create_code("3.      p = p->next;")
        code24 = create_code("4.  }")
        code25 = create_code("5.  p->next = node;")

        code_group = VGroup(
            code1, code2, code3, code4, code5
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group.shift(DOWN)
        code_rect = get_rect2(code_group, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)
        self.add(code_rect)
        self.play(FadeIn(code_group))

        self.wait(9)
        group_list = create_link(['head', '1', '2'], ORIGIN, line_width=0.7, line_color=WHITE)[1]
        group_list[len(group_list) - 1].set_color(RED_B)
        link = VGroup(*group_list).move_to(ORIGIN).shift(UP * 1.5 + LEFT * 1.5)
        self.play(ShowCreation(link))
        size = len(group_list)

        node = create_link(['node'], ORIGIN, line_width=0.7, line_color=WHITE)[1][0][0].next_to(
            group_list[size - 1], buff=1)
        self.play(FadeIn(node))
        self.wait(2)

        rect1 = get_rect2(code1, stroke_color=ORANGE, stroke_width=3, buff=0.05).stretch(
            0.87, 0, about_edge=VGroup(code2, code3, code4).get_right())
        self.play(ShowCreation(rect1))
        p = Tex("p").set_color(BLUE_E).next_to(group_list[1][0], DOWN, buff=0.1).scale(0.8)
        self.play(ShowCreation(p))
        self.wait(2)

        unit1 = (code2.get_center()[1] - code1.get_center()[1]) * UP
        unit2 = group_list[1].get_center() - group_list[0].get_center()
        unit3 = group_list[size - 1].get_center() - group_list[size - 2].get_center()

        # 第一次循环
        self.play(rect1.shift, unit1)
        rect1.save_state()
        self.play(rect1.shift, unit1)
        self.play(p.shift, unit2)
        self.play(rect1.shift, unit1)

        # 第二次循环
        self.play(rect1.restore)
        rect1.save_state()
        self.play(rect1.shift, unit1)
        self.play(p.shift, unit3)
        self.play(rect1.shift, unit1)
        self.wait(3)

        # 第三次循环
        self.play(rect1.restore)
        self.play(rect1.shift, unit1 * 3)
        self.wait(2)

        arrow1 = Line(p.get_right(), node.get_left())
        arrow1.add_tip(width=0.2, length=0.2)
        self.play(ShowCreation(arrow1))

        error = SVGMobject("../../../assets/svg_images/error.svg", color=RED).scale(0.15).move_to(arrow1.get_center())
        self.play(FadeIn(error))
        self.wait(2)

        code_group2 = VGroup(
            code21, code22, code23, code24, code25
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group2.shift(DOWN)
        right_code = VGroup(get_rect2(code_group2, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                                      fill_color=WHITE), code_group2).shift(RIGHT * 4)

        arrow = Line(VGroup(code_rect, code_group).get_right() + RIGHT * 0.2 + LEFT * 4,
                     right_code.get_left() + LEFT * 0.2, stroke_width=10, color=YELLOW)
        arrow.add_tip(width=0.3, length=0.3)

        self.remove(rect1)
        self.play(VGroup(code_rect, code_group).shift, LEFT * 4)
        self.play(ShowCreation(arrow))
        self.play(FadeIn(right_code))
        self.wait(5)


class ErrorLink2(Scene):
    def construct(self) -> None:
        title = Title("错误代码-单链表(带头结点)头插").scale(0.9)
        self.add(title)

        code1 = create_code("1.  // 带结点为head的单链表插入node")
        code2 = create_code("2.  head->next = node;")
        code3 = create_code("3.  // node的next指向第一个元素")
        code4 = create_code("4.  node->next = head->next;")

        code21 = create_code("1.  // p存储结点1")
        code22 = create_code("2.  p = head->next;")
        code23 = create_code("3.  head->next = node;")
        code24 = create_code("4.  node->next = p;")

        code_group = VGroup(
            code1, code2, code3, code4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_rect = get_rect2(code_group, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)
        self.add(code_rect)
        self.play(FadeIn(code_group))

        self.wait(10)
        self.play(VGroup(code_rect, code_group).shift, DOWN * 1.8)

        group_list = create_link(['head', '1', '2'], ORIGIN, line_width=0.7, line_color=WHITE)[1]
        group_list[len(group_list) - 1].set_color(RED_B)
        link = VGroup(*group_list).move_to(ORIGIN).shift(UP * 1.5)
        self.play(ShowCreation(link))
        size = len(group_list)

        node = create_link(['node'], ORIGIN, line_width=0.7, line_color=WHITE)[1][0][0].next_to(
            group_list[0][1], DOWN, buff=1)
        self.play(FadeIn(node))
        self.wait(2)

        unit1 = (code2.get_center()[1] - code1.get_center()[1]) * UP
        rect1 = get_rect2(code4, stroke_color=ORANGE, stroke_width=3, buff=0.05).stretch(
            0.87, 0, about_edge=code4.get_right())
        rect1.shift(-unit1 * 2)
        self.play(ShowCreation(rect1))
        arrow1 = Line(group_list[0][0][1].get_bottom(), node[0].get_top())
        arrow1.add_tip(width=0.2, length=0.2)
        self.play(FadeOut(group_list[0][1], run_time=1), ShowCreation(arrow1, run_time=2))

        self.wait(2)

        self.play(rect1.shift, unit1 * 2)
        self.wait()
        self.play(Indicate(arrow1, scale_factor=1.1, color=YELLOW))
        rect2 = get_rect2(node, buff=0.01, stroke_color=RED_B, stroke_width=3)
        self.add(rect2)

        x = node[1].get_right()[0] - node[0].get_center()[0]
        arrow_child1 = Line(node[1].get_right(), node[1].get_right() + RIGHT * 0.2)
        arrow_child2 = Line(node[1].get_right() + RIGHT * 0.2, node[1].get_right() + RIGHT * 0.2 + DOWN * 0.8)
        arrow_child3 = Line(node[1].get_right() + RIGHT * 0.2 + DOWN * 0.8,
                            node[1].get_right() + RIGHT * 0.2 + DOWN * 0.8 + LEFT * (x + 0.2))
        arrow_child4 = Line(node[1].get_right() + RIGHT * 0.2 + DOWN * 0.8 + LEFT * (x + 0.2), node[0].get_bottom())
        arrow_child4.add_tip(width=0.2, length=0.2)
        self.play(ShowCreation(arrow_child1, run_time=0.3))
        self.play(ShowCreation(arrow_child2, run_time=0.5))
        self.play(ShowCreation(arrow_child3, run_time=0.8))
        self.play(ShowCreation(arrow_child4, run_time=0.3))
        error = SVGMobject("../../../assets/svg_images/error.svg", color=RED).scale(0.15).move_to(
            arrow_child3.get_center())
        self.play(FadeIn(error))

        self.wait(2)
        code_group2 = VGroup(code21, code22, code23, code24).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group2.shift(DOWN * 1.8)
        right_code = VGroup(get_rect2(code_group2, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                                      fill_color=WHITE), code_group2).shift(RIGHT * 4)

        arrow = Line(VGroup(code_rect, code_group).get_right() + RIGHT * 0.2 + LEFT * 3.8,
                     right_code.get_left() + LEFT * 0.2, stroke_width=10, color=YELLOW)
        arrow.add_tip(width=0.3, length=0.3)

        self.remove(rect1)
        self.play(VGroup(code_rect, code_group).shift, LEFT * 3.8)
        self.play(ShowCreation(arrow))
        self.play(FadeIn(right_code))
        self.wait(5)


class ErrorLink3(Scene):
    def construct(self) -> None:
        title = Title("错误代码-单链表删除结点").scale(0.9)
        self.add(title)
        code1 = create_code("1.  // 删除单链表结点p")
        code2 = create_code("2.  delete p;")

        code21 = create_code("1.  // 需要获取p的前驱结点pre")
        code22 = create_code("2.  // pre的next指向p的next")
        code23 = create_code("3.  pre->next=p->next")
        code24 = create_code("4.  delete p;")

        code_group = VGroup(code1, code2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_rect = get_rect2(code_group, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)

        self.add(code_rect)
        self.play(FadeIn(code_group))
        self.wait(10)

        self.play(VGroup(code_rect, code_group).shift, DOWN * 1.8)
        group_list = create_link(['1', '2', 'p', '4'], ORIGIN, line_width=0.7, line_color=WHITE)[1]
        group_list[len(group_list) - 1].set_color(RED_B)
        link = VGroup(*group_list).move_to(ORIGIN).shift(UP * 1.5)
        self.play(ShowCreation(link))

        self.wait(2)
        rect1 = get_rect2(code2, stroke_color=ORANGE, stroke_width=3, buff=0.05).stretch(
            0.7, 0, about_edge=code2.get_right())
        self.play(ShowCreation(rect1))
        self.wait()
        self.play(FadeOut(group_list[2]))
        self.wait()
        error = SVGMobject("../../../assets/svg_images/error.svg", color=RED).scale(0.15).move_to(
            group_list[1][1].get_center())
        self.play(FadeIn(error))
        self.wait(2)

        code_group2 = VGroup(code21, code22, code23, code24).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group2.shift(DOWN * 1.8)
        right_code = VGroup(get_rect2(code_group2, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                                      fill_color=WHITE), code_group2).shift(RIGHT * 4)

        arrow = Line(VGroup(code_rect, code_group).get_right() + RIGHT * 0.3 + LEFT * 3.8,
                     right_code.get_left() + LEFT * 0.3, stroke_width=10, color=YELLOW)
        arrow.add_tip(width=0.3, length=0.3)

        self.remove(rect1)
        self.play(VGroup(code_rect, code_group).shift, LEFT * 3.8)
        self.play(ShowCreation(arrow))
        self.play(FadeIn(right_code))
        self.wait(5)


class ErrorLink4(Scene):
    def construct(self) -> None:
        title = Title("错误代码-单链表遍历打印").scale(0.9)
        self.add(title)
        code1 = create_code("1.  LinkNode *p = head;")
        code2 = create_code("2.  while (p) {")
        code3 = create_code("3.      p = p->next;")
        code4 = create_code("4.      printf(p->data);")
        code5 = create_code("5.  }")

        code21 = create_code("1.  LinkNode *p = head->next;")
        code22 = create_code("2.  while (p) {")
        code23 = create_code("3.      printf(p->data);")
        code24 = create_code("4.      p = p->next;")
        code25 = create_code("5.  }")

        code_group = VGroup(code1, code2, code3, code4, code5).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_rect = get_rect2(code_group, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)
        self.add(code_rect)
        self.play(FadeIn(code_group))
        self.wait(10)

        self.play(VGroup(code_rect, code_group).shift, DOWN * 1.5)
        group_list = create_link(['head', '1', '2', '3'], ORIGIN, line_width=0.7, line_color=WHITE)[1]
        group_list[len(group_list) - 1].set_color(RED_B)
        link = VGroup(*group_list).move_to(ORIGIN).shift(UP * 1.5)
        self.play(ShowCreation(link))

        p = Tex("p").set_color(BLUE_E).next_to(group_list[0][0], DOWN, buff=0.1).scale(0.8)
        self.play(ShowCreation(p))
        self.wait(1)

        size = len(group_list)
        unit1 = (code2.get_center()[1] - code1.get_center()[1]) * UP
        unit2 = group_list[1].get_center() - group_list[0].get_center()
        unit3 = group_list[size - 1].get_center() - group_list[size - 2][0].get_center()
        rect1 = get_rect2(code4, stroke_color=ORANGE, stroke_width=3, buff=0.05).stretch(
            0.84, 0, about_edge=code4.get_right())
        rect1.shift(-unit1 * 2)
        self.play(ShowCreation(rect1))
        rect1.save_state()
        for i in range(1, size - 1):
            self.play(rect1.restore)
            rect1.save_state()
            self.play(rect1.shift, unit1)
            self.play(p.shift, unit2)
            self.play(rect1.shift, unit1)
            self.play(group_list[i][0][0][1].set_color, GREEN)
            self.play(rect1.shift, unit1)
        self.wait(3)
        self.play(rect1.restore)
        self.play(rect1.shift, unit1)
        self.play(p.shift, unit3)
        self.play(rect1.shift, unit1)

        self.wait(2)
        error = SVGMobject("../../../assets/svg_images/error.svg", color=RED).scale(0.15).move_to(
            code4.get_center()).shift(DOWN * 0.2 + RIGHT * 0.5)
        self.play(FadeIn(error))

        self.wait(2)
        code_group2 = VGroup(code21, code22, code23, code24, code25).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group2.shift(DOWN * 1.5)
        right_code = VGroup(get_rect2(code_group2, buff=0.2, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                                      fill_color=WHITE), code_group2).shift(RIGHT * 4)

        arrow = Line(VGroup(code_rect, code_group).get_right() + RIGHT * 0.3 + LEFT * 3.8,
                     right_code.get_left() + LEFT * 0.3, stroke_width=10, color=YELLOW)
        arrow.add_tip(width=0.3, length=0.3)

        self.remove(rect1, error)
        self.play(VGroup(code_rect, code_group).shift, LEFT * 3.8)
        self.play(ShowCreation(arrow))
        self.play(FadeIn(right_code))
        self.wait(5)
