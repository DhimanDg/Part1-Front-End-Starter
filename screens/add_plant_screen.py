
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
import os


class AddPlantScreen(Screen):

    pass



class PlantnameRow(ButtonBehavior, BoxLayout):
    title = StringProperty("Add Plant")
    subtitle = StringProperty("You can add a new plant here")

    def on_press(self):
        self.opacity = 0.85
        return super().on_press()
    
    def on_release(self):
        self.opacity = 1
        return super().on_release()




Builder.load_file(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "add_plant_screen.kv")
)