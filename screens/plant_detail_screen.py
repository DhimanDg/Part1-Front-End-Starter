from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
import os


class PlantDetailScreen(Screen):

    pass



class DetailRow(ButtonBehavior, BoxLayout):
    title = StringProperty("Add Detail")
    subtitle = StringProperty("You can add a plant detail here")

    def on_press(self):
        self.opacity = 0
        return super().on_release()
    
    def on_release(self):
        self.opacity = 1
        return super().on_release()




Builder.load_file(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "plant_detail_screen.kv")
)