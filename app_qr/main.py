from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.utils import platform
from kivy.clock import Clock
from kivy.uix.button import Button
from android_permissions import AndroidPermissions
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import webbrowser
from kivy.clock import mainthread
from kivy.metrics import dp
from kivy.graphics import Line, Color, Rectangle
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from gestures4kivy import CommonGestures
from camera4kivy import Preview
from kivy.core.window import Window
from kivy.core.window import Window

global name
global last
Window.show()

if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android import mActivity
    View = autoclass('android.view.View')

    @run_on_ui_thread
    def hide_landscape_status_bar(instance, width, height):
        # width,height gives false layout events, on pinch/spread
        # so use Window.width and Window.height
        if Window.width > Window.height:
            # Hide status bar
            option = View.SYSTEM_UI_FLAG_FULLSCREEN
        else:
            # Show status bar
            option = View.SYSTEM_UI_FLAG_VISIBLE
        mActivity.getWindow().getDecorView().setSystemUiVisibility(option)
elif platform != 'ios':
    # Dispose of that nasty red dot, required for gestures4kivy.
    from kivy.config import Config
    Config.set('input', 'mouse', 'mouse, disable_multitouch')


class QRReader(Preview, CommonGestures):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.annotations = []


    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):


        pil_image = Image.frombytes(mode='RGBA', size=image_size, data= pixels)
        barcodes = pyzbar.decode(pil_image, symbols=[ZBarSymbol.QRCODE])
        found = []
        for barcode in barcodes:
            text = barcode.data.decode('utf-8')
            print(text)
            if text == "SuperQRcode":
                global name
                global last
                Window.close()
                print("closed")
                
                #else get new

class MyApp(App):
    def build(self):
        self.qrreader = QRReader(letterbox_color = 'black',aspect_ratio = '16:9')
        if platform == 'android':
            Window.bind(on_resize=hide_landscape_status_bar)
        return self.qrreader

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def start_app(self):
        self.dont_gc = None
        # Can't connect camera till after on_start()
        Clock.schedule_once(self.connect_camera)

    def connect_camera(self,dt):
        self.qrreader.connect_camera(analyze_pixels_resolution = 640,
                                     enable_analyze_pixels = True)

    def on_stop(self):
        self.qrreader.disconnect_camera()

class RegGrid(GridLayout):
    def __init__(self, **kwargs):
        super(RegGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        global name
        global last
        name = self.name.text
        last = self.lastName.text
        if name == "" or last == "" :
            print("write please data")
        else:
            print("Name:", name, "Last Name:", last)
            MyApp().run()

class Place(App):
    def build(self):
        layout = BoxLayout(padding=100,orientation = 'vertical')
        place = Label(text='Place',font_size=40)
        numbeP = Label(text='10',font_size=60)
        layout.add_widget(place)
        layout.add_widget(numbeP)
        time = Label(text='time',font_size=40)
        numbeT = Label(text='10 years',font_size=60)
        layout.add_widget(time)
        layout.add_widget(numbeT)
        return layout

class Register(App):

    def build(self):
        return RegGrid()

class first(App):
    def build(self):
        global layout
        layout = BoxLayout(padding=100)
        button = Button(text='Start',font_size=40, on_press=self.callback)
        layout.add_widget(button)
        return layout


    def callback(self, event):
        global layout
        layout.clear_widgets()
        layout = BoxLayout(padding=100,orientation = 'vertical')
        place = Label(text='Place',font_size=40)
        numbeP = Label(text='10',font_size=60)
        layout.add_widget(place)
        layout.add_widget(numbeP)
        time = Label(text='time',font_size=40)
        numbeT = Label(text='10 years',font_size=60)
        layout.add_widget(time)
        layout.add_widget(numbeT)
        print("button pressed")
        Register().run()
        return layout

first().run()
