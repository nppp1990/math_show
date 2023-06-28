import numpy as np

from manimlib import *


def get_angle(p1, p2, center):
    return np.arctan2(p2[1] - center[1], p2[0] - center[0]) - np.arctan2(p1[1] - center[1], p1[0] - center[0])


class Test(Scene):

    def construct(self):
        earh = VGroup(Circle(stroke_color=BLUE, stroke_width=6), Text("地球", font_size=30)).scale(0.7)
        self.add(earh)

        line1 = Line(ORIGIN, RIGHT * 1.2, color=YELLOW, stroke_width=8).add_tip(width=0.3, length=0.3).shift(LEFT * 6)
        line = VGroup(
            line1.copy().shift(UP * 2),
            line1.copy().shift(UP * 1),
            line1,
            line1.copy().shift(DOWN * 1),
            line1.copy().shift(DOWN * 2),
        )
        self.play(FadeIn(VGroup(line)), FadeIn(Text("太阳光", color=YELLOW_A).scale(0.7).next_to(line, UP)))
        self.wait()

        track = Circle(stroke_color=WHITE, stroke_width=0.5).scale(3.8)
        moon_circle = Circle(stroke_color=BLACK, stroke_width=4).scale(0.3).move_to(track.get_left())
        moon_arc = Sector(outer_radius=moon_circle.get_radius(), angle=PI,
                          start_angle=PI / 2,
                          fill_color=YELLOW, arc_center=moon_circle.get_center())
        moon = VGroup(moon_arc, moon_circle)
        moon_text = Text("月球", font_size=60).scale(0.3)
        always(moon_text.next_to, moon, LEFT * 0.3)

        self.play(FadeIn(moon_text), FadeIn(moon), FadeIn(track))
        self.wait(2)
        arc1 = Arc(radius=track.get_radius(), angle=PI / 4, stroke_width=0).rotate(
            PI, about_point=earh.get_center())

        self.play(MoveAlongPath(moon, arc1), run_time=2)
        head_img = ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/dx.jpeg").scale(0.1)
        self.play(
            FadeOut(earh, run_time=1),
            FadeIn(head_img, run_time=1),
            moon.scale, 4, run_time=3
        )
        self.wait()

        line_vector = Line(moon.get_center(), head_img)
        unit_vector = line_vector.get_unit_vector()
        # 垂直向量
        unit_vector2 = np.array([-unit_vector[1], unit_vector[0], 0])
        print(unit_vector)
        line_arrow1 = Line(line_vector.get_start() + 1.5 * unit_vector, line_vector.get_end() - 0.5 * unit_vector,
                           color=YELLOW, stroke_width=8).add_tip(width=0.3, length=0.3)
        line_arrow = VGroup(line_arrow1.copy().shift(unit_vector2 * 0.7),
                            line_arrow1,
                            line_arrow1.copy().shift(unit_vector2 * -0.7))
        self.play(ShowCreation(line_arrow))
        self.wait(3)

        moon_radius = moon[1].get_radius()
        view_line = Line(moon.get_center() + unit_vector2 * (moon_radius + 0.4),
                         moon.get_center() - unit_vector2 * (moon_radius + 0.4))
        self.play(ShowCreation(view_line), run_time=3)
        self.wait(3)

        poi1 = moon.get_center() + unit_vector2 * moon_radius
        poi2 = moon[1].get_center() + UP * moon_radius

        view_arc = ArcBetweenPoints(
            start=poi1,
            end=poi2,
            angle=get_angle(poi1, poi2, moon.get_center()),
            color=WHITE, stroke_width=8)
        self.play(ShowCreation(view_arc), run_time=3)

        self.wait(3)

        moon_demo = ImageMobject("/Users/yuanjian/Downloads/py-project/manim/assets/images/moon_demo.png").shift(
            RIGHT * 5)
        self.play(ShowCreation(moon_demo))
        self.wait(5)
