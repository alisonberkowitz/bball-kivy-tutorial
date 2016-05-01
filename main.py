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