from manimlib import *
from yj.common.scene.link import LinkNode
from yj.common.utils.utils import get_rect2


class Test1(Scene):
    def construct(self):
        text = Text("123")
        self.add(get_rect2(text, buff=1, stroke_color=RED, stroke_width=6))
        self.add(text)
        self.add(ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/dx.jpeg"))
