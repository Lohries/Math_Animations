from manim import *
from pydub import AudioSegment
from pydub.playback import play

class IntroText(Scene):
    def construct(self):
        
        #Intro
        title = Text("Differential Equations applied in Engineering")
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
       
        description = Text(
            "Differential equations are the key to understanding the dynamic nature of engineering systems, providing a mathematical bridge to comprehend and design the behavior of complex physical phenomena.",
            font_size=100
        ).scale_to_fit_width(config.frame_width - 1)

  
        author = Text("William E. Boyce", font_size=50, slant=ITALIC)
        Poincare = Text("Henri Poincaré", font_size=50, slant=ITALIC)

        image_author = ImageMobject("author")
        Poincare_author = ImageMobject("Poincare")
        
       
        description.move_to(ORIGIN)
        
        author.next_to(description, DOWN, buff=0.5)  
        author.shift(DOWN * 1.5)
        image_author.next_to(author, UP, buff=0.5)  
        
        Poincare.next_to(description, DOWN, buff=0.5)
        Poincare.shift(DOWN * 1.5)
        Poincare_author.next_to(author, UP, buff=0.5)  
        
        #Graphs 
        axes = Axes(
            x_range= [-6, 6, 1],
            y_range= [-5, 5, 1],

            x_length= 6,
            y_length= 6,
            
            axis_config={"color": WHITE}

        )
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        solution1 = axes.plot(lambda x: 0, color=BLUE )
        solution2 = axes.plot(lambda x: 1, color=BLUE )
        point = Dot(axes.c2p(0.5, 0.5), color=RED)
        general = Text("Point (x0, y0)", font_size=25).next_to(point, RIGHT)
        generic_solution = axes.plot(lambda x: 1-x, color=RED, x_range=[0.25, 0.75, 1])
        
        

        
        #Fundamentals 
        definition = Text("In mathematics, a differential equation is an equation that relates one or more unknown functions and their derivatives. In applications, the functions generally represent physical quantities, the derivatives represent their rates of change, and the differential equation defines a relationship between the two.", font_size=100).scale_to_fit_width(config.frame_width - 1)
        definition.move_to(UP)


        theory = Text("Differencial Equation Qualitative Theory", font_size=50)
        theory.move_to(UP)
        theory_explanation = Text("The Qualitative Theory of Differential Equations focuses on understanding the behavior of solutions to differential equations without necessarily solving them explicitly", font_size=100).scale_to_fit_width(config.frame_width-1)
        theory_explanation.move_to(ORIGIN)
        theory_explanation.next_to(theory, DOWN, buff=0.5)
        
        
        
        
        
        #Calculations
        equation = MathTex(r"y = y^{1/2}")
        equation.move_to(UP*3.5)
        equation1 = MathTex(r"\frac{dy}{dx} = y^{1/2}")
        equation1.next_to(equation, DOWN)
        equation2 = MathTex(r"dy = y^{1/2} \, dx")
        equation2.next_to(equation1, DOWN)
        equation3 = MathTex(r"dy = \frac{dx}{y^{1/2}}")
        equation3.next_to(equation2, DOWN)
        equation4 = MathTex(r"dy = \frac{dx}{y^{-1/2}}")
        equation4.next_to(equation3, DOWN)
        equation5 = MathTex(r"\int dx = \int {y^{-1/2} dy")
        equation5.next_to(equation4, DOWN)
        equation6 = MathTex(r"x + C = \frac{y^{1/2}}{1/2} + C")
        equation6.move_to(UP*3.0)
        equation7 = MathTex(r"x + C = 2 \sqrt{y} + C")
        equation7.next_to(equation6, DOWN)
        equation8 = MathTex(r"\frac{x + C}{2} = \sqrt{y}")
        equation8.next_to(equation7, DOWN)
        equation9 = MathTex(r"\left(\frac{x + C}{2}\right)^2 = y")
        equation9.next_to(equation8, DOWN)
        explanation = Text("This simple exercise contains many solutions to each value of x. So given the infinite differential equations, the area of our study is not to determine de solution, but the ways that the equations can be manipulate.", font_size=100).scale_to_fit_width(config.frame_width-1)
        explanation.next_to(equation9, DOWN)
        

        
        
        #Solutions
        qualitative = Text("So let's put this in practise. First we gonna analyze an equation seeing through the old vision and then the new vision.", font_size=100).scale_to_fit_width(config.frame_width-1)
        qualitative.move_to(UP*3.5)
        eq_q1 = MathTex(r"x' = x(x-1)")

        dimensions = Text("We have only one dimenssion")
        dimensions.next_to(eq_q1, DOWN)
        order = Text("We got a first order equations as well")
        order.next_to(dimensions, DOWN)
        eq_q1.next_to(qualitative, DOWN)
        eq_q2 = MathTex(r"\frac{dx}{dy} = x(x-1)")
        eq_q2.next_to(eq_q1, DOWN)
        

      
        
        eq_q3 = MathTex(r"dx = x(x-1) \, dy")
        eq_q3.move_to(UP*3.5)

        eq_q4 = MathTex(r"\frac{dx}{x(x-1)} = dy")
        eq_q4.next_to(eq_q3, DOWN)

        eq_q5 = MathTex(r"\int \frac{dx}{x(x-1)} = \int dy")
        eq_q5.next_to(eq_q4, DOWN)
        
        eq_q6 = MathTex(r"\int \left(\frac{1}{x} - \frac{1}{x-1}\right) dx = \int dy")
        eq_q6.next_to(eq_q5, DOWN)
        
        
        eq_q7 = MathTex(r"\ln |x| - \ln |x-1| = y + C")
        eq_q7.move_to(UP*3.5)
        
        eq_q8 = MathTex(r"\ln \left|\frac{x}{x-1}\right| = y + C")
        eq_q8.next_to(eq_q7, DOWN)
        
        eq_q9 = MathTex(r"\frac{x}{x-1} = e^{y+C} = {e^y} {e^C}")
        eq_q9.next_to(eq_q8, DOWN)
        
        
        eq_q10 = MathTex(r"\frac{x}{x-1} = Ce^y")
        eq_q10.next_to(eq_q9, DOWN)
        
        
        eq_q11 = MathTex(r"x = {Ce^y}({x - 1})")
        eq_q11.next_to(eq_q10, DOWN)
        
        eq_q12 = MathTex(r"y = \ln \left( \frac{x}{x-1} \right) - \ln(C)")
        eq_q12.move_to(ORIGIN)
        
        eq_q13 = MathTex(r"y = \ln \left( \frac{x}{C(x-1)} \right)")
        eq_q13.next_to(eq_q12, DOWN)
        

        new_vision = Text("Qualitative Analyses")
        new_vision.move_to(UP*3.5)
        nw = MathTex(r"x' = x(x-1)")
        nw_v = MathTex(r"x = 0, \, F(y, 0) = 0, \, y(x) = 0 \, \text{is a solution}").next_to(nw, DOWN)
        nw_v2 = MathTex(r"x = 1, \, F(y, 1) = 1, \, y(x) = 1 \, \text{is a solution}").next_to(nw_v, DOWN)
        
        
        
        #Conclusion
        first_interval = Text("In the interval 0<x<1 we have F(x, y) < 0", color=RED)
        derivative_fisrt_interval = Text("Taking the derivative, we can see that x' < 0", color=BLUE)
        final_conclusion = Text("We can now prove that whenever the solution is x within the interval (0, 1), it will be descending.").scale_to_fit_width(config.frame_width-1)
        looking_tendecies = Text("Now with the other points, we can see that the points inside of the interval tends to converge to 0 and the externals to the interval tends to 0 or 1, relative if they are right from the interval or left", color=GREEN, font_size=80).scale_to_fit_width(config.frame_width-1)
        looking_tendecies.move_to(DOWN)

        
        
        first_interval.move_to(UP*3.0)
        derivative_fisrt_interval.next_to(first_interval, DOWN)
        
        
        # Animações

        #sound = AudioSegment.from_mp3("sounds.mp3")
        #play(sound)
  
        #self.play(music)

        self.play(Write(author))
        self.wait(5)
        
        self.play(FadeIn(image_author))  
        self.wait(8)
        self.play(FadeOut(author))
        self.play(FadeOut(image_author))
        self.play(Write(description))
        self.wait(8)
        self.play(FadeOut(description))
        #self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES) #phi - inclina theta - gira gamma - rotaciona
        #self.wait(2)
        #self.play(FadeIn(axes, graph))
        #self.wait(3)
        #self.play(FadeOut(axes, graph))

        #self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES, run_time=2)
        self.play(Write(definition))
        self.wait(5)
        self.play(FadeOut(definition))
        
        self.play(Write(equation))
        self.wait(2)
        self.play(Write(equation1))
        self.wait(2)
        self.play(Write(equation2))
        self.wait(2)
        self.play(Write(equation3))
        self.wait(3)
        self.play(Write(equation4))
        self.wait(2)
        self.play(Write(equation5))
        self.wait(2)
       
        self.play(FadeOut(equation, equation1, equation2, equation3, equation4, equation5))
        self.wait(2)
        self.play(Write(equation6))
        self.wait(2)
        self.play(Write(equation7))
        self.wait(2)
        self.play(Write(equation8))
        self.wait(2)
        self.play(Write(equation9))
        self.play(Write(explanation))
        self.wait(8)
        self.play(FadeOut(equation6, equation7, equation8, equation9, explanation))
        self.wait(3)
        self.play(Write(Poincare))
        self.play(FadeIn(Poincare_author))
        self.wait(4)
        self.play(FadeOut(Poincare, Poincare_author))
        self.play(Write(theory))
        self.play(Write(theory_explanation))
        self.wait(5)
        self.play(FadeOut(theory_explanation, theory))
        
        self.play(Write(qualitative))
        self.wait(3)
        self.play(Write(eq_q1))
        self.wait(3)
        self.play(Write(dimensions))
        self.play(Write(order))
        self.wait(3)
        self.play(Write(eq_q2))
        self.wait(3)
        self.play(FadeOut(qualitative, order, dimensions, eq_q1, eq_q2))
        self.wait(3)
        self.play(Write(eq_q3))
        self.wait(3)
        self.play(Write(eq_q4))
        self.wait(3)
        self.play(Write(eq_q5))
        self.wait(3)  
        self.play(Write(eq_q6))
        self.play(FadeOut(eq_q3, eq_q4, eq_q5, eq_q6))
        
        self.play(Write(eq_q7))
        self.wait(3)
        self.play(Write(eq_q8))
        self.wait(3)
        self.play(Write(eq_q9))
        self.wait(3)
        self.play(Write(eq_q10))
        self.wait(3)
        self.play(Write(eq_q11))
        self.wait(3)
        self.wait(2)
        self.play(FadeOut(eq_q7, eq_q8, eq_q9, eq_q10, eq_q11))
        self.wait(2)
        self.play(Write(eq_q12))
        self.wait(3)
        self.play(Write(eq_q13))
        self.play(FadeOut(eq_q12, eq_q13))
        
        self.play(Write(new_vision))
        self.play(Write(nw))
        self.play(Write(nw_v))
        self.play(Write(nw_v2))
        self.wait(5)
        
        self.play(FadeOut(new_vision, nw, nw_v, nw_v2))
        self.play(Write(axes), Write(labels), Write(solution1), Write(solution2), Write(point), Write(general), Write(generic_solution))
        self.wait(4)
        self.play(FadeOut(axes, labels, solution1, solution2,  point, general, generic_solution))
        self.wait(2)
        self.play(Write(first_interval), Write(derivative_fisrt_interval))
        self.wait(4)
        self.play(Write(final_conclusion))
        self.wait(4)
        self.play(Write(looking_tendecies))
        self.wait(4)
  
  
        
 
