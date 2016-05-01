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