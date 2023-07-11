import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.math_show.common.scene.link import create_link
from yj.math_show.common.utils.utils import get_rect2

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
    "遍历单链表，找到最后一个结点": "#808080",
    "只要p的next不为空，就向后前进": "#808080",
    "p记录链表之前的第一个元素": "#808080",
    "head的next指向新nodeX，nodeX变为新的第一个元素": "#808080",
    "nodeX的next指向p防止“断链”": "#808080",
    "新插入的结点next指向原先的头指针h": "#808080",
    "链表新的头指针为nodeX": "#808080",
    "更新头指针h": "#808080",
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
}


def create_code(text):
    code = Text(text, color=BLACK,
                font_size=20,
                slant=ITALIC,
                t2c=color_map_quick,
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map_quick)
    return code


class Head(Scene):
    def construct(self) -> None:
        self.wait(5)


class Link1(Scene):
    def construct(self) -> None:
        title = Title("单链表插入").scale(0.9)
        self.add(title)

        node_list, group_list = create_link(['head', 1, 2, 3], ORIGIN + LEFT * 4, line_width=0.7, line_color=WHITE)
        group_list[len(group_list) - 1].set_color(RED_B)
        link = VGroup(*group_list).scale(0.8).shift(LEFT * 2.5 + UP * 2)
        self.play(FadeIn(link, run_time=2))
        self.show_link1(group_list, title)
        self.show_link2(group_list, title)
        self.show_link3(group_list, title)

    def show_link1(self, group_list, title):
        code1 = create_code("1.  void insertNode(LinkNode *head, LinkNode *nodeX) {")
        code2 = create_code("2.      LinkNode *p = head;")
        code3 = create_code("3.      // 遍历单链表，找到最后一个结点")
        code4 = create_code("4.      while (p->next) {")
        code5 = create_code("5.          // 只要p的next不为空，就向后前进")
        code6 = create_code("6.          p = p->next;")
        code7 = create_code("7.      }")
        code8 = create_code("8.      p->next = nodeX;")
        code9 = create_code("9.      nodeX->next = NULL;")
        code10 = create_code("10. }")

        code_group = VGroup(
            code1, code2, code3, code4, code5, code6, code7, code8, code9, code10,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group.shift(DOWN * 1.5)
        code_rect = get_rect2(code_group, buff=0.1, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)

        # self.wait()
        self.play(
            Transform(title, Title("单链表插入-尾插法")),
            FadeIn(code_rect)
        )
        self.play(Write(code1))
        self.wait()

        point_arrow_line = Line(ORIGIN, ORIGIN + UP * 0.6, stroke_width=7).next_to(
            group_list[0][0], direction=DOWN, buff=0.1)
        point_arrow_line.add_tip(width=0.2, length=0.2)
        p_text = Tex("p").next_to(point_arrow_line, DOWN, buff=0.05).scale(0.6)
        point = VGroup(point_arrow_line, p_text)
        self.play(FadeIn(point))
        self.play(Write(code2))
        self.wait(2)

        unit = group_list[1].get_center()[0] - group_list[0].get_center()[0]
        for i in range(len(group_list) - 2):
            self.play(point.shift, RIGHT * unit)
        self.play(Write(code3))
        self.play(Write(code4))
        self.play(Write(code5))
        self.play(Write(code6))
        self.play(Write(code7))

        self.wait(2)
        last_g = group_list[len(group_list) - 2]
        old_arrow = last_g[1]
        node = create_link(['X'], ORIGIN, line_width=0.7, line_color=WHITE)[1][0].scale(0.8)
        node.shift(UP * 1 + RIGHT * 3.3)
        self.play(ShowCreation(node[0]))
        self.wait(2)

        null_text = group_list[len(group_list) - 1].copy()
        self.remove(old_arrow, group_list[len(group_list) - 1])
        arrow = Line(old_arrow.get_left(), node[0][0].get_top())
        arrow.add_tip(width=0.16, length=0.16)
        self.play(ShowCreation(arrow))
        self.play(Write(code8))

        self.wait(2)
        null_text.next_to(node[1], buff=0)
        self.play(ShowCreation(node[1]))
        self.play(ShowCreation(null_text))
        self.play(Write(code9))
        self.play(Write(code10))
        self.wait(3)

        self.play(FadeOut(point),
                  FadeOut(node),
                  FadeOut(null_text),
                  FadeOut(code_group),
                  FadeOut(code_rect),
                  FadeOut(arrow),
                  )
        self.add(old_arrow, group_list[len(group_list) - 1])

    def show_link2(self, group_list, title):
        self.play(Transform(title, Title("单链表插入-头插法")))
        self.wait(2)
        code1 = create_code("1.  void insertNode(LinkNode *head, LinkNode *nodeX) {")
        code2 = create_code("2.      // p记录链表之前的第一个元素")
        code3 = create_code("3.      LinkNode *p = head->next;")
        code4 = create_code("4.      // head的next指向新nodeX，nodeX变为新的第一个元素")
        code5 = create_code("5.      head->next = nodeX;")
        code6 = create_code("6.      // nodeX的next指向p防止“断链”")
        code7 = create_code("7.      nodeX->next = p;")
        code8 = create_code("8.  }")
        code_group = VGroup(
            code1, code2, code3, code4, code5, code6, code7, code8
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group.shift(DOWN * 1.5)
        code_rect = get_rect2(code_group, buff=0.1, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)

        node = create_link(['X'], ORIGIN, line_width=0.7, line_color=WHITE)[1][0].scale(0.8)[0]
        old_arrow = group_list[0][1]
        p_head = group_list[0][0]
        node.move_to(old_arrow.get_center() + DOWN)
        self.play(FadeIn(node))
        self.play(FadeIn(code_rect))
        self.play(Write(code1))

        self.wait()

        indicate = get_rect2(group_list[1][0], buff=0.01, stroke_color=RED_B, stroke_width=3)
        self.play(ShowCreation(indicate))
        p = Tex("p").set_color(BLUE_E).scale(0.7).move_to(group_list[1][0].get_bottom())
        self.play(ShowCreation(p))
        self.remove(indicate)
        self.play(Write(code2))
        self.play(Write(code3))

        arrow1 = Line(p_head[1].get_bottom(), node[0].get_top())
        arrow1.add_tip(width=0.16, length=0.16)

        arrow2 = Line(node[1].get_top(), group_list[1][0][0].get_bottom())
        arrow2.add_tip(width=0.16, length=0.16)

        self.wait(2)
        self.play(FadeOut(old_arrow), ShowCreation(arrow1))
        self.play(Write(code4))
        self.play(Write(code5))

        self.wait(2)
        self.play(ShowCreation(arrow2))
        self.play(Write(code6))
        self.play(Write(code7))
        self.play(Write(code8))
        self.wait(3)
        self.play(
            FadeOut(code_rect),
            FadeOut(code_group),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(node),
            FadeOut(p),
            FadeIn(old_arrow)
        )

    def show_link3(self, group_list, title):
        code1 = create_code("1.  LinkNode* insertNode(LinkNode *h, LinkNode *nodeX) {")
        code2 = create_code("2.      // 新插入的结点next指向原先的头指针h")
        code3 = create_code("3.      nodeX->next = h;")
        code4 = create_code("4.      // 链表新的头指针为nodeX")
        code5 = create_code("5.      return nodeX;")
        code6 = create_code("6.  }")
        code7 = create_code("7.  // 更新头指针h")
        code8 = create_code("8.  h = insertNode(h, nodeX);")
        code_group = VGroup(
            code1, code2, code3, code4, code5, code6, code7, code8
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code_group.shift(DOWN * 1.5)
        code_rect = get_rect2(code_group, buff=0.1, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)

        self.play(Transform(title, Title("不带头结点的单链表插入-头插法")))
        self.wait(2)

        head = Tex("h").set_color(BLUE_E).scale(0.7).move_to(group_list[1][0].get_bottom())
        self.play(FadeOut(group_list[0]), ShowCreation(head))

        node = create_link(['X'], ORIGIN, line_width=0.7, line_color=WHITE)[1][0].scale(0.8)[0]
        node.move_to(group_list[0][0].get_center() + DOWN)
        self.play(ShowCreation(node))
        self.play(FadeIn(code_rect))
        self.play(Write(code1))

        self.wait(2)
        arrow1 = Line(node[1].get_right(), group_list[1][0][0].get_left())
        arrow1.add_tip(width=0.16, length=0.16)
        self.play(ShowCreation(arrow1))
        self.play(Write(code2))
        self.play(Write(code3))

        self.wait(3)
        self.play(Write(code4))
        self.play(Write(code5))
        self.play(Write(code6))
        self.wait(2)
        indicate = get_rect2(node, buff=0.01, stroke_color=RED_B, stroke_width=3)
        self.play(ShowCreation(indicate))
        self.play(head.move_to, node.get_bottom() + DOWN * 0.2)
        self.remove(indicate)
        self.play(Write(code7))
        self.play(Write(code8))
