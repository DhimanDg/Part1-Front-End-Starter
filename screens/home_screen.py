from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
import os

class HomeScreen(Screen):
    pass

class PotListItem(ButtonBehavior, BoxLayout):
    file_name = StringProperty("daisy.png")

    def on_press(self):
        return super().on_press()
    
    def on_release(self):
        return super().on_release()

Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\home_screen.kv')