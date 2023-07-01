from manimlib import *
from yj.common.utils.utils import get_rect2

POSITION = [ORIGIN,
            # 第二层
            ORIGIN + LEFT * 2 + DOWN, ORIGIN + RIGHT * 2 + DOWN,
            # 第三层
            ORIGIN + LEFT * 3 + DOWN * 2.5, ORIGIN + LEFT * 1 + DOWN * 2.5,
            ORIGIN + RIGHT * 1 + DOWN * 2.5, ORIGIN + RIGHT * 3 + DOWN * 2.5,
            # 第四层
            ORIGIN + LEFT * 3.3 + DOWN * 4, ORIGIN + LEFT * 2.7 + DOWN * 4,
            ORIGIN + LEFT * 1.3 + DOWN * 4, ORIGIN + LEFT * 0.7 + DOWN * 4]


def create_code(text):
    color_map = {
        "bool": "#000080",
        "int": "#000080",
        "if": "#000080",
        "true": "#000080",
        "false": "#000080",
        "return": "#000080",
        ";": "#000080",
        "2": "#000080",
        "1": "#000080",
        "*": "#808080",
        "/": "#808080",
        "@param": "#808080",
        "@retrun": "#808080",
        "判断是否为二叉搜索树": "#808080",
        "子树在根结点的下标": "#808080",
        "数组长度": "#808080",
        "数组表示的二叉树": "#808080",
        "false表示不是二叉搜索树": "#808080",
        "左结点": "#808080",
        "空结点": "#808080",
        "有左结点，并且left>=i": "#808080",
        "右结点": "#808080",
        "有右结点，并且right<=i": "#808080",
        "只有左子树和右子树都满足条件，才是二叉搜索树": "#808080",
    }
    code = Text(text, color=BLACK,
                font_size=20,
                slant=ITALIC,
                t2c=color_map,
                t2s={'1': NORMAL, '2': NORMAL, '3': NORMAL, '4': NORMAL},
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map)
    return code


def create_tip(text, color_map):
    tip = Text(text, color=BLACK,
               t2c=color_map).scale(0.8).move_to(np.array([0, -3.5, 0]))
    tip.set_color_by_text_to_color_map(color_map)
    return tip


class TreeNode:
    def __init__(self, data, position=ORIGIN, radius=0.5, left=None, right=None):
        self.data = data
        self.left_node = left
        self.right_node = right
        self.center = position
        self.radius = radius
        if data == -1 or data is None:
            self.group = VGroup(Circle(radius=radius, stroke_color=GREY, stroke_width=2),
                                Text('', color=BLACK, font="Menlo", font_size=30)).move_to(position)
        else:
            self.group = VGroup(Circle(radius=radius, stroke_color=BLACK, stroke_width=2),
                                Text(str(data), color=BLACK, font="Menlo", font_size=30)).move_to(position)

    def connect_left(self, left):
        line_center = Line(self.center, left.center)
        unit_vector = line_center.get_unit_vector()
        start, end = line_center.get_start_and_end()
        new_start = start + unit_vector * self.radius
        new_end = end - unit_vector * self.radius
        line = Line(new_start, new_end, color=BLACK)
        # left的父结点
        left.parent = self
        # self的left结点
        self.left_node = left
        return line

    def connect_right(self, right):
        line_center = Line(self.center, right.center)
        unit_vector = line_center.get_unit_vector()
        start, end = line_center.get_start_and_end()
        new_start = start + unit_vector * self.radius
        new_end = end - unit_vector * self.radius
        line = Line(new_start, new_end)
        # right的父结点
        right.parent = self
        # self的right结点
        self.right_node = right
        return line


def create_tree(origin, arr, radius, tree_list, group_list, line_list, blank_group_list, blank_line_list):
    size = len(arr)
    for i in range(size):
        node = TreeNode(arr[i], origin + POSITION[i], radius)
        tree_list[i] = node
        parent = int((i - 1) / 2)
        is_none = arr[i] == -1 or arr[i] is None
        if is_none:
            blank_group_list.append(node.group)
        else:
            group_list.append(node.group)
        if i > 0:
            line_center = Line(origin + POSITION[parent], origin + POSITION[i])
            unit_vector = line_center.get_unit_vector()
            start, end = line_center.get_start_and_end()
            new_start = start + unit_vector * radius
            new_end = end - unit_vector * radius
            if is_none:
                blank_line_list.append(DashedLine(new_start, new_end, color=GREY))
            else:
                print("i----", i, len(line_list))
                line_list.append(Line(new_start, new_end, color=BLACK))


def create_blank_tree(origin, arr, blank_tree_list, blank_group_list, blank_line_list, radius):
    size = len(arr)
    for i in range(size):
        if arr[i] == -1 or arr[i] is None:
            parent = int((i - 1) / 2)
            line_center = Line(origin + POSITION[parent], origin + POSITION[i])
            unit_vector = line_center.get_unit_vector()
            start, end = line_center.get_start_and_end()
            new_start = start + unit_vector * radius
            new_end = end - unit_vector * radius
            line = DashedLine(new_start, new_end, color=BLACK)
            data_item = VGroup(Circle(radius=radius, stroke_color=GREY, stroke_width=2, fill_color=WHITE),
                               Text('', color=BLACK, font="Menlo", font_size=30)).move_to(origin + POSITION[i])
            blank_tree_list[i] = data_item
            blank_group_list.append(data_item)
            blank_line_list.append(line)


class TestX(Scene):
    def construct(self):
        text = Text("123")
        self.add(get_rect2(text, buff=1, stroke_color=RED, stroke_width=6))
        self.add(text)
        self.add(ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/dx.jpeg"))

        # self.add(TripleScene())


class Test1(Scene):
    def construct(self):
        # self.add(error)
        # error = Text("123")
        # self.add(error)

        example1 = [8, 6, 9, 4, 5]
        example_tree_list1 = [None] * len(example1)
        example_group_list1 = []
        example_line_list1 = []
        create_tree(ORIGIN, example1, 0.5, example_tree_list1, example_group_list1, example_line_list1, [], [])
        example_tree1 = VGroup(*example_group_list1, *example_line_list1).shift(UP * 1.3 + LEFT * 3).scale(0.7)
        self.add(example_tree1)

        self.wait()
        self.play(
            example_group_list1[1].set_color, RED,
            example_group_list1[4].set_color, RED,
            example_line_list1[3].set_color, RED
        )

        error = SVGMobject("../../../assets/svg_images/error.svg", color=RED).scale(0.25).next_to(
            example_group_list1[4])
        self.play(Indicate(error, scale_factor=1.2, color=RED))

        # example2 = [8, 6, 9, 4, 7]
        # example_tree_list2 = [None] * len(example2)
        # example_group_list2 = []
        # example_line_list2 = []
        # create_tree(ORIGIN, example2, 0.5, example_tree_list2, example_group_list2, example_line_list2, [], [])
        # example_tree2 = VGroup(VGroup(*example_group_list2, *example_line_list2)).shift(UP * 1.3 + RIGHT * 3).scale(0.7)
        # self.play(ShowCreation(example_tree2))
        # self.wait()
        #
        # self.play(TransformFromCopy(example_tree_list1[4].group, example_tree_list2[4].group))
        # coin = SVGMobject("../../../assets/svg_images/right.svg", color="#1DAFEA").scale(0.25).next_to(
        #     example_group_list2[4])
        # self.play(Indicate(coin, scale_factor=1.2, color="#1DAFEA"))
        #
        # self.wait(2)
        # example_group_list1[1].set_color(BLACK)
        # example_group_list1[4].set_color(BLACK)
        # example_line_list1[3].set_color(BLACK)
        # example_group1 = VGroup(*example_group_list2, *example_line_list2)
        # self.play(FadeOut(coin),
        #           FadeOut(example_group1),
        #           FadeOut(error),
        #           VGroup(*example_group_list1, *example_line_list1).move_to, ORIGIN)
        #
        # self.play(example_group_list1[0].set_color, BLUE)
        # self.play(example_group_list1[1].set_color, BLUE, example_group_list1[2].set_color, BLUE)
        # search_tip = Text("6<8<9", color=BLACK).next_to(example_group1, DOWN)
        # coin.next_to(example_group_list1[0])
        # self.play(Indicate(coin, scale_factor=1.2, color="#1DAFEA"), Write(search_tip))
        #
        # self.play(FadeOut(example_group_list1[0]),
        #           FadeOut(example_line_list1[0]),
        #           FadeOut(example_line_list1[1]),
        #           FadeOut(coin))
        #
        # child1 = VGroup(example_group_list1[1], example_group_list1[3], example_group_list1[4])
        # child_rect1 = get_rect(child1, 0.1)
        # child2 = VGroup(example_group_list1[2])
        # child_rect2 = get_rect(child2, 0.1)
        # self.play(Indicate(child_rect1), Indicate(child_rect2))
        # self.wait()
        #
        # self.play(
        #     FadeOut(child_rect1),
        #     FadeOut(child_rect2),
        #     example_group_list1[1].set_color, RED,
        #     example_group_list1[3].set_color, RED,
        #     example_group_list1[4].set_color, RED,
        # )
        # self.wait()
        # error.next_to(example_group_list1[1])
        # self.play(Indicate(error, scale_factor=1.2, color=RED))
        #
        # self.remove(child_rect1, error, example_tree1)

        example_tree_list1 = [None] * len(example1)
        example_group_list1 = []
        example_line_list1 = []
        create_tree(ORIGIN, example1, 0.5, example_tree_list1, example_group_list1, example_line_list1, [], [])
        example_tree1 = VGroup(*example_group_list1, *example_line_list1).move_to(ORIGIN + RIGHT * 3 + UP).scale(
            0.7)
        self.play(ShowCreation(example_tree1))

        code1 = create_code(
            "/**\n* 判断是否为二叉搜索树\n* @param arr 数组表示的二叉树\n* @param i 子树在根结点的下标\n* @param n 数组长度\n* @return false表示不是二叉搜索树\n*/\nbool isSearchTree(int arr[], int n, int i) {")
        code2 = create_code("    if (i >= n || arr[i] == -1) {\n        // 空结点\n        return true;\n    }")
        code3 = create_code(
            "\n    int left = 2 * i + 1;// 左结点\n    if (left < n && arr[left] != -1 && arr[left] >= arr[i]) {\n        // 有左结点，并且left>=i\n        return false;\n    }")
        code4 = create_code(
            "\n    int right = 2 * i + 2;// 右结点\n    if (right < n && arr[right] != -1 && arr[right] <= arr[i]) {\n        // 有右结点，并且right<=i\n        return false;\n    }")
        code5 = create_code(
            "    \n    // 只有左子树和右子树都满足条件，才是二叉搜索树\n    return isSearchTree(arr, n, left) && isSearchTree(arr, n, right);")
        code6 = create_code("}\n\nbool isSearch(int arr[], int n) {\n    return isSearchTree(arr, n, 0);\n}")
        code_group = VGroup(code1, code2, code3, code4, code5, code6).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1).to_edge(LEFT)
        self.play(Write(code_group))
        # self.play(
        #     FadeOut(example_group_list1[2]),
        #     FadeOut(error),
        #     FadeOut(child_rect1),
        #     FadeIn(example_tree1)
        # )

        # subject = Text(
        #     "用数组保存二叉树，每个结点保存正整数\n空结点的值为-1，设计一个高效算法\n判断二叉树是否为二叉搜索树")
        # subject.set_color(BLACK)
        # subject.set_color_by_text_to_color_map({
        #     "数组": BLUE,
        #     "二叉树": BLUE,
        #     "搜索树": BLUE_E,
        # })
        # self.add(subject)
        # # self.wait()
        #
        # rec = Rectangle(stroke_color="#10AEFF", stroke_width=6, width=2.5,
        #                 height=0.8).shift(RIGHT * 0.77 + DOWN * 0.68)
        # self.play(Indicate(rec, scale_factor=1.1, color="#10AEFF"))

        # arrow = Line(LEFT, RIGHT, stroke_width=15, color=BLACK)
        # arrow.add_tip(width=0.4, length=0.4)
        # self.play(ShowCreation(arrow, run_time=1))
        # arrow.save_state()
        # self.play(arrow.scale, 3)
        #
        # relations = VGroup(
        #     Text("对于任意结点i和数组arr", color=BLACK, t2c={"arr": BLUE, "i": BLUE})
        #     .set_color_by_text_to_color_map({"arr": BLUE, "i": BLUE}),
        #     Text("父结点(如果有的话)：arr[(i - 1) / 2]", color=BLACK, t2c={"如果有的话": RED, "i": BLUE})
        #     .set_color_by_text_to_color_map({"如果有的话": RED, "i": BLUE}),
        #     Text("左孩子(如果有的话)：arr[2 * i + 1]", color=BLACK, t2c={"如果有的话": RED, "i": BLUE})
        #     .set_color_by_text_to_color_map({"如果有的话": RED, "i": BLUE}),
        #     Text("右孩子(如果有的话)：arr[2 * i + 2]", color=BLACK, t2c={"如果有的话": RED, "i": BLUE})
        #     .set_color_by_text_to_color_map({"如果有的话": RED, "i": BLUE})
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.6).shift(DOWN + RIGHT)
        # self.play(Write(relations))
        #
        # rec = Rectangle(stroke_color=BLUE, stroke_width=7,
        #                 width=relations.get_width() + 0.2,
        #                 height=relations.get_height() * 0.75 + 0.2).move_to(
        #     relations.get_center() + DOWN * relations.get_height() / 8)
        # self.play(Indicate(rec, scale_factor=1.1, color=BLUE))
        #
        # self.play(FadeOut(rec, relations[0]), arrow.restore)

        # self.camera.background_rgba = WHITE
        tree_list = [None] * 10
        group_list = []
        line_list = []
        # create_tree(ORIGIN, [2, 3, 1, -1, 4, 5, 6, -1, -1, 10], 0, tree_list, group_list, line_list)
        # print("---", group_list, line_list)
        # tree = VGroup(*group_list, *line_list)
        # self.add(tree.shift(UP * 3).scale(0.5))


class Test2(Scene):
    def construct(self):
        array1 = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8).scale(0.5),
                        Text('a', color=BLACK, font="Menlo", font_size=25))
        array2 = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8).scale(0.5),
                        Text('1', color=BLACK, font="Menlo", font_size=25)) \
            .move_to(array1.get_center()).shift(np.array((array1.get_width(), 0, 0)))
        array3 = VGroup(Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8).scale(0.7),
                        Text('1', color=BLACK, font="Menlo", font_size=25)) \
            .move_to(array2.get_center()).shift(np.array((array2.get_width(), 0, 0)))

        self.add(array1, array2, array3)


class TestRes(Scene):
    def construct(self):
        radius = 0.5

        title = Title("2022年408算法题", color=BLACK).scale(0.9)
        title.underline.set_color(BLACK)
        self.add(title)

        subject = Text(
            "用数组保存二叉树，每个结点保存正整数\n空结点的值为-1，设计一个高效算法\n判断二叉树是否为二叉搜索树")
        subject.set_color(BLACK)
        subject.set_color_by_text_to_color_map({
            "数组": BLUE,
            "二叉树": BLUE,
            "搜索树": BLUE_E,
        })
        self.play(Write(subject))
        self.wait()

        tip = create_tip("首先看下题目关键字", {"关键字": BLUE})
        self.play(Write(tip))
        self.wait()
        subject.save_state()
        self.play(subject.shift, UP * 2 + LEFT * 4.5,
                  subject.scale, 0.45)

        sub_text = Text("数组保存二叉树", color=BLACK).shift(UP * 2).scale(0.6)
        self.wait(0.5)
        title2 = Title("二叉树的数组表示", color=BLACK).scale(0.9)
        title2.underline.set_color(BLACK)

        tree_data_list = ['a', 'b', 'c', None, None, 'd']
        tree_list = [None] * len(tree_data_list)
        group_list = []
        line_list = []
        blank_group_list = []
        blank_line_list = []

        create_tree(ORIGIN, tree_data_list, radius, tree_list, group_list, line_list, blank_group_list, blank_line_list)
        tree = VGroup(VGroup(*group_list, *line_list), VGroup(*blank_group_list, *blank_line_list)).shift(
            UP * 1.3 + LEFT * 3).scale(0.7)

        self.play(TransformMatchingStrings(subject, sub_text, path_arc=90 * DEGREES),
                  Transform(title, title2), FadeIn(tree[0]), FadeOut(tip))
        self.wait(0.5)

        # 画数组
        array_items = []
        pre_item = None
        for item in tree_data_list:
            node = None
            if pre_item is None:
                node = Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8).scale(0.6). \
                    shift(RIGHT * 1.5)
            else:
                node = Rectangle(stroke_color=BLACK, stroke_width=2, width=1.5, height=0.8).scale(0.6) \
                    .move_to(pre_item.get_center()).shift(np.array((pre_item.get_width(), 0, 0)))
            pre_item = node
            array_items.append(node)
        array_group = VGroup(*array_items)
        self.play(ShowCreation(array_group))

        self.wait()
        self.play(Transform(tip, create_tip("画出二叉树对应的完全二叉树，并对其编号",
                                            {"完全二叉树": BLUE, "编号": BLUE_E})))
        self.play(ShowCreation(tree[1]))
        self.wait()

        number_item = []
        for i in range(len(tree_list)):
            tree_node = tree_list[i].group
            number_item.append(Text(str(i), color=BLUE, font="Menlo", font_size=20)
                               .move_to(tree_node.get_center() + DOWN * 0.55))
        self.play(ShowCreation(VGroup(*number_item)), run_time=2)

        arrow = Line(LEFT, RIGHT, stroke_width=15, color=BLACK)
        arrow.add_tip(width=0.4, length=0.4)
        self.play(ShowCreation(arrow),
                  Transform(tip, create_tip("二叉树的编号=数组的下标，依次向数组存入二叉树结点即可", {
                      "编号": BLUE_E, "下标": BLUE_E, "结点": BLUE
                  })))
        arr_text_list = []
        for i in range(len(tree_data_list)):
            if (tree_data_list[i] is not None):
                text = Text(tree_data_list[i], color=BLACK, font="Menlo", font_size=20).move_to(
                    array_items[i].get_center())
                arr_text_list.append(text)
                self.play(TransformFromCopy(tree_list[i].group, text))

        relations = VGroup(
            Text("对于任意结点i和数组arr", color=BLACK, t2c={"arr": BLUE, "i": BLUE})
            .set_color_by_text_to_color_map({"arr": BLUE, "i": BLUE}),
            Text("父结点(如果有的话)：arr[(i - 1) / 2]", color=BLACK, t2c={"如果有的话": RED, "i": BLUE})
            .set_color_by_text_to_color_map({"如果有的话": RED, "i": BLUE}),
            Text("左孩子(如果有的话)：arr[2 * i + 1]", color=BLACK, t2c={"如果有的话": RED, "i": BLUE})
            .set_color_by_text_to_color_map({"如果有的话": RED, "i": BLUE}),
            Text("右孩子(如果有的话)：arr[2 * i + 2]", color=BLACK, t2c={"如果有的话": RED, "i": BLUE})
            .set_color_by_text_to_color_map({"如果有的话": RED, "i": BLUE})
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.6).shift(DOWN * 1.5 + RIGHT * 0.8)
        self.play(Transform(tip, create_tip("数组中二叉树结点的关系如上", {})), Write(relations))

        rec = Rectangle(stroke_color=BLUE, stroke_width=7,
                        width=relations.get_width() + 0.2,
                        height=relations.get_height() * 0.75 + 0.2).move_to(
            relations.get_center() + DOWN * relations.get_height() / 8)
        self.play(Indicate(rec, scale_factor=1.1, color=BLUE))
        self.wait()

        self.play(FadeOut(rec),
                  FadeOut(arrow),
                  FadeOut(sub_text),
                  FadeOut(tip),
                  FadeOut(relations),
                  FadeOut(array_group),
                  FadeOut(VGroup(*arr_text_list)),
                  FadeOut(VGroup(*number_item)),
                  FadeOut(VGroup(*group_list)),
                  FadeOut(VGroup(*line_list)),
                  FadeOut(VGroup(*blank_group_list)),
                  FadeOut(VGroup(*blank_line_list)),
                  subject.restore)
        rec = Rectangle(stroke_color="#10AEFF", stroke_width=6, width=2.5,
                        height=0.8).shift(RIGHT * 0.77 + DOWN * 0.68)
        title3 = Title("二叉搜索树定义", color=BLACK).scale(0.9)
        title3.underline.set_color(BLACK)
        self.play(Indicate(rec, scale_factor=1.1, color="#10AEFF"), Transform(title, title3))
        self.wait()
        self.play(FadeOut(rec),
                  subject.shift, UP * 2 + LEFT * 4.5,
                  subject.scale, 0.45)

        example = ['a', 'l', 'r']
        tree_list = [None] * len(example)
        group_list = []
        line_list = []
        create_tree(ORIGIN, example, 0.5, tree_list, group_list, line_list, [], [])
        self.play(ShowCreation(VGroup(*group_list, *line_list)))

        tip = create_tip("二叉搜索树：对于任意一个结点a，必然满足a.left<a<a.right", {
            "二叉搜索树": BLUE, "任意": BLUE, "a.left<a<a.right": BLUE
        })
        sub_text = Text("l<a<r", color=BLUE).shift(UP * 2).scale(0.6)
        self.play(Write(tip), Write(sub_text))

        example1 = [8, 6, 9, 4, 5]
        example_tree_list1 = [None] * len(example1)
        example_group_list1 = []
        example_line_list1 = []
        create_tree(ORIGIN, example1, 0.5, example_tree_list1, example_group_list1, example_line_list1, [], [])
        example_tree1 = VGroup(*example_group_list1, *example_line_list1).shift(UP * 1.3 + LEFT * 3).scale(0.7)
        self.play(FadeIn(example_tree1), FadeOut(sub_text), FadeOut(VGroup(*group_list, *line_list)))

        self.wait()
        self.play(
            Transform(tip,
                      create_tip("左图的二叉树由于结点6大于其右孩子5，所以不是二叉搜索树", {"结点6大于其右孩子5": RED})),
            example_group_list1[1].set_color, RED,
            example_group_list1[4].set_color, RED,
            example_line_list1[3].set_color, RED
        )
        error = SVGMobject("../../../assets/svg_images/error.svg", color=RED).scale(0.25).next_to(
            example_group_list1[4])
        self.play(Indicate(error, scale_factor=1.2, color="#D81E06"))

        self.wait()
        example2 = [8, 6, 9, 4, 7]
        example_tree_list2 = [None] * len(example2)
        example_group_list2 = []
        example_line_list2 = []
        create_tree(ORIGIN, example2, 0.5, example_tree_list2, example_group_list2, example_line_list2, [], [])
        example_tree2 = VGroup(*example_group_list2, *example_line_list2).shift(UP * 1.3 + RIGHT * 3).scale(0.7)
        self.play(ShowCreation(example_tree2))
        self.wait()

        self.play(TransformFromCopy(example_group_list1[4], example_group_list2[4]),
                  Transform(tip, create_tip("结点5改成结点7得到的新二叉树便是一棵二叉搜索树",
                                            {"二叉搜索树": BLUE})))
        coin = SVGMobject("../../../assets/svg_images/right.svg", color="#1DAFEA").scale(0.25).next_to(
            example_group_list2[4])
        self.play(Indicate(coin, scale_factor=1.2, color="#1DAFEA"))

        self.wait(2)
        example_group_list1[1].set_color(BLACK)
        example_group_list1[4].set_color(BLACK)
        example_line_list1[3].set_color(BLACK)
        self.play(FadeOut(coin),
                  FadeOut(example_tree2),
                  FadeOut(error),
                  example_tree1.shift, RIGHT * 2)

        title4 = Title("算法步骤", color=BLACK).scale(0.9)
        title4.underline.set_color(BLACK)
        self.play(Transform(tip, create_tip("首先看根结点：" + str(example1[0]), {str(example1[0]): BLUE})),
                  Transform(title, title4),
                  example_group_list1[0].set_color, BLUE)
        self.wait()
        self.play(example_group_list1[1].set_color, BLUE, example_group_list1[2].set_color, BLUE)
        coin.next_to(example_group_list1[0])
        self.play(Indicate(coin, scale_factor=1.2, color="#1DAFEA"),
                  Transform(tip, create_tip("6<8<9：所以根结点8满足条件", {"6<8<9": BLUE, "8": BLUE_E})))
        self.wait()

        self.play(FadeOut(example_group_list1[0]),
                  FadeOut(example_line_list1[0]),
                  FadeOut(example_line_list1[1]),
                  FadeOut(coin),
                  Transform(tip, create_tip("排除根结点8，看看其左右子树是否满足条件", {"左右子树": BLUE, "8": BLUE_E})))
        self.wait()

        child1 = VGroup(example_group_list1[1], example_group_list1[3], example_group_list1[4])
        child_rect1 = old_get_rect(child1, 0.1)
        child2 = VGroup(example_group_list1[2])
        child_rect2 = old_get_rect(child2, 0.1)
        self.play(ShowCreation(child_rect1), ShowCreation(child_rect2))
        self.wait()

        self.play(
            FadeOut(child_rect2),
            FadeOut(child2),
            Transform(tip, create_tip("先看看左子树6", {"左子树": BLUE, "6": BLUE_E})),
            example_group_list1[1].set_color, RED,
            example_group_list1[3].set_color, RED,
            example_group_list1[4].set_color, RED,
        )
        self.wait()
        error.next_to(example_group_list1[1])
        self.play(Indicate(error, scale_factor=1.2, color=RED),
                  Transform(tip, create_tip("6>5：不满足根<右的条件", {"根<右": BLUE, "6>5": BLUE_E, "不满足": RED})))
        self.wait()
        self.play(FadeOut(tip), run_time=0.5)

        self.remove(child_rect1, example_tree1, example_tree2, error)
        # todo 太麻烦了 不住地咋整 重新new了一个
        example_tree_list1 = [None] * len(example1)
        example_group_list1 = []
        example_line_list1 = []
        create_tree(ORIGIN, example1, 0.5, example_tree_list1, example_group_list1, example_line_list1, [], [])
        example_tree1 = VGroup(*example_group_list1, *example_line_list1).move_to(ORIGIN + RIGHT * 3 + UP).scale(0.7)
        title5 = Title("代码实现", color=BLACK).scale(0.9)
        title5.underline.set_color(BLACK)
        self.play(ShowCreation(example_tree1), Transform(title, title5))
        self.wait(1)

        code1 = create_code(
            "/**\n* 判断是否为二叉搜索树\n* @param arr 数组表示的二叉树\n* @param i 子树在根结点的下标\n* @param n 数组长度\n* @return false表示不是二叉搜索树\n*/\nbool isSearchTree(int arr[], int n, int i) {")
        code2 = create_code("    if (i >= n || arr[i] == -1) {\n        // 空结点\n        return true;\n    }")
        code3 = create_code(
            "\n    int left = 2 * i + 1;// 左结点\n    if (left < n && arr[left] != -1 && arr[left] >= arr[i]) {\n        // 有左结点，并且left>=i\n        return false;\n    }")
        code4 = create_code(
            "\n    int right = 2 * i + 2;// 右结点\n    if (right < n && arr[right] != -1 && arr[right] <= arr[i]) {\n        // 有右结点，并且right<=i\n        return false;\n    }")
        code5 = create_code(
            "    \n    // 只有左子树和右子树都满足条件，才是二叉搜索树\n    return isSearchTree(arr, n, left) && isSearchTree(arr, n, right);")
        code6 = create_code("}\n\nbool isSearch(int arr[], int n) {\n    return isSearchTree(arr, n, 0);\n}")
        code_group = VGroup(code1, code2, code3, code4, code5, code6).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1).to_edge(LEFT)

        tip = create_tip("函数定义：方法名、参数、返回值", {"方法名": BLUE, "参数": BLUE, "返回值": BLUE})
        self.play(
            FadeOut(subject),
            Write(tip),
            Write(code1))
        self.wait(2)

        self.play(Transform(tip, create_tip("处理空结点的情况，-1或者越界表示空",
                                            {"-1": BLUE_E, "越界": BLUE_E, "空结点": BLUE})),
                  Write(code2))
        self.wait(2)

        self.play(
            Indicate(example_group_list1[0], scale_factor=1.2, color=BLUE, run_time=2),
            Indicate(example_group_list1[1], scale_factor=1.2, color=BLUE, run_time=2),
            Transform(tip, create_tip("判断i是否大于left", {"i": BLUE_E, "left": BLUE_E, "大于": BLUE})),
            Write(code3)
        )
        self.wait(2)

        self.play(
            Indicate(example_group_list1[0], scale_factor=1.2, color=BLUE, run_time=2),
            Indicate(example_group_list1[2], scale_factor=1.2, color=BLUE, run_time=2),
            Transform(tip, create_tip("判断i是否小于right", {"i": BLUE_E, "right": BLUE_E, "小于": BLUE})),
            Write(code4)
        )
        self.wait(2)

        child_rect1 = old_get_rect(VGroup(example_group_list1[1], example_group_list1[3], example_group_list1[4]), 0.1)
        child_rect2 = old_get_rect(VGroup(example_group_list1[2]), 0.1)
        self.play(
            ShowCreation(child_rect1),
            ShowCreation(child_rect2),
            Transform(tip, create_tip("递归判断左右子树是否也为二叉搜索树", {"递归": BLUE})),
            Write(code5)
        )
        self.wait(2)

        self.play(Transform(tip, create_tip("补上最后调用的代码就搞定了", {})),
                  Write(code6))
        self.wait(5)
