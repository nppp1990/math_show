from manimlib import *
import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')


class LinkNode:

    def __init__(self, data, position=ORIGIN, **args):
        """以position为中心坐标的链表结点"""
        data_item = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8,
                                     fill_opacity=1, fill_color=WHITE),
                           Text(data, color=BLACK, font="Menlo", font_size=30))
        next_item = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8,
                                     fill_opacity=1, fill_color="#E6D0DE"),
                           Text('next', color=BLACK, font="Menlo", font_size=30))
        self.data = data
        data_group = VGroup(data_item, next_item).arrange(RIGHT, buff=0).move_to(position).scale(0.7)
        arrow = Line(ORIGIN, ORIGIN + RIGHT * args["line_width"], color=args["line_color"]).next_to(data_group, buff=0)
        arrow.add_tip(width=0.2, length=0.2)
        self.group = VGroup(data_group, arrow)
        self.next = None

    def con_next(self, other, is_null=False):
        arrow = Line(self.get_right(), other.get_left(), color=BLACK)
        arrow.add_tip(width=0.2, length=0.2)
        if not is_null:
            self.next = other
        return arrow

    def get_left(self):
        return self.group.get_left()

    def get_right(self):
        return self.group.get_right()


def create_link(num, origin=ORIGIN, **args):
    node_list = []
    group_list = []
    pre = None
    for data in num:
        node = LinkNode(str(data), origin, **args)
        node_list.append(node)
        group_list.append(node.group)
        if pre is not None:
            node.group.next_to(pre.group, buff=0)
        pre = node

    null_item = Text('NULL', color=BLACK, font="Menlo", font_size=30).next_to(pre.group, buff=0)
    group_list.append(null_item)

    return node_list, group_list


def create_link2(num, origin=ORIGIN, **args):
    group_list = []
    pre = None
    for data in num:
        data_item = VGroup(
            Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8, fill_opacity=1, fill_color=WHITE),
            Text(data, color=BLACK, font="Menlo", font_size=30))
        arrow = Line(ORIGIN, ORIGIN + RIGHT * args["line_width"], color=args["line_color"]).next_to(data_item, buff=0)
        arrow.add_tip(width=0.2, length=0.2)
        node = VGroup(data_item, arrow)
        group_list.append(node)
        if pre is not None:
            node.next_to(pre, buff=0)
        pre = node
    null_item = Text('NULL', color=BLACK, font="Menlo", font_size=30).next_to(pre, buff=0)
    group_list.append(null_item)
    return group_list


class Test1(Scene):
    def construct(self):
        node_list, group_list = create_link(['head', 2, 3], ORIGIN + LEFT * 4, line_width=2, line_color=RED)
        self.play(ShowCreation(VGroup(*group_list).scale(1)))
        self.play(VGroup(*group_list).scale, 0.3,
                  VGroup(*group_list).shift, RIGHT)
