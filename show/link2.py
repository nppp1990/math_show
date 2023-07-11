import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.math_show.common.scene.link import create_link
from yj.math_show.common.utils.text import create_bottom_tip
from yj.math_show.common.utils.utils import get_path_by_points


class Test1(Scene):

    def construct(self):
        title = Title("链表分类", color=BLACK).scale(0.9)
        title.underline.set_color(BLACK)
        self.add(title)
        self.wait()

        node_list, group_list = create_link([1, 2, 3], ORIGIN + LEFT * 4, line_width=0.7, line_color=BLACK)
        link_group = VGroup(*group_list)
        tip = create_bottom_tip("不带头结点的单链表", {"不带头结点": BLUE})

        point_arrow_line = Line(ORIGIN, ORIGIN + UP * 0.8, color=BLACK, stroke_width=10).next_to(
            group_list[0][0], direction=DOWN, buff=0.1)
        point_arrow_line.add_tip(width=0.3, length=0.3)
        point_arrow_text = Text("head", color=BLACK).scale(0.7)
        point_arrow_text.next_to(point_arrow_line, buff=0.15)
        point_arrow = VGroup(point_arrow_line, point_arrow_text)

        self.show_link1(title, link_group, group_list, point_arrow, tip)
        self.wait(2)

        self.play(FadeIn(VGroup(*group_list[:len(group_list) - 1])),
                  FadeOut(point_arrow))
        self.wait()
        self.play(link_group.shift, RIGHT * 2)
        self.wait()

        head_img = ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/dx.jpeg")
        head_arrow = group_list[0][1].copy().next_to(group_list[0], LEFT, buff=0)
        head_img.scale(0.2).next_to(head_arrow, LEFT, buff=0)

        self.show_link2(title, link_group, group_list, point_arrow, tip, head_img, head_arrow)
        self.wait(2)

        paths = get_path_by_points([group_list[len(group_list) - 2][1].get_start(),
                                    group_list[len(group_list) - 2][1].get_start(),
                                    group_list[len(group_list) - 2][1].get_end(),
                                    group_list[len(group_list) - 2][1].get_end() + UP * 1.2,
                                    group_list[0][0].get_left() + group_list[0][1].get_width() * LEFT + UP * 1.2,
                                    group_list[0][0].get_left() + group_list[0][1].get_width() * LEFT,
                                    group_list[0][0].get_left()], color=BLACK)
        paths[len(paths) - 1].add_tip(width=0.2, length=0.2)

        self.show_link3(title, link_group, group_list, point_arrow, tip, head_img, head_arrow, paths)

        self.show_link4(title, link_group, group_list, point_arrow, tip, head_img, head_arrow, paths)

        self.wait(2)
        self.clear()
        link_img = ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/link.jpg").scale(2)
        self.add(link_img)
        self.wait(6)

    def show_link1(self, title, link_group, group_list, point_arrow, tip):
        title2 = Title("链表分类-不带头结点的单链表", color=BLACK).scale(0.9)
        title2.underline.set_color(BLACK)
        self.play(ShowCreation(link_group, run_time=2),
                  Write(tip),
                  Transform(title, title2))
        self.wait()
        self.play(FadeIn(point_arrow),
                  Transform(tip, create_bottom_tip("不带头结点的单链表：head指针指向第一个有数据域的结点", {
                      "不带头结点": BLUE
                  })))
        self.wait()
        right = group_list[len(group_list) - 1].get_center()[0] - point_arrow[0].get_center()[0]
        self.play(
            Transform(tip, create_bottom_tip("不带头结点的单链表：链表为空的状态如图, head=NULL", {
                "不带头结点": BLUE, "链表为空": BLUE
            })),
            FadeOut(VGroup(*group_list[:len(group_list) - 1]), run_time=2),
            point_arrow.shift, RIGHT * right, run_time=2)

    def show_link2(self, title, link_group, group_list, point_arrow, tip, head_img, head_arrow):
        title2 = Title("链表分类-带头结点的单链表", color=BLACK).scale(0.9)
        title2.underline.set_color(BLACK)
        self.play(Transform(title, title2))

        start_poi = LEFT_SIDE + TOP + head_img.get_width() / 2 * RIGHT + head_img.get_height() / 2 * DOWN
        arc = ArcBetweenPoints(start_poi, head_img.get_center(), angle=TAU / 5)
        head_img.save_state()

        def update_func(mob, alpha):
            mob.restore()
            mob.move_to(arc.point_from_proportion(alpha))
            mob.rotate(TAU * 4 * alpha)

        self.play(UpdateFromAlphaFunc(head_img, update_func, run_time=3),
                  Transform(tip, create_bottom_tip("带头结点的单链表：会增加一个空数据域的头结点", {
                      "带头结点": BLUE, "空数据域": BLUE_E, "头结点": BLUE
                  })))
        self.wait(2)
        self.play(ShowCreation(head_arrow),
                  Transform(tip, create_bottom_tip("带头结点的单链表：头结点的next指向链表第一个数据域的结点", {
                      "带头结点": BLUE, "头结点": BLUE
                  })))
        self.wait(2)
        point_arrow.shift(RIGHT * (head_img.get_center()[0] - point_arrow[0].get_center()[0]))
        self.play(FadeIn(point_arrow),
                  Transform(tip, create_bottom_tip("带头结点的单链表：head指向头结点", {
                      "head": BLUE, "头结点": BLUE
                  })))
        self.wait(2)

        # 不包含null的最后一个
        last_item = group_list[len(group_list) - 2]
        right_dis = last_item.get_center()[0] + last_item.get_width() / 2 - (
                head_arrow.get_center()[0] + head_img.get_width() / 2)
        self.play(
            Transform(tip, create_bottom_tip("带头结点的单链表：链表为空的状态如图，head->next=NULL", {
                "带头结点": BLUE, "链表为空": BLUE
            })),
            FadeOut(VGroup(*group_list[:len(group_list) - 1]), run_time=2),
            head_img.shift, RIGHT * right_dis,
            head_arrow.shift, RIGHT * right_dis,
            point_arrow.shift, RIGHT * right_dis, run_time=2)

    def show_link3(self, title, link_group, group_list, point_arrow, tip, head_img, head_arrow, paths):
        title2 = Title("链表分类-不带头结点的循环单链表", color=BLACK).scale(0.9)
        title2.underline.set_color(BLACK)
        point_dest_poi = np.array([group_list[0][0].get_center()[0], point_arrow.get_center()[1], 0])
        self.play(FadeOut(head_img, run_time=1),
                  FadeOut(head_arrow, run_time=1),
                  Transform(title, title2, run_time=1),
                  Transform(tip, create_bottom_tip("接着我们看看不带头结点的循环单链表", {
                      "循环单链表": BLUE, "不带头结点": BLUE
                  })),
                  FadeIn(VGroup(*group_list[:len(group_list) - 1]), run_time=2),
                  point_arrow.move_to, point_dest_poi, run_time=2)
        self.wait()
        self.play(FadeOut(group_list[len(group_list) - 1]),
                  Transform(tip, create_bottom_tip("不带头结点的循环单链表：链表最后一个结点不再指向NULL", {
                      "循环单链表": BLUE, "不带头结点": BLUE, "最后一个": BLUE_E, "NULL": RED
                  })))
        self.wait(1.5)

        self.play(FadeOut(group_list[len(group_list) - 2][1], run_time=0.5),
                  Transform(tip, create_bottom_tip("不带头结点的循环单链表：链表最后一个结点指向第一个数据域结点", {
                      "循环单链表": BLUE, "不带头结点": BLUE, "最后一个": BLUE_E, "数据域": BLUE_E
                  })),
                  ShowCreation(VGroup(*paths), run_time=4))
        self.wait(1.5)

        null_item = Text('NULL', color=BLACK, font="Menlo", font_size=30).move_to(
            np.array([point_arrow[0].get_center()[0], group_list[0].get_center()[1], 0])
        )
        self.play(
            Transform(tip, create_bottom_tip("不带头结点的循环单链表：链表为空的状态如图, head=NULL", {
                "不带头结点": BLUE, "循环单链表": BLUE, "链表为空": BLUE
            })),
            FadeOut(VGroup(*group_list[:len(group_list) - 2]), run_time=2),
            FadeOut(VGroup(group_list[len(group_list) - 2][0]), run_time=2),
            FadeOut(VGroup(*paths), run_time=2))
        self.play(ShowCreation(null_item))
        self.wait(2)
        self.play(FadeOut(null_item))

    def show_link4(self, title, link_group, group_list, point_arrow, tip, head_img, head_arrow, paths):
        title2 = Title("链表分类-带头结点的循环单链表", color=BLACK).scale(0.9)
        title2.underline.set_color(BLACK)
        self.play(
            Transform(title, title2),
            FadeIn(VGroup(*group_list[:len(group_list) - 2])),
            FadeIn(VGroup(group_list[len(group_list) - 2][0])),
            FadeIn(VGroup(*paths)))
        self.play(Transform(tip, create_bottom_tip("接下来我们看看带头结点的循环单链表", {
            "带头结点": BLUE, "循环单链表": BLUE
        })))
        self.wait()
        head_dis = (group_list[0].get_left()[0] - head_arrow.get_right()[0]) * RIGHT
        head_img.shift(head_dis)
        self.play(FadeIn(head_img),
                  Transform(tip, create_bottom_tip("带头结点的循环单链表：先增加一个没有数据的头结点", {
                      "带头结点": BLUE, "循环单链表": BLUE, "头结点": BLUE
                  })))
        self.wait(2)

        head_arrow.shift(head_dis)
        self.play(FadeIn(head_arrow),
                  Transform(tip, create_bottom_tip("带头结点的循环单链表：头结点的next指向第一个数据域结点", {
                      "带头结点": BLUE, "循环单链表": BLUE, "头结点": BLUE
                  })))
        self.wait(2)

        point_arrow.shift(RIGHT * (head_img.get_center()[0] - point_arrow[0].get_center()[0]))
        self.play(FadeIn(point_arrow),
                  Transform(tip, create_bottom_tip("带头结点的循环单链表：head指向这个头结点", {
                      "带头结点": BLUE, "循环单链表": BLUE, "头结点": BLUE
                  })))
        self.wait(2)

        last2 = paths[len(paths) - 2]
        path2 = get_path_by_points([last2.get_start(),
                                    last2.get_start() + LEFT * head_img.get_width() / 2,
                                    last2.get_start() + LEFT * head_img.get_width() / 2 + DOWN * (
                                            UP * 1.2 - head_img.get_width() / 2)], color=BLACK)
        path2[len(path2) - 1].add_tip(width=0.2, length=0.2)

        self.play(
            FadeOut(paths[len(paths) - 1]),
            FadeOut(paths[len(paths) - 2]),
            Transform(tip,
                      create_bottom_tip("带头结点的循环单链表：最后一个数据域结点要指向头结点head", {
                          "带头结点": BLUE, "循环单链表": BLUE, "头结点": BLUE
                      })))
        self.wait(2)
        self.play(ShowCreation(VGroup(*path2)), run_time=2)
        self.wait(3)

        self.play(
            FadeOut(head_arrow),
            FadeOut(VGroup(*group_list[:len(group_list) - 2]), run_time=2),
            FadeOut(VGroup(group_list[len(group_list) - 2][0]), run_time=2),
            FadeOut(VGroup(*path2)),
            FadeOut(VGroup(*paths[:len(paths) - 2])),
            Transform(tip,
                      create_bottom_tip("带头结点的循环单链表：链表为空的状态如图", {
                          "带头结点": BLUE, "循环单链表": BLUE, "头结点": BLUE
                      }))
        )

        path3 = get_path_by_points([head_arrow.get_left(),
                                    head_arrow.get_right(),
                                    head_arrow.get_right() + UP * 1.2,
                                    head_arrow.get_center() + UP * 1.2,
                                    head_img.get_top(),
                                    ], color=BLACK)
        path3[len(path3) - 1].add_tip(width=0.2, length=0.2)
        self.play(ShowCreation(VGroup(*path3)),
                  Transform(tip, create_bottom_tip("带头结点的循环单链表：链表为空的状态如图，head->next=head", {
                      "带头结点": BLUE, "循环单链表": BLUE, "头结点": BLUE
                  })))


class TestLine(Scene):
    def construct(self):
        self.add(Text("xxxxx"))
        self.wait()
        self.clear()
        head_img = ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/link.jpg").scale(2)
        self.add(head_img)

    # l = Line(ORIGIN, LEFT)
    # print(l.end, l.get_end())
    #
    # paths = get_path_by_points([ORIGIN, RIGHT * 2, RIGHT * 2 + DOWN * 3, RIGHT * 2 + DOWN * 3 + LEFT * 5],
    #                            color=WHITE, stroke_width=10)
    # paths[len(paths) - 1].add_tip(width=0.3, length=0.3)
    # self.play(ShowCreation(VGroup(*paths)), run_time=4)
