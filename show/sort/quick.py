import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')

from manimlib import *
from yj.math_show.common.utils.utils import get_circle
from yj.math_show.common.utils.utils import swap_arr
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
    "递归结束的条件": "#808080",
    "key为基准数": "#808080",
    "从最右往左找到第一个小于p的位置j": "#808080",
    "从左往右找到第一个大于p的位置i": "#808080",
    "交换i和j": "#808080",
    "i和j相遇，说明temp的左边的数都小于等于temp；右边都大于等于temp": "#808080",
    "temp位置已确定，递归快排基准数左右两边剩余的数": "#808080",
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
                font_size=19,
                slant=ITALIC,
                t2c=color_map_quick,
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map_quick)
    return code


def create_list(arrays):
    nodes = VGroup(
        *[
            VGroup(Circle(radius=0.5, stroke_width=1, stroke_color=BLACK, fill_opacity=1, fill_color=WHITE),
                   Text(str(item), color=BLACK))
            for item in arrays
        ]
    ).arrange(RIGHT, buff=0.3)
    return nodes


def create_list2(arrays):
    nodes = VGroup(
        *[
            VGroup(Circle(radius=0.5, stroke_color=BLACK, fill_opacity=1, fill_color=GREEN),
                   Text(str(item), color=BLACK))
            for item in arrays
        ]
    ).arrange(RIGHT, buff=0.3)
    return nodes


class QuickSort(Scene):
    def construct(self) -> None:
        title = Title("看图写代码-快速排序").scale(0.8)
        self.add(title)
        data_list = [4, 1, 3, 5, 8, 7, 2]
        data_map = [0, 1, 2, 3, 4, 5, 6]
        sorted_list = [4, 1, 3, 5, 8, 7, 2]
        sorted_list.sort()

        old_arrays = create_list(data_list)
        sort_arrays = create_list2(sorted_list)

        self.show_desc(old_arrays, sort_arrays)
        # self.add(old_arrays.shift(UP * 2))
        # self.add(old_arrays)

        old_arrays.save_state()
        self.show_principle1(old_arrays)
        code_group, code_rect = self.show_exchange_code()
        self.show_code1(code_rect, code_group)

        self.show_exchange(data_list, data_map, old_arrays)
        self.wait()
        old_arrays.restore()

        data_list = [4, 1, 3, 5, 8, 7, 2]
        data_map = [0, 1, 2, 3, 4, 5, 6]

        self.play(
            FadeIn(code_rect),
            old_arrays.shift, LEFT * 4,
            old_arrays.scale, 0.6,
            title.shift, LEFT * 4.25,
        )

        # self.add(code_rect)
        self.add(code_group[0], code_group[1], code_group[2], code_group[3], code_group[4],
                 code_group[25], code_group[26], code_group[27], code_group[28])
        self.show_exchange(data_list, data_map, old_arrays, code_group),

    def show_desc(self, old_arrays, sort_arrays):
        self.play(ShowCreation(old_arrays, run_time=0.1))
        # 解说：这是一个无序序列
        self.wait(2)
        old_arrays.save_state()
        self.play(old_arrays.shift, UP * 2)

        match_index = [3, 0, 1, 4, 6, 5, 2]
        self.play(*[
            ReplacementTransform(old_arrays[index].copy(), sort_arrays[match_index[index]])
            for index in range(len(match_index))
        ], run_time=3)
        # 解说：快速排序：一个把无须序列转换成有序序列的算法
        self.wait(5)
        self.play(
            FadeOut(sort_arrays)
        )

    def show_principle1(self, old_arrays):
        poi = [
            DOWN * 1,
            DOWN * 2.1 + LEFT * 4.1,
            DOWN * 2.17 + LEFT * 3.1,
            DOWN * 1.91 + RIGHT * 3.91,
            DOWN * 1.4 + RIGHT * 3.04,
            DOWN * 0.9 + RIGHT * 3.9,
            DOWN * 1.37 + LEFT * 2.5,
        ]
        alpha = [0, 0.5, 0.8, -0.5, -0.2, -0.1, 0.1]

        coin = SVGMobject("../../../assets/svg_images/coin.svg", color=WHITE).scale(1.5).shift(LEFT * 3.5 + DOWN * 1.25)
        fav = SVGMobject("../../../assets/svg_images/favo.svg", color=WHITE).scale(1.5).shift(RIGHT * 3.5 + DOWN * 1.2)
        remove_obj = [coin, fav]
        # 解说：接下来，我们介绍快速排序的核心思想
        self.wait(2)
        mid_point = old_arrays[0].copy()
        self.play(mid_point.move_to, poi[0], run_time=2)
        remove_obj.append(mid_point)
        mid_point[0].set_color(BLUE_C)
        # 解说：选择序列第一个数作为"基数"
        self.wait(2)
        self.play(
            FadeIn(coin), FadeIn(fav), run_time=2
        )

        # 解说：把序列中剩下的数中小于基数的放到基数的左边，大于基数的数放到基数的右边
        # 解说：那么就能确定基数在最终排序序列中的位置
        for i in range(1, len(poi)):
            self.play(
                Indicate(old_arrays[i][1], color=BLUE_A, scale_factor=1.4)
            )
            self.test(remove_obj, old_arrays[i], poi[i], alpha[i])

        # 解说：把
        self.wait(10)
        mid_cir = get_circle(mid_point, stroke_color=GREEN, stroke_width=1, buff=0)
        self.play(ShowCreation(mid_cir))
        remove_obj.append(mid_cir)
        mid_point[0].set_color(GREEN)

        coin_cir = get_circle(coin, stroke_color=ORANGE, stroke_width=5, buff=0.05)
        self.play(ShowCreation(coin_cir))
        remove_obj.append(coin_cir)
        # 解说：左边的数：变成一个连续的无序序列，但是长度比之前序列小；因此只要重复之前的操作，最终无须序列的长度会变为0，也就是全都已排序
        self.wait(5)
        self.remove(VGroup(*remove_obj))

    def test(self, removes: [], point1, point2_poi: np.ndarray, angle):
        circle = ArcBetweenPoints(point1.get_center(), point2_poi, angle=angle)
        obj = point1.copy()
        removes.append(obj)
        obj.save_state()

        def update_func(mob, alpha):
            mob.restore()

            mob.move_to(circle.point_from_proportion(alpha))
            if angle < 0:
                mob.rotate(-TAU * 4 * alpha)
            else:
                mob.rotate(TAU * 4 * alpha)

        self.play(
            UpdateFromAlphaFunc(obj, update_func),
            run_time=2
        )
        # "#FAFAD2"
        obj[0].set_color(BLUE_A)

    def show_code1(self, code_rect, code_group):
        # 解说：因此快排可以用递归来实现
        self.play(FadeIn(code_rect))
        self.play(Write(code_group[0]))
        # 解说：定义递归函数：通过数组+左右下标三个参数：便可以表示数组任意一段序列
        self.wait(3)
        # 解说：先写递归结束条件：当序列长度为0或者1时显然无须再排序了
        self.play(Write(code_group[1]))
        self.play(Write(code_group[2]))
        self.play(Write(code_group[3]))
        self.play(Write(code_group[4]))

        # 解说：中间按照"基数"划分的代码咱写空着
        self.wait(3)
        self.play(Write(code_group[25]))
        self.play(Write(code_group[26]))
        self.play(Write(code_group[27]))
        self.play(Write(code_group[28]))
        # 解说：划分完后，再次递归函数，对左右两边序列进行快排
        # 解说：这样整个序列就完成了排序
        self.wait(3)
        self.remove(code_rect)
        self.remove(code_group)

    def show_exchange(self, data_list, data_map, old_arrays, code_group=None):
        left = 0
        right = len(data_list) - 1
        unit = old_arrays[1].get_center()[0] - old_arrays[0].get_center()[0]

        self.exchange2(data_list, data_map, old_arrays, unit, left, right, True, code_group)

    def exchange2(self, data_list, data_map, old_arrays, unit, left, right, first, code_group=None):
        if left > right:
            return
        if left == right:
            self.wait()
            old_arrays[data_map[left]][0].set_color(GREEN)
            return
        self.wait(1)
        key = data_list[left]
        i = left
        j = right

        scale = 1
        if code_group is not None:
            scale = 0.6
        left_arrow = Line(old_arrays[data_map[left]].get_center() + 1.7 * DOWN * scale,
                          old_arrays[data_map[left]].get_center() + 0.7 * DOWN * scale,
                          color=YELLOW, stroke_width=8 * scale).add_tip(width=0.2 * scale, length=0.2 * scale)
        left_text = Tex("LEFT").scale(0.5 * scale).next_to(left_arrow, DOWN, buff=0.1 * scale)
        left_p = VGroup(left_arrow, left_text)
        right_arrow = Line(old_arrays[data_map[right]].get_center() + 1.7 * DOWN * scale,
                           old_arrays[data_map[right]].get_center() + 0.7 * DOWN * scale,
                           color=BLUE, stroke_width=8 * scale).add_tip(width=0.2 * scale, length=0.2 * scale)
        right_text = Tex("RIGHT").scale(0.5 * scale).next_to(right_arrow, DOWN, buff=0.1 * scale)
        right_p = VGroup(right_arrow, right_text)

        old_arrays[data_map[left]][0].set_color(YELLOW)
        if first:
            # 解说：选择第一个数为"基数"
            self.wait(5)
        # 解说：定义两个左右"指针"
        self.play(
            ShowCreation(left_p),
            ShowCreation(right_p)
        )
        if first and code_group is not None:
            self.play(Write(code_group[5]))
            self.play(Write(code_group[6]))
            self.play(Write(code_group[7]))
            self.play(Write(code_group[8]))
            self.wait(2)
            self.play(Write(code_group[9]))

        loop = 0
        while i < j:
            while i < j and data_list[j] >= key:
                j -= 1
                self.play(
                    right_p.shift, LEFT * unit
                )
            if first and loop == 0:
                if code_group is None:
                    self.wait(5)
                else:
                    self.play(Write(code_group[10]))
                    self.play(Write(code_group[11]))
                    self.play(Write(code_group[12]))
                    self.play(Write(code_group[13]))
                    self.wait()
            while i < j and data_list[i] <= key:
                i += 1
                self.play(
                    left_p.shift, RIGHT * unit
                )
            if first and loop == 0:
                if code_group is None:
                    self.wait(5)
                else:
                    self.play(Write(code_group[14]))
                    self.play(Write(code_group[15]))
                    self.play(Write(code_group[16]))
                    self.play(Write(code_group[17]))
                    self.wait()
            if i < j:
                swap_arr(data_list, i, j)
                self.play(
                    old_arrays[data_map[i]].move_to, old_arrays[data_map[j]].get_center(),
                    old_arrays[data_map[j]].move_to, old_arrays[data_map[i]].get_center(),
                )
                swap_arr(data_map, i, j)
            if first and loop == 0:
                if code_group is None:
                    self.wait()
                else:
                    self.play(Write(code_group[18]))
                    self.play(Write(code_group[19]))
                    self.play(Write(code_group[20]))
                    self.play(Write(code_group[21]))
                    self.play(Write(code_group[22]))
                    self.wait()
            loop = 1

        self.wait(1)
        swap_arr(data_list, left, i)
        self.play(
            old_arrays[data_map[i]].move_to, old_arrays[data_map[left]].get_center(),
            old_arrays[data_map[left]].move_to, old_arrays[data_map[i]].get_center(),
        )
        swap_arr(data_map, i, left)
        old_arrays[data_map[i]][0].set_color(GREEN)

        if first and code_group is not None:
            self.play(Write(code_group[23]))
            self.play(Write(code_group[24]))

        self.remove(left_p, right_p)
        self.exchange2(data_list, data_map, old_arrays, unit, left, i - 1, False, code_group)
        self.exchange2(data_list, data_map, old_arrays, unit, j + 1, right, False, code_group)

    def show_exchange_code(self):
        code1 = create_code("1.  void quickSort(int arr[], int left, int right) {")
        code2 = create_code("2.      if (left >= right) {")
        code3 = create_code("3.          // 递归结束的条件")
        code4 = create_code("4.          return;")
        code5 = create_code("5.      }")
        code6 = create_code("6.      // key为基准数")
        code7 = create_code("7.      int key = arr[left];")
        code8 = create_code("8.      int i = left;")
        code9 = create_code("9.      int j = right;")
        code10 = create_code("10.     while (i < j) {")
        code11 = create_code("11.         while (i < j && arr[j] >= key) {")
        code12 = create_code("12.             // 从最右往左找到第一个小于p的位置j")
        code13 = create_code("13.             j--;")
        code14 = create_code("14.         }")
        code15 = create_code("15.         while (i < j && arr[i] <= key) {")
        code16 = create_code("16.             // 从左往右找到第一个大于p的位置i")
        code17 = create_code("17.             i++;")
        code18 = create_code("18.         }")
        code19 = create_code("19.         if (i < j) {")
        code20 = create_code("20.             // 交换i和j")
        code21 = create_code("21.             swap(arr, i, j);")
        code22 = create_code("22.         }")
        code23 = create_code("23.      }")
        code24 = create_code("24.      // i和j相遇，说明temp的左边的数都小于等于temp；右边都大于等于temp")
        code25 = create_code("25.      swap(arr, i, left);")
        code26 = create_code("26.      // temp位置已确定，递归快排基准数左右两边剩余的数")
        code27 = create_code("27.      quickSort(arr, left, i - 1);")
        code28 = create_code("28.      quickSort(arr, j + 1, right);")
        code29 = create_code("29. }    ")

        code_group = VGroup(
            code1, code2, code3, code4, code5, code6, code7, code8, code9, code10,
            code11, code12, code13, code14, code15, code16, code17, code18, code19, code20,
            code21, code22, code23, code24, code25, code26, code27, code28, code29
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_edge(RIGHT, buff=0.3)
        code_rect = get_rect2(code_group, buff=0.1, stroke_color=BLACK, stroke_width=5, fill_opacity=1,
                              fill_color=WHITE)
        return code_group, code_rect
        # self.add()
        # self.add(code_group)


class Test(Scene):
    def construct(self) -> None:
        test1 = Circle()
        self.add(test1)
        test = Line(ORIGIN, ORIGIN + 3 * DOWN).next_to(test1, DOWN, buff=0.01)
        test.scale(0.5, about_edge=TOP)
        self.add(test)
