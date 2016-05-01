# Basketball Game with the Kivy Python library

## Installation
First make sure you have python installed, 2.7 is the strongly recommended version

Next install Kivy with the following commands from your command line:
```
pip install cython
pip install hg+http://bitbucket.org/pygame/pygame #i did apt-get install python-pygame
pip install kivy #i did apt-get install python-kivy
```
You may need to use the `sudo` command before pip for a successful install

## Hello World
Save the following into a text file titled `main.py`
```
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label


class BasketballApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    BasketballApp().run()
```
Now from your command line, run `python main.py`
Congratulations! You have run your first Kivy app :)
Let's break it down:
- The first few lines of the code are just imports, these tell python that we are using
the Kivy library
- The next part is a class definition. The App class in Kivy does a thing, so we inherit it. Right now,
our app returns the text "Hello World" That is what you see on the screen when you run it
- Finally, we run our app. Explain `if __name__ == '__main__':`

Now that you've done "Hello World", lets make our app into a Basketball Game.

## Setting Up the Basketball Game
We first need to add a BasketballGame widget to our app. A Widget is Kivy's class for ...
 In `main.py` add the class like so:

```
class BasketballGame(Widget):
    pass
```

Now, instead of returning the text 'Hello World' when we build the app, we want to return
an instance of our BasketballGame widget. Since we are no longer using Kivy's label class, 
but are now using Kivy's widget class, we want to change the import label to import widget.
It should now look like this:
<!-- explain what an instance and a class is? -->

```
import kivy
kivy.require('1.0.6') 

from kivy.app import App
from kivy.uix.widget import Widget

class BasketballGame(Widget):
	pass
		

class BasketballApp(App):

    def build(self):
        return BasketballGame()


if __name__ == '__main__':
    BasketballApp().run()
```

## Adding a Hoop
In our game, we will have a hoop and a score. We draw these by defining how the `BasketballGame widget`
looks. This is done in a new file called `basketball.kv` that will be automatically loaded when the 
application is run. In the same directory as your `main.py`, create a file called `basketball.kv` and 
add the following:

```
<BasketballGame>:    
    canvas:
        Rectangle:
            pos: self.center_x - 100, self.top - 200
            size: 200, 100

        Color:
            rgb: 1, 0, 0
        Rectangle:
            pos: self.center_x - 50, self.top - 200
            size: 100, 10

    Label:
        font_size: 70  
        center_x: root.width / 2
        top: root.center_y
        text: "0"
```
Now run the app from your command line with `python main.py`. You should see a hoop made of a white 
rectangle as the backboard and a red rectangle as the rim, and a zero that will display the score.

## Adding the Ball
Now we have a hoop, but we still need a ball to shoot. Let's add a `Ball` class to create a widget 
that will be our ball.

Add this to your `main.py` file:
```
class Ball(Widget):
	pass
```

And this to your `basketball.kv` file:
```
<Ball>:
    size: 50, 50
    canvas:
    	Color: 
    		rgb: 1, .65, 0
        Ellipse:
            pos: self.pos
            size: self.size
```

Now make sure to reference your ball in your game: `ball = ObjectProperty(None)`
Add the following line to your imports: `from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty`

Don’t forget to hook it up in the kv file, by giving the child widget an id and 
setting the BasketballGame’s ball ObjectProperty to that id:
```
<BasketballGame>:
    ball: game_ball

    # ... (canvas and Labels)

    Ball:
        id: game_ball
        center_x: self.parent.center_x
        top: 50
```
To review, you should have two files in your directory, one `main.py` that should look like this:
```
import kivy
kivy.require('1.0.6') 

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty

class Ball(Widget):
	pass
		

class BasketballGame(Widget):
	ball = ObjectProperty(None)
		

class BasketballApp(App):

    def build(self):
        return BasketballGame()


if __name__ == '__main__':
    BasketballApp().run()
```
and a `basketball.kv` that should look like this:
```
<BasketballGame>:  
    ball: game_ball

    canvas:
        Rectangle:
            pos: self.center_x - 100, self.top - 200
            size: 200, 100

        Color:
            rgb: 1, 0, 0
        Rectangle:
            pos: self.center_x - 50, self.top - 200
            size: 100, 10

    Label:
        font_size: 70  
        center_x: root.width / 2
        top: root.center_y
        text: "0"

    Ball:
        id: game_ball
        center_x: self.parent.center_x
        top: 50  
        
<Ball>:
    size: 50, 50
    canvas:
        Color: 
            rgb: 1, .65, 0
        Ellipse:
            pos: self.pos
            size: self.size
```
Now when you run `python main.py` from the command line, you should have a hoop and a ball!

## Shooting the Ball
Now that we have all of our equipment set up, we need to make our game interactive and take 
user input so we can shoot the ball.

We need the game to update so we add
```
Clock.schedule_interval(game.update, 1.0/60.0)
```

... After this step the `main.py` should look like this:

```
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
```