
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder

Builder.load_file('layout/menuscreen.kv')
Builder.load_file('layout/scanscreen.kv')

class MenuScreen(Screen):

    def add_server(self):
        print "doing"

    def scan_mode_on(self):
        pass

    def scan_mode_off(self):
        pass

    def start_cam(self):
        pass

    def exit(self):
        App.get_running_app().stop()


class ScanScreen(Screen):

    pass

class CameraPreview(FloatLayout):

    def __init__(self,*args,**kwargs):
        cam = Camera(resolution=(640,480), size=(500,500))
        self.add_widget()
        return super(self,CameraPreview).__init__(*args, **kwargs)

class RootScreen(ScreenManager):
    kv_directory = 'layout'

    pass


class PictureTakerApp(App):
    kv_directory = 'layout'
    sm = ObjectProperty()
    
    def build(self):
        # Create the screen manager
        sm = RootScreen()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ScanScreen(name='scan'))
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    PictureTakerApp().run()