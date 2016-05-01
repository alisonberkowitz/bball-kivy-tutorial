import kivy
kivy.require('1.0.6') 
import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector

class Ball(Widget):
	# velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def shoot_ball(self,angle):
        self.velocity = Vector(4, 0).rotate(angle)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # if the touch collides with our widget, let's grab it
            touch.grab(self)

            # record where the touch started
            self.start_shot = touch.pos

	        # and accept the touch.
            return True

    def on_touch_up(self,touch):
        if touch.grab_current is self:
            dif_x = touch.x - self.start_shot[0]
            dif_y = touch.y - self.start_shot[1]
            angle = math.degrees(math.atan (dif_y/dif_x))
            if dif_x < 0:
            	angle += 180
            self.shoot_ball(angle)
		

class BasketballGame(Widget):
    ball = ObjectProperty(None)

    def update(self, dt):
        self.ball.move()

        # land on bottom
        if (self.ball.y < 0):
        	# self.ball.center_x = self.center_x
        	self.ball.top = 50
        	self.ball.velocity_x = 0
        	self.ball.velocity_y = 0

        # bounce off top
        if (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
		

class BasketballApp(App):

    def build(self):
        game = BasketballGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    BasketballApp().run()