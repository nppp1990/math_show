import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.common.scene.link import create_link
from yj.common.scene.link import create_link2
from yj.common.utils.utils import get_rect2
from yj.common.utils.utils import get_del_line

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
    "遍历单链表并反转": "#808080",
    "p2的next指向p1": "#808080",
    "p1前进一位：p1变为p2": "#808080",
    "p2前进一位：p2变为p2的next": "#808080",
    "p2前进一位：p2变为temp": "#808080",
    "temp存储p2的next": "#808080",
    "第一个结点的next指向NULL": "#808080",
    "返回新链表的head": "#808080",
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
                font_size=28,
                slant=ITALIC,
                t2c=color_map_quick,
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map_quick)
    return code


class LinkReverse(Scene):
    def construct(self) -> None:
        title = Title("单链表反转").scale(0.9)
        self.add(title)

        group_list = create_link2(['A1', 'A2', 'A3', 'A4'], ORIGIN, line_width=0.9, line_color="#E6D0DE")
        group_list[len(group_list) - 1].set_color(RED_B)
        link = VGroup(*group_list).move_to(ORIGIN).shift(UP * 1.5).scale(0.9)
        self.play(ShowCreation(link))
        size = len(group_list)

        group_list2 = create_link2(['A4', 'A3', 'A2', 'A1'], ORIGIN, line_width=0.9, line_color="#E6D0DE")
        group_list2[len(group_list2) - 1].set_color(RED_B)
        link2 = VGroup(*group_list2).move_to(ORIGIN).shift(DOWN * 0.5).scale(0.9)
        arrow = Line(link.get_center() + DOWN * 0.4, link2.get_center() + UP * 0.4, stroke_width=16, color=YELLOW)
        arrow.add_tip(width=0.4, length=0.4)

        self.wait(2)
        self.play(ShowCreation(arrow))
        self.wait(0.5)
        self.play(FadeIn(link2))

        self.wait(6)
        self.remove(link2, arrow)

        self.play(link.shift, RIGHT * (group_list[0][1].get_width() + group_list[size - 1].get_width()))
        link.save_state()

        unit1 = group_list[1].get_center() - group_list[0].get_center()
        unit2 = group_list[size - 1].get_center() - group_list[size - 2][0].get_center()
        p1 = Tex("p1").next_to(group_list[0][0], DOWN, buff=0.15).set_color(BLUE_A).scale(0.5).shift(-unit2)
        p2 = Tex("p2").next_to(group_list[0][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        last_null = group_list[size - 1].copy().next_to(group_list[0], LEFT, group_list[0][1].get_width())
        for i in range(size - 1):
            if i == 0:
                self.play(Write(p1), Write(p2), FadeIn(last_null))
            elif i == 1:
                self.play(p1.shift, unit2,
                          p2.shift, unit1)
            else:
                self.play(p1.shift, unit1,
                          p2.shift, unit1)

            current = group_list[i]
            cur_node = current[0]
            cur_point = current[1]
            item_rect = get_rect2(cur_node, buff=0.08, stroke_color=YELLOW, stroke_width=2)
            self.play(ShowCreation(item_rect))
            self.wait()
            if i == size - 2:
                self.play(FadeOut(cur_point), FadeOut(group_list[size - 1]))
            else:
                self.play(FadeOut(cur_point))

            cur_point.shift(-unit1)
            cur_point.rotate(PI)
            self.play(ShowCreation(cur_point))
            self.remove(item_rect)

        self.play(p1.shift, unit1,
                  p2.shift, unit2)

        self.wait(2)
        self.remove(p1, p2, last_null)
        self.play(link.restore, run_time=2)
        self.play(link.shift, UP * 0.6)
        title2 = Title("单链表反转-错误代码1").scale(0.9)
        self.play(Transform(title, title2))
        self.show_code1(link)
        self.show_code2(link, title)
        self.show_perfect_code(link)

    def show_code1(self, link):
        link.save_state()
        code1 = create_code("1.  // 遍历单链表并反转")
        code2 = create_code("2.  while (p2) {")
        code3 = create_code("3.      // p2的next指向p1")
        code4 = create_code("4.      p2->next = p1;")
        code5 = create_code("5.      // p1前进一位：p1变为p2")
        code6 = create_code("6.      p1 = p2;")
        code7 = create_code("7.      // p2前进一位：p2变为p2的next")
        code8 = create_code("8.      p2 = p2->next;")
        code9 = create_code("9.  }")
        code_group = VGroup(code1, code2, code3, code4, code5, code6, code7, code8, code9).arrange(
            DOWN, aligned_edge=LEFT, buff=0.07).shift(DOWN * 1.2)
        code_rect = get_rect2(code_group, buff=0.15, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                              fill_color=WHITE)

        code21 = create_code("1.  while (p2) {")
        code22 = create_code("2.      // temp存储p2的next")
        code23 = create_code("3.      LinkNode *temp = p2->next;")
        code24 = create_code("4.      p2->next = p1;")
        code25 = create_code("5.      // p1前进一位：p1变为p2")
        code26 = create_code("6.      p1 = p2;")
        code27 = create_code("7.      // p2前进一位：p2变为temp")
        code28 = create_code("8.      p2 = temp;")
        code29 = create_code("9.  }")

        self.play(FadeIn(code_rect, run_time=0.5))
        self.play(FadeIn(code_group))
        p1 = Tex("p1").next_to(link[0][0], DOWN, buff=0.15).set_color(BLUE_A).scale(0.5)
        p2 = Tex("p2").next_to(link[1][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        self.play(Write(p1, run_time=0.5), Write(p2, run_time=0.5))

        link_unit = link[1].get_center() - link[0].get_center()
        code_unit = (code2.get_center()[1] - code1.get_center()[1]) * UP
        rect1 = get_rect2(code4, stroke_color=ORANGE, stroke_width=3, buff=0.05).stretch(
            0.64, 0, about_point=code4.get_right())
        self.play(ShowCreation(rect1))
        point = link[1][1]

        self.play(FadeOut(point))
        point.set_color(YELLOW)
        point.shift(-link_unit)
        point.rotate(PI)
        self.play(ShowCreation(point, run_time=2))

        self.play(rect1.shift, code_unit * 2)
        self.play(p1.shift, link_unit + DOWN * 0.3)

        self.play(rect1.shift, code_unit * 2)
        self.play(Indicate(point, scale_factor=1.1, color=YELLOW))
        a_rect1 = get_rect2(link[0][0], buff=0.05, stroke_color=RED, stroke_width=2)
        self.play(ShowCreation(a_rect1))
        self.play(p2.shift, -link_unit)

        self.wait(12)
        self.remove(rect1, p1, p2, a_rect1)
        self.play(VGroup(code_rect, code_group).shift, LEFT * 4)

        code_group2 = VGroup(code21, code22, code23, code24, code25, code26, code27, code28, code29).arrange(
            DOWN, aligned_edge=LEFT, buff=0.07).shift(DOWN * 1.2 + RIGHT * 4)
        right_code = VGroup(get_rect2(code_group2, buff=0.15, stroke_color=BLACK, stroke_width=2, fill_opacity=1,
                                      fill_color=WHITE), code_group2)
        arrow = Line(code_rect.get_right() + RIGHT * 0.1, right_code.get_left() + LEFT * 0.1,
                     stroke_width=10, color=YELLOW).add_tip(width=0.3, length=0.3)
        self.play(ShowCreation(arrow))
        self.play(FadeIn(right_code), link.restore)

        rect23 = get_rect2(code23, stroke_color=ORANGE, stroke_width=3, buff=0.05).stretch(
            0.76, 0, about_point=code23.get_right())
        temp = Tex("temp").next_to(link[2][0], DOWN, buff=0.15).set_color(GREY_C).scale(0.5)
        p1 = Tex("p1").next_to(link[0][0], DOWN, buff=0.15).set_color(BLUE_A).scale(0.5)
        p2 = Tex("p2").next_to(link[1][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        self.play(ShowCreation(rect23), ShowCreation(p1), ShowCreation(p2), Write(temp))
        self.wait(4)
        link.save_state()

        self.play(rect23.shift, code_unit)
        self.play(FadeOut(point))
        point.set_color(YELLOW)
        point.shift(-link_unit)
        point.rotate(PI)
        self.play(ShowCreation(point))
        self.play(rect23.shift, code_unit * 2)
        self.play(p1.shift, link_unit)
        self.play(rect23.shift, code_unit * 2)
        self.play(FadeOut(temp),
                  p2.shift, link_unit)

        self.wait()
        self.remove(p1, p2, code_rect, code_group, right_code, arrow, rect23)
        link.restore()

    def show_code2(self, link, title):
        link.save_state()
        code1 = create_code("1.  LinkNode *reverse(LinkNode *head) {")
        code2 = create_code("2.      if (head == NULL) {")
        code3 = create_code("3.          return head;")
        code4 = create_code("4.      }")
        code5 = create_code("5.      LinkNode *p1 = head;")
        code6 = create_code("6.      LinkNode *p2 = p1->next;")
        code7 = create_code("7.      while (p2) {")
        code8 = create_code("8.         LinkNode *temp = p2->next;")
        code9 = create_code("9.         p2->next = p1;")
        code10 = create_code("10.        p1 = p2;")
        code11 = create_code("11.        p2 = temp;")
        code12 = create_code("12.     }")
        code13 = create_code("13.     // 第一个结点的next指向NULL")
        code14 = create_code("14.     head->next = NULL;")
        code15 = create_code("15.     // 返回新链表的head")
        code16 = create_code("16.     return p1;")
        code17 = create_code("17. }")
        code18 = create_code("18. head = reverse(head);")
        code_group = VGroup(
            code1, code2, code3, code4, code5, code6, code7, code8, code9,
            code10, code11, code12, code13, code14, code15, code16, code17, code18
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.07).shift(DOWN * 1.2).scale(0.75)

        code_rect1 = get_rect2(VGroup(code5, code8, code12),
                               buff=0.15, stroke_color=BLACK, stroke_width=2, fill_opacity=1, fill_color=WHITE)
        self.play(FadeIn(code_rect1))
        self.play(
            Write(code5, run_time=0.5),
            Write(code6, run_time=0.5),
            Write(code7, run_time=0.5),
            Write(code8, run_time=0.5),
            Write(code9, run_time=0.5),
            Write(code10, run_time=0.5),
            Write(code11, run_time=0.5),
            Write(code12, run_time=0.5),
        )

        p1 = Tex("p1").next_to(link[0][0], DOWN, buff=0.15).set_color(BLUE_A).scale(0.5)
        p2 = Tex("p2").next_to(link[1][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        temp = Tex("temp").next_to(link[2][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        size = len(link)
        unit1 = link[1].get_center() - link[0].get_center()
        unit2 = link[size - 1].get_center() - link[size - 2][0].get_center()
        for i in range(size - 2):
            if i == 0:
                self.play(Write(p1), Write(p2))
            else:
                self.play(FadeOut(temp, run_time=0.3),
                          p1.shift, unit1,
                          p2.shift, unit1)
                if i == size - 3:
                    temp.shift(unit2)
                else:
                    temp.shift(unit1)
            self.play(FadeIn(temp))
            point = link[i + 1][1]
            self.play(FadeOut(point))
            point.set_color(YELLOW)
            point.shift(-unit1)
            point.rotate(PI)
            self.play(ShowCreation(point))
        self.play(FadeOut(temp, run_time=0.3),
                  p1.shift, unit1,
                  p2.shift, unit2)

        wrong1 = get_rect2(link[0], buff=0.08, stroke_color=RED, stroke_width=2)
        self.play(ShowCreation(wrong1))
        # 忘了改title了 视频已经录了 懒得调整、直接remove
        title2 = Title("单链表反转-错误代码2").scale(0.9)
        self.remove(title)
        self.add(title2)

        code_rect2 = get_rect2(VGroup(code5, code8, code12, code13, code14),
                               buff=0.15, stroke_color=BLACK, stroke_width=2, fill_opacity=1, fill_color=WHITE)

        head = Tex("head").next_to(link[0][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        self.play(Write(head))
        self.wait(2)
        self.play(Transform(code_rect1, code_rect2))
        self.play(Write(code13), Write(code14))

        wrong_point = link[0][1]
        self.play(FadeOut(wrong_point))
        wrong_point.set_color(YELLOW)
        wrong_point.shift(-unit1)
        wrong_point.rotate(PI)
        self.play(ShowCreation(wrong_point))
        last_null = link[size - 1].copy().next_to(wrong_point, LEFT, buff=0)
        self.play(FadeIn(last_null), FadeOut(link[size - 1], run_time=0.3))
        self.wait()
        self.play(FadeOut(wrong1))

        title3 = Title("单链表反转-错误代码3").scale(0.9)
        self.remove(title2)
        self.add(title3)
        self.wait(5)

        head_line = get_del_line(head, color=RED)
        self.play(ShowCreation(head_line))
        self.wait()

        self.play(Indicate(p1, scale_factor=1.2, color=YELLOW))
        self.wait()
        code_rect3 = get_rect2(VGroup(code1, code5, code8, code12, code13, code14, code18),
                               buff=0.15, stroke_color=BLACK, stroke_width=2, fill_opacity=1, fill_color=WHITE)
        self.play(Transform(code_rect1, code_rect3))
        self.play(Write(code1))
        self.play(Write(code15))
        self.play(Write(code16))
        self.play(Write(code17))
        self.play(Write(code18))
        self.wait(2)

        self.remove(head_line)
        self.play(head.next_to, p1, DOWN, buff=0.5)

        title4 = Title("单链表反转-错误代码4").scale(0.9)
        self.remove(title3)
        self.add(title4)
        null_rect = get_rect2(code6, stroke_color=RED, stroke_width=3, buff=0.05).stretch(
            0.28, 0, about_point=code6.get_right())
        self.play(ShowCreation(null_rect))
        self.wait(5)
        self.play(Write(code2))
        self.play(Write(code3))
        self.play(Write(code4))
        self.wait()
        self.play(FadeOut(null_rect))
        self.wait(10)
        self.play(FadeOut(code_group),
                  FadeOut(p1),
                  FadeOut(p2),
                  FadeOut(head),
                  FadeOut(code_rect1),
                  FadeOut(last_null))
        self.play(link.restore)
        title5 = Title("单链表反转-最终版本").scale(0.9)
        self.remove(title4)
        self.add(title5)

    def show_perfect_code(self, link):
        code1 = create_code("1.  LinkNode *reverse(LinkNode *head) {")
        code2 = create_code("2.      LinkNode *p1 = NULL;")
        code3 = create_code("3.      LinkNode *p2 = head;")
        code4 = create_code("4.      while (p2) {")
        code5 = create_code("5.          LinkNode *temp = p2->next;")
        code6 = create_code("6.          p2->next = p1;")
        code7 = create_code("7.          p1 = p2;")
        code8 = create_code("8.          p2 = temp;")
        code9 = create_code("9.      }")
        code10 = create_code("10.     return p1;")
        code11 = create_code("11. }")
        code12 = create_code("12. head = reverse(head)")
        code_group = VGroup(
            code1, code2, code3, code4, code5, code6, code7, code8, code9,
            code10, code11, code12
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.07).shift(DOWN * 1.2).scale(0.9)
        perfect_code = VGroup(
            get_rect2(code_group, buff=0.15, stroke_color=BLACK, stroke_width=2, fill_opacity=1, fill_color=WHITE),
            code_group)
        self.play(FadeIn(perfect_code))

        size = len(link)
        link_unit1 = link[1].get_center() - link[0].get_center()
        link_unit2 = link[size - 1].get_center() - link[size - 2][0].get_center()
        code_unit = (code2.get_center()[1] - code1.get_center()[1]) * UP
        p1 = Tex("p1").next_to(link[0][0], DOWN, buff=0.15).set_color(BLUE_A).scale(0.5).shift(-link_unit2)
        p2 = Tex("p2").next_to(link[0][0], DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        temp = Tex("temp").next_to(link[1][0], DOWN, buff=0.15).set_color(GREY_C).scale(0.5)
        last_null = link[size - 1].copy().next_to(link[0], LEFT, link[0][1].get_width())
        # self.add(p1, p2, last_null)
        code_rect = get_rect2(code1, stroke_color=ORANGE, stroke_width=3, buff=0.05)
        code_rect.shift(code_unit)

        self.play(ShowCreation(code_rect))
        self.play(FadeIn(last_null), Write(p1))
        self.wait()

        self.play(code_rect.shift, code_unit)
        self.play(Write(p2))
        self.wait()

        self.play(code_rect.shift, code_unit)
        code_rect.save_state()
        for i in range(size - 1):
            wait_time = 0.5
            if i == 0:
                wait_time = 1

            if i > 0:
                self.play(code_rect.restore)
                self.save_state()

            self.play(code_rect.shift, code_unit, run_time=wait_time)
            self.play(FadeIn(temp), run_time=wait_time)
            self.wait(0.5)

            self.play(code_rect.shift, code_unit, run_time=wait_time)
            point = link[i][1]
            self.play(FadeOut(point), run_time=wait_time)
            point.set_color(YELLOW)
            point.shift(-link_unit1)
            point.rotate(PI)
            self.play(ShowCreation(point), run_time=wait_time)
            if i == 0:
                self.wait(2)
            else:
                self.wait(0.5)

            self.play(code_rect.shift, code_unit, run_time=wait_time)
            if i == 0:
                self.play(p1.shift, link_unit2, run_time=wait_time)
            else:
                self.play(p1.shift, link_unit1, run_time=wait_time)
            self.play(code_rect.shift, code_unit, run_time=wait_time)
            if i == size - 2:
                self.play(FadeOut(temp), p2.shift, link_unit2, run_time=wait_time)
            else:
                self.play(FadeOut(temp), p2.shift, link_unit1, run_time=wait_time)
            if i >= size - 3:
                temp.shift(link_unit2)
            else:
                temp.shift(link_unit1)

        self.play(code_rect.restore)
        self.play(code_rect.shift, code_unit * 6)
        self.wait()
        self.play(code_rect.shift, code_unit * 2, run_time=0.5)
        head = Tex("head").next_to(p1, DOWN, buff=0.15).set_color(BLUE_C).scale(0.5)
        self.play(FadeIn(head))


class TestTitle(Scene):
    def construct(self) -> None:
        title = Title("单链表反转").scale(0.9)
        self.add(title)
        text = Text("xxxxxx")
        self.add(text)
        self.play(text.shift, RIGHT)
        title2 = Title("单链表反转------xxxx").scale(0.9)
        self.remove(title)
        self.add(title2)
        self.play(text.shift, UP)
