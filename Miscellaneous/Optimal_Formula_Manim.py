from manim import *

class TNAnimation(Scene):
    def construct(self):
        # Create the formula
        formula = MathTex(r'Tn = 4n - 3')
        '''Part 1'''
        self.play(Write(formula))
        self.wait()
        self.play(FadeOut(formula))
        # set up parametres for part 2
        ax = Axes(
            x_range = [0, 5, 1],
            y_range = [0, 15, 1],
            x_length = 5,
            y_length = 5,
            axis_config = {'include_numbers': True},
        )
        '''part 2'''
        func = lambda x: ((4*x) - 3)
        curve = ax.plot(func, color = YELLOW)
        self.play(Create(ax))
        self.play(Write(curve))
        self.wait()
        self.play(FadeOut(curve, ax))

# Without this clause I had to run the file from the command line and add -p to open it in a video editor
if __name__ == "__main__":
    TNAnimation().render()
