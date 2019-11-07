import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.gridlayout import GridLayout

class Deepak(GridLayout):
	pass
		

class Dhristi(App):
	def build(self):
		title = "Dhristi"
		Window.clearcolor = get_color_from_hex('#FFFFFF')
		return Deepak() 

if __name__ == "__main__":
	Dhristi().run()