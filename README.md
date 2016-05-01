# Basketball Game with the Kivy Python library

## Installation
First make sure you have python installed

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

```class BasketballGame(Widget):
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