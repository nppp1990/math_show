import sys

sys.path.insert(0, '/Users/yuanjian/Downloads/py-project/manim')
from yj.math_show.common.utils.utils import get_rect2
from yj.math_show.common.utils.utils import get_del_line
from yj.math_show.common.utils.text import create_bottom_tip
from manimlib import *

color_map_20 = {
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

    "/": "#808080",
    "记录最小值": "#808080",
    "记录新的最小值": "#808080",
    "判断a、b、c中最小值，并且将其index++": "#808080",
    "bool": "#000080",
    "while": "#000080",
    "int": "#000080",
    "if": "#000080",
    "else": "#000080",
    "return": "#000080",
    ";": "#000080",
}


def create_code(text):
    code = Text(text, color=BLACK,
                font_size=19,
                slant=ITALIC,
                t2c=color_map_20,
                t2s={'1.': NORMAL, '2.': NORMAL, '3.': NORMAL, '4.': NORMAL},
                alignment='LEFT',
                font="Menlo")
    code.set_color_by_text_to_color_map(color_map_20)
    return code


def crate_array(nums: [], color):
    groups = []
    pre = None
    for num in nums:
        group = VGroup(Square(stroke_width=0).scale(0.5),
                       Text(str(num), color=color, font="Menlo", font_size=30))
        if pre is not None:
            group.next_to(pre, RIGHT, buff=0)
        pre = group
        groups.append(group)
    return VGroup(*groups)


def get_min(s1, s2, s3, i, j, k):
    return abs(s1[i] - s2[j]) + abs(s1[i] - s3[k]) + abs(s2[j] - s3[k])


def get_bottom_tip(text, color_map=None, **kwargs):
    return create_bottom_tip(text, color_map, color=WHITE, **kwargs)


def get_wrapper_num(num):
    return " " + str(num) + " "


def show_prove(self):
    self.add(Title("算法步骤推导").scale(0.9))

    prove_txt1 = Tex("S1[i]<S2[j]<S3[k])").scale(0.7).shift(LEFT * 3)
    prove_arrow1 = Line(prove_txt1.get_right() + RIGHT * 0.3, prove_txt1.get_right() + 1.3 * RIGHT,
                        stroke_width=10).add_tip(width=0.3, length=0.3)
    prove_tex_res1 = Tex("D=2(S3[k]-S1[i])").scale(0.7).next_to(prove_arrow1, buff=0.3)
    prove1 = VGroup(prove_txt1, prove_tex_res1, prove_arrow1)
    prove_height = prove_txt1.get_height()

    prove_txt2 = Tex("S1[i], S2[j+1], S3[k]", tex_to_color_map={
        "j+1": BLUE
    }).scale(0.7).move_to(prove_txt1.get_left(), aligned_edge=LEFT)
    prove_tex_res2 = Tex("D=2(max(S3[k],S2[j+1])-S1[i])", tex_to_color_map={
        "j+1": BLUE
    }).scale(0.7).move_to(prove_tex_res1.get_left(), aligned_edge=LEFT)
    prove_arrow2 = prove_arrow1.copy()
    prove_del2 = get_del_line(prove_txt2, color=RED)
    prove2 = VGroup(prove_txt2, prove_tex_res2, prove_arrow2, prove_del2)

    prove_txt3 = Tex("S1[i], S2[j], S3[k+1]", tex_to_color_map={
        "k+1": BLUE
    }).scale(0.7).move_to(prove_txt1.get_left(), aligned_edge=LEFT)
    prove_tex_res3 = Tex("D=2(S3[k+1]-S1[i])", tex_to_color_map={
        "k+1": BLUE
    }).scale(0.7).move_to(prove_tex_res1.get_left(), aligned_edge=LEFT)
    prove_arrow3 = prove_arrow1.copy()
    prove_del3 = get_del_line(prove_txt3, color=RED)
    prove3 = VGroup(prove_txt3, prove_tex_res3, prove_arrow3, prove_del3)

    prove_txt4 = Tex("S1[i+1], S2[j], S3[k]", tex_to_color_map={
        "i+1": BLUE
    }).scale(0.7).move_to(prove_txt1.get_left(), aligned_edge=LEFT)
    prove_tex_res4 = Tex("2(|S3[k]-S1[i+1]|)\\\\2(|S3[k]-S1[j]|)\\\\2(|S3[i+1]-S1[j]|)", tex_to_color_map={
        "i+1": BLUE
    }).scale(0.7).move_to(prove_tex_res1.get_left(), aligned_edge=LEFT)
    prove_arrow4 = prove_arrow1.copy()
    prove4 = VGroup(prove_txt4, prove_tex_res4, prove_arrow4)

    tip = get_bottom_tip("对于任意的i、j、k")
    self.play(Write(tip), Write(prove_txt1))
    self.play(ShowCreation(prove_arrow1))
    self.play(Write(prove_tex_res1))
    self.wait(2)

    self.play(Transform(tip, get_bottom_tip("要查找可能得最小值，下一个步骤只可能是i++或者j++或者k++", {
        "i++": BLUE, "j++": BLUE, "k++": BLUE
    })))
    self.wait(2)

    self.play(Write(prove_txt2, lag_ratio=0.5), prove1.shift, UP * (prove_height + 0.3))
    self.play(ShowCreation(prove_arrow2))
    self.play(Write(prove_tex_res2))
    self.wait()
    self.play(ShowCreation(prove_del2),
              Transform(tip, get_bottom_tip("j++显然得不到更小的距离值", {
                  "j++": BLUE, "更小": BLUE
              })))
    self.wait(2)

    self.play(Write(prove_txt3, lag_ratio=0.5), VGroup(prove1, prove2).shift, UP * (prove_height + 0.3))
    self.play(ShowCreation(prove_arrow3))
    self.play(Write(prove_tex_res3))
    self.wait(2)
    self.play(ShowCreation(prove_del3),
              Transform(tip, get_bottom_tip("k++同样得不到更小的距离值", {
                  "k++": BLUE, "更小": BLUE
              })))
    self.wait(2)

    self.play(Write(prove_txt4, lag_ratio=0.5), VGroup(prove1, prove2, prove3).shift,
              UP * (prove_tex_res4.get_height() + 0.3))
    self.play(ShowCreation(prove_arrow4))
    self.play(Write(prove_tex_res4))
    self.wait()
    self.play(Transform(tip, get_bottom_tip("i++可能得到不同的三种距离值，并且有可能更小", {
        "i++": BLUE, "更小": BLUE
    })))
    self.wait(2)
    self.play(Transform(tip, get_bottom_tip(
        "综上，对于每一个(i,j,k)（S1[i]<S2[j]<S3[k]）时\n只有改变i=i+1，才有可能找到更小的距离")))


class Test(Scene):
    def construct(self):
        self.show_subject()
        self.show_process()
        self.wait(3)
        self.clear()
        show_prove(self)
        self.wait(3)
        self.clear()
        self.add(Title("算法过程演示").scale(0.9))
        s1 = [-1, 0, 9]
        s2 = [-25, -10, 10, 11]
        s3 = [2, 9, 17, 30, 41]

        array1 = crate_array(s1, BLUE).shift(LEFT * 1 + UP * 2)
        array2 = crate_array(s2, GREEN).move_to(array1.get_left() + DOWN * 1, aligned_edge=LEFT)
        array3 = crate_array(s3, YELLOW).move_to(array1.get_left() + DOWN * 2, aligned_edge=LEFT)
        arrays = VGroup(array1, array2, array3)

        # tip1 = get_bottom_tip("每次选择最小数所在数组的下标递增")
        tip = get_bottom_tip("记录最小距离")

        i = 0
        j = 0
        k = 0

        min_text = Text("min", font="Menlo", font_size=30, color="#F7F7F7").next_to(array1, LEFT).shift(LEFT)
        line = Line(min_text.get_right(), min_text.get_right() + 0.7 * RIGHT,
                    color="#F7F7F7", stroke_width=10).add_tip(width=0.3, length=0.3).next_to(min_text, RIGHT)
        min_index = VGroup(min_text, line).shift(UP)

        value_text_lab = Text("最小距离：", font_size=30).move_to(min_text.get_left() + DOWN * 4, aligned_edge=LEFT)
        min_value = Text("", font_size=30).next_to(value_text_lab, RIGHT, buff=0.2)
        value_text_lab2 = Text("当前距离：", font_size=30).next_to(value_text_lab, DOWN, buff=0.2)
        cur_value = Text("", font_size=30).set_color("#F7F7F7").next_to(value_text_lab2, RIGHT, buff=0.2)

        rect = get_rect2(VGroup(array1[0], array2[0], array3[0]), buff=-0.1, stroke_color=ORANGE, stroke_width=6)
        min_dis = get_min(s1, s2, s3, i, j, k)
        min_x = 0
        self.play(FadeIn(arrays), run_time=2)
        self.add(value_text_lab, value_text_lab2, cur_value)

        min_nums = None

        while i < len(s1) and j < len(s2) and k < len(s3):
            temp = get_min(s1, s2, s3, i, j, k)
            is_first = i == 0 and j == 0 and k == 0
            if is_first:
                self.play(ShowCreation(rect), run_time=1)
                min_nums = Text("(" + str(s1[i]) + ","
                                + str(s2[j]) + ","
                                + str(s3[k]) + ")",
                                font_size=30, color=GREY).next_to(min_value, LEFT, buff=1.6)
                self.play(Write(min_nums))
                self.play(
                    Transform(min_value, Text(str(min_dis), font_size=30).next_to(value_text_lab, RIGHT, buff=0.2)),
                    Write(tip))
                # self.wait()
            else:
                self.move_min_index(min_index, arrays[min_x])
                self.play(Transform(tip, get_bottom_tip("每次选择最小数所在数组的下标递增")))
                self.move_array(arrays[min_x])
                self.play(Transform(cur_value,
                                    Text(str(temp), font_size=30).set_color("#F7F7F7").next_to(
                                        value_text_lab2, RIGHT, buff=0.2)))
                # self.wait()

            if temp < min_dis:
                min_dis = temp
                self.play(Transform(min_nums, Text("(" + str(s1[i]) + ","
                                                   + str(s2[j]) + ","
                                                   + str(s3[k]) + ")",
                                                   font_size=30, color=GREY)
                                    .next_to(min_value, LEFT, buff=1.6)))
                self.play(
                    Transform(min_value, Text(str(min_dis), font_size=30).next_to(value_text_lab, RIGHT, buff=0.2)))

                # self.wait()

            if s1[i] < s2[j]:
                if s1[i] < s3[k]:
                    i += 1
                    min_x = 0
                else:
                    k += 1
                    min_x = 2
            else:
                if s2[j] < s3[k]:
                    j += 1
                    min_x = 1
                else:
                    k += 1
                    min_x = 2

        self.move_min_index(min_index, arrays[min_x])

        self.wait(2)

        self.show_code()
        self.wait(5)

    def show_code(self):
        self.clear()
        # self.add(Title("代码实现").scale(0.9))
        temp_tip = Text("接下来通过算法动画，来看看代码的实现")
        self.play(Write(temp_tip))
        s1 = [-1, 0, 9]
        s2 = [-25, -10, 10, 11]
        s3 = [2, 9, 17, 30, 41]

        array1 = crate_array(s1, BLUE).shift(LEFT * 5 + UP * 2).scale(0.8)
        array2 = crate_array(s2, GREEN).scale(0.8).move_to(array1.get_left() + DOWN * 1, aligned_edge=LEFT)
        array3 = crate_array(s3, YELLOW).scale(0.8).move_to(array1.get_left() + DOWN * 2, aligned_edge=LEFT)
        arrays = VGroup(array1, array2, array3)

        min_text = Text("min", font="Menlo", font_size=30, color="#F7F7F7").next_to(array1, LEFT).shift(LEFT)
        line = Line(min_text.get_right(), min_text.get_right() + 0.7 * RIGHT,
                    color="#F7F7F7", stroke_width=10).add_tip(width=0.3, length=0.3).next_to(min_text, RIGHT)
        min_index = VGroup(min_text, line).scale(0.8).shift(UP)
        rect = get_rect2(VGroup(array1[0], array2[0], array3[0]), buff=-0.1, stroke_color=ORANGE, stroke_width=6)
        i = 0
        j = 0
        k = 0
        min_dis = get_min(s1, s2, s3, i, j, k)
        min_x = 0

        min_value = Text("", font_size=30).move_to(min_text.get_left() + DOWN * 4, aligned_edge=LEFT)
        poi = min_value.get_center()

        code1 = create_code("1.  int getMinD(int a[], int b[], int c[], int l, int m, int n) {")
        code2 = create_code("2.      int i = 0, j = 0, k = 0;")
        code3 = create_code("3.      // 记录最小值\n4.      int min = getDis(a[i],b[j],c[k]);\n5.      int temp;")
        code4 = create_code("6.      while (i < l && j < m && k < n) {")
        code5 = create_code(
            "7.          temp = getDis(a[i], b[j], c[k]);\n8.          if (temp < min) {\n9.              // 记录新的最小值\n10.             min = temp;\n11.         }")
        code12 = create_code("12.         // 判断a、b、c中最小值，并且将其index++")
        code13 = create_code("13.         if (a[i] < b[j]) {")
        code14 = create_code("14.             if (a[i] < c[k]) {")
        code15 = create_code("15.                 i++;")
        code16 = create_code("16.             } else {")
        code17 = create_code("17.                 k++;")
        code18 = create_code("18.             }")
        code19 = create_code("19.         } else {")
        code20 = create_code("20.             if (b[i] < c[k]) {")
        code21 = create_code("21.                 j++;")
        code22 = create_code("22.             } else {")
        code23 = create_code("23.                 k++;")
        code24 = create_code("24.             }")
        code25 = create_code("25.         }")
        code26 = create_code("26.     }")
        code27 = create_code("27.     return min;")
        code28 = create_code("28.  }")
        code_group = VGroup(
            code1, code2, code3, code4, code5,
            code12, code13, code14, code15, code16, code17, code18, code19, code20,
            code21, code22, code23, code24, code25, code26, code27, code28
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(RIGHT)

        self.add(get_rect2(code_group, buff=0.1, stroke_color=BLACK, stroke_width=5, fill_opacity=1, fill_color=WHITE))

        self.play(FadeOut(temp_tip, run_time=0 / 5),
                  FadeIn(arrays, run_time=2))
        self.wait()

        tip = get_bottom_tip("首先定义函数").to_edge(LEFT)
        self.play(Write(VGroup(code1, code28)), Write(tip))
        self.wait()
        self.play(Write(VGroup(code2)), Transform(tip, get_bottom_tip("i,j,k用来遍历三个数组", {
            "i": BLUE, "j": GREEN, "k": YELLOW}).to_edge(LEFT)))

        has_show_tip = False
        has_show_tip2 = False

        while i < len(s1) and j < len(s2) and k < len(s3):
            temp = get_min(s1, s2, s3, i, j, k)
            is_first = i == 0 and j == 0 and k == 0
            if is_first:
                self.play(ShowCreation(rect), run_time=1)
                self.play(
                    Transform(min_value, Text("min=" + str(min_dis), font_size=30).move_to(poi, aligned_edge=LEFT)))
                self.wait()
                self.play(Write(VGroup(code3)), Transform(tip, get_bottom_tip("初始状态下的最小距离").to_edge(LEFT)))
                self.play(Write(VGroup(code4, code26)),
                          Transform(tip, get_bottom_tip("当i、j、k有一个越界时结束循环", {
                              "i": BLUE, "j": GREEN, "k": YELLOW, "越界": BLUE
                          }).scale(0.7).to_edge(LEFT)))
            else:
                self.move_min_index(min_index, arrays[min_x])
                self.move_array(arrays[min_x])
                if has_show_tip and not has_show_tip2:
                    self.play(Write(VGroup(
                        code12, code13, code14, code15, code16, code17, code18, code19, code20,
                        code21, code22, code23, code24, code25,
                    )), Transform(tip, get_bottom_tip("找出三个数中最小的下标：递增", {
                        "最小": BLUE, "下标": BLUE, "递增": BLUE
                    }).scale(0.8).to_edge(LEFT)))
                    has_show_tip2 = True

                # self.wait()

            if temp < min_dis:
                min_dis = temp
                if not has_show_tip:
                    self.play(Write(VGroup(code5)),
                              Transform(tip, get_bottom_tip("当前的距离temp和min比较、用较小的更新min", {
                                  "较小": BLUE, "更新min": BLUE
                              }).scale(0.6).to_edge(LEFT)))
                    has_show_tip = True
                self.play(
                    Transform(min_value, Text("min=" + str(min_dis), font_size=30).move_to(poi, aligned_edge=LEFT)))

            if s1[i] < s2[j]:
                if s1[i] < s3[k]:
                    i += 1
                    min_x = 0
                else:
                    k += 1
                    min_x = 2
            else:
                if s2[j] < s3[k]:
                    j += 1
                    min_x = 1
                else:
                    k += 1
                    min_x = 2

        self.move_min_index(min_index, arrays[min_x])
        self.play(Write(code27), Transform(tip, get_bottom_tip("循环结束后，min就是最小距离", {
            "min": BLUE
        }).scale(0.9).to_edge(LEFT)))
        self.wait(10)

    def move_min_index(self, min_index, target_y):
        self.play(
            min_index.shift,
            DOWN * (min_index.get_center()[1] - target_y.get_center()[1])
        )

    def move_array(self, array):
        self.play(
            array.shift,
            LEFT * array[0].get_width()
        )
        array.remove(array[0])

    def show_subject(self):
        title = Title("2020年408算法题").scale(0.9)
        self.add(title)
        subject = Text(
            "定义三元组 (a, b, c) （其中a, b, c均为整数）的\n"
            "距离D=|a-b| + |b-c| + |c-a|。\n"
            "给定三个非空整数集合S1、S2和S3，按升序分别存储在3个数组中。\n"
            "设计一个尽可能高效的算法，计算并输出所有可能的三元组\n"
            " (a, b, c) （a∈S1, b∈S2, c∈S3）中的 最小距离 。\n"
            "例如 S1={-1，0，9}, S2={-25，-10，10，11}，S3={2，9，17，30，41}\n"
            "则 最小距离 为 2 ，相应的三元组为 (9，10，9) 。")
        subject.scale(0.8)
        subject.set_color_by_text_to_color_map({
            "最小距离": BLUE,
            " (a, b, c) ": BLUE,
            "D=|a-b| + |b-c| + |c-a|": "#449C47",
            " (9，10，9) ": GREEN,
            " 2 ": GREEN
        })
        self.play(Write(subject), run_time=10)

        self.wait(3)
        self.play(FadeOut(title),
                  subject.shift, UP * 3 + LEFT * 4,
                  subject.scale, 0.5)

    def show_process(self):
        text1 = VGroup(Text("假设"), Tex("a<b<c")).arrange(RIGHT, buff=0.1).shift(LEFT * 2)
        text2 = VGroup(Text("那么"), Tex("D=|a-b|+|b-c|+|c-a|")).arrange(RIGHT, buff=0.2).move_to(
            text1.get_left(), aligned_edge=LEFT)

        text3 = VGroup(Tex("D=(b-a)+(c-b)+(c-a)="), Tex("2(c-a)")).arrange(RIGHT, buff=0.2).move_to(
            text1.get_left(), aligned_edge=LEFT)
        self.play(Write(text1))
        self.wait(0.5)
        height = text1.get_height()
        self.play(Write(text2, lag_ratio=0.5), text1.shift, UP * (height + 0.3))
        self.wait(0.5)
        self.play(Write(text3, lag_ratio=0.5), VGroup(text1, text2).shift, UP * (height + 0.3))
        self.wait(1)

        rect = get_rect2(text3[1], stroke_color=BLUE, stroke_width=6, buff=0.1)
        tip = get_bottom_tip("所以D的值取决于a和c的差值", {"a": BLUE, "c": BLUE})
        self.play(ShowCreation(rect, run_time=2), Write(tip, run_time=1, lag_ratio=1))


class Test2(Scene):

    def construct(self) -> None:
        show_prove(self)


class Test3(Scene):
    def construct(self):
        code1 = create_code("1.  int getMinD(int a[], int b[], int c[], int l, int m, int n) {")
        code2 = create_code("2.      int i = 0, j = 0, k = 0;")
        code3 = create_code("3.      // 记录最小值\n4.      int min = getDis(a[i],b[j],c[k]);\n5.      int temp;")
        code4 = create_code("6.      while (i < l && j < m && k < n) {")
        code5 = create_code(
            "7.          temp = getDis(a[i], b[j], c[k]);\n8.          if (temp < min) {\n9.              // 记录新的最小值\n10.             min = temp;\n11.         }")
        code12 = create_code("12.         // 判断a、b、c中最小值，并且将其index++")
        code13 = create_code("13.         if (a[i] < b[j]) {")
        code14 = create_code("14.             if (a[i] < c[k]) {")
        code15 = create_code("15.                 i++;")
        code16 = create_code("16.             } else {")
        code17 = create_code("17.                 k++;")
        code18 = create_code("18.             }")
        code19 = create_code("19.         } else {")
        code20 = create_code("20.             if (b[i] < c[k]) {")
        code21 = create_code("21.                 j++;")
        code22 = create_code("22.             } else {")
        code23 = create_code("23.                 k++;")
        code24 = create_code("24.             }")
        code25 = create_code("25.         }")
        code26 = create_code("26.     }")
        code27 = create_code("27.     return min;")
        code28 = create_code("28.  }")
        code_group = VGroup(
            code1, code2, code3, code4, code5,
            code12, code13, code14, code15, code16, code17, code18, code19, code20,
            code21, code22, code23, code24, code25, code26, code27, code28
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(RIGHT)

        self.add(get_rect2(code_group, buff=0.1, stroke_color=BLACK, stroke_width=5, fill_opacity=1, fill_color=WHITE))

        tip = get_bottom_tip("首先定义函数").to_edge(LEFT)
        self.play(Write(VGroup(code1, code28)), Write(tip))
        self.play(Write(VGroup(code2)), Transform(tip, get_bottom_tip("i,j,k用来遍历三个数组", {
            "i": BLUE, "j": GREEN, "k": YELLOW}).to_edge(LEFT)))
        self.play(Write(VGroup(code3)), Transform(tip, get_bottom_tip("初始状态下的最小距离").to_edge(LEFT)))
        self.play(Write(VGroup(code4, code26)),
                  Transform(tip, get_bottom_tip("当i、j、k有一个越界时结束循环", {
                      "i": BLUE, "j": GREEN, "k": YELLOW, "越界": BLUE
                  }).scale(0.7).to_edge(LEFT)))
        self.play(Write(VGroup(code5)),
                  Transform(tip, get_bottom_tip("当前的距离temp和min比较、用较小的更新min", {
                      "较小": BLUE, "更新min": BLUE
                  }).scale(0.6).to_edge(LEFT)))
        self.play(Write(VGroup(
            code12, code13, code14, code15, code16, code17, code18, code19, code20,
            code21, code22, code23, code24, code25,
        )), Transform(tip, get_bottom_tip("找出三个数中最小的下标：递增", {
            "最小": BLUE, "下标": BLUE, "递增": BLUE
        }).scale(0.8).to_edge(LEFT)))
        self.play(Write(code27), Transform(tip, get_bottom_tip("循环结束后，min就是最小距离", {
            "min": BLUE
        }).scale(0.9).to_edge(LEFT)))
