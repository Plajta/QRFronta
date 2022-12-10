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
from kivy.core.image import Image as CoreImage
from kivy.uix.image import AsyncImage
global gotit
gotit = 0
global name
global last





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

            if text == "SuperQRcode":
                global name
                global last
                global gotit
                if gotit == 1:
                    print("1")
                elif gotit == 0:
                    gotit = 1
                    print(text)
                else:
                    print("2")



                #else get new
def my_callback(dt):
    global gotit
    global disconnectcamera
    if gotit==1:
        gotit = 2
        print("change")
        Placet().run()
        print("disconect")
        disconnectcamera.qrreader.disconnect_camera()
        print("disconected")

class MyApp(App):
    def build(self):
        self.qrreader = QRReader(letterbox_color = 'black',aspect_ratio = '16:9')
        if platform == 'android':
            Window.bind(on_resize=hide_landscape_status_bar)
            global gotit
        return self.qrreader

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def start_app(self):
        self.dont_gc = None
        # Can't connect camera till after on_start()
        event = Clock.schedule_once(self.connect_camera)
        Clock.schedule_interval(my_callback, 0.1)

    def connect_camera(self,dt):
        self.qrreader.connect_camera(analyze_pixels_resolution = 640,
                                     enable_analyze_pixels = True)

    def on_stop(self):
        global disconnectcamera
        disconnectcamera = self
        self.qrreader.disconnect_camera()


class RegGrid(GridLayout):
    def __init__(self, **kwargs):
        super(RegGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: ",font_size=80,size_hint=(.05, .1),padding_y=50))
        self.name = TextInput(multiline=False,font_size=80,size_hint=(.05, .1))
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: ",font_size=80,size_hint=(.05, .1)))
        self.lastName = TextInput(multiline=False,font_size=80,size_hint=(.05, .1))
        self.inside.add_widget(self.lastName)

        self.add_widget(self.inside)

        self.submit = Button(text="Scan QR", font_size=80,size_hint=(.05, .1))
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
            self.remove_widget(self.submit)
            MyApp().run()


class PleaceGrid(GridLayout):
    def __init__(self, **kwargs):
        super(PleaceGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="Your Place: ", font_size=80))
        self.inside.add_widget(Label(text="10", font_size=160))
        self.inside.add_widget(Label(text="Your left time: ", font_size=80))
        self.inside.add_widget(Label(text="20m", font_size=160))
        self.canvas.add(Color(0, 0, 0))
        self.canvas.add(Rectangle(size=(5000, 5000)))
        self.add_widget(self.inside)

class firstGrid(BoxLayout):
    def __init__(self, **kwargs):
        super(firstGrid, self).__init__(**kwargs)
        self.inside = GridLayout()
        self.inside.cols = 1
        self.inside.add_widget(AsyncImage(source ='./Q-lite.png'))
        self.submit = Button(text="Go To Be Faster", font_size=80,size_hint=(.05, .1))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, soms):
        self.remove_widget(self.submit)
        Register().run()



class Placet(App):
    def build(self):
        return PleaceGrid()


class Register(App):

    def build(self):
        return RegGrid()

class first(App):
    def build(self):
        return firstGrid()


first().run()
