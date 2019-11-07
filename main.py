import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class Deepak(GridLayout):

	name = ObjectProperty(None)
	email1 = ObjectProperty(None)
	number1 = ObjectProperty(None)
	orga1 = ObjectProperty(None)

	def btn(self):
		print("Name : " , self.name.text,"email : " , self.email.text,"Number : " , self.number.text,"Organisation : " , self.orga.text)
		

	pass
		

class Dhristi(App):
	def build(self):
		title = "Dhristi"
		Window.clearcolor = get_color_from_hex('#FFFFFF')
		return Deepak() 

if __name__ == "__main__":
	Dhristi().run()