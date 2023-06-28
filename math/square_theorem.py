from manimlib import *


class Test1(Scene):
    def construct(self):
        title = Title('多项式平方展开').scale(0.9)
        self.add(title)
        self.show(4)
        self.show_square(4)

    def show(self, n) -> None:
        # 拼接a + b +c + ... + 到res
        res1 = '('
        a = 'a'
        for i in range(1, n + 1):
            if i == n:
                res1 += a + ')^2'
            else:
                res1 += a + '+'
            a = chr(ord(a) + 1)

        show_text1 = Tex(res1).scale(0.7)
        # self.play(Write(show_text1))

        # 拼接a^2 + b^2 + c^2 + ... + 2ab + 2ac + 2bc + ... 到res
        res2 = ''
        a = 'a'
        for i in range(1, n + 1):
            if i == n:
                res2 += a + '^2'
            else:
                res2 += a + '^2+'
            a = chr(ord(a) + 1)
        a = 'a'
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # if j == n:
                #     res2 += '2' + a + chr(ord(a) + j - i)
                # else:
                res2 += '+' + '2' + a + chr(ord(a) + j - i)
            a = chr(ord(a) + 1)
        show_text2 = Tex(res2).scale(0.7)
        show_text2.next_to(show_text1, DOWN, buff=0.5)
        # self.play(Write(show_text2))

    def show_square(self, n):
        # 大小为n的数组，随机生成n个0~1的数
        arr = []
        for i in range(n):
            arr.append(random.random())
        print(arr)
        points = []
        v_pos = ORIGIN
        for i in range(n + 1):
            cur_pos = v_pos.copy()
            temp = [cur_pos.copy()]
            for j in range(n):
                cur_pos += RIGHT * arr[j]
                temp.append(cur_pos.copy())
            if i != n:
                v_pos += DOWN * arr[i]
            points.append(temp)

        line_group = []
        for i in range(n):
            line_group.append(Line(points[i][0], points[i + 1][0], color=BLACK))
        self.add(*line_group)
