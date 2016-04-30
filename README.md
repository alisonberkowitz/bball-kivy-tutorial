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
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
```