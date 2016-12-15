#!python3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class StartScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")

class MainApp(App):
    
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()
