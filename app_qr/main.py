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

import base64, socket

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

        pil_image = Image.frombytes(mode='RGBA', size=image_size, data=pixels)
        barcodes = pyzbar.decode(pil_image, symbols=[ZBarSymbol.QRCODE])
        found = []
        for barcode in barcodes:
            text = barcode.data.decode('utf-8')

            global name
            global last
            global gotit

            try:
                if gotit == 1:
                    print("1")
                    return
                elif gotit == 0:
                    gotit = 1
                    print(text)
                else:
                    print("2")
                    return
                proj, queue, ip, port = text.split(";")
                print(proj, queue, ip, port)
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect((ip, int(port)))

                data = "new-user;" + base64.b64encode(f"{name} {last}".encode("utf-8")).decode("utf-8")
                clientSocket.send(data.encode())
                dataFromServer = clientSocket.recv(1024)
                uid = dataFromServer.decode()
                print(uid)

                with open("HopeIllNeverDeleteItAgain.txt", "w") as f:
                    f.write(f"{text};{uid}\n")

            except Exception as E:
                print(E)

            if text == "SuperQRcode":
                if gotit == 1:
                    print("1")
                elif gotit == 0:
                    gotit = 1
                    print(text)
                else:
                    print("2")

                # else get new


def my_callback(dt):
    global gotit
    global disconnectcamera
    if gotit == 1:
        gotit = 2
        print("change")
        Placet().run()
        print("disconect")
        disconnectcamera.qrreader.disconnect_camera()
        print("disconected")


class MyApp(App):
    def build(self):
        self.qrreader = QRReader(letterbox_color='black', aspect_ratio='16:9')
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

    def connect_camera(self, dt):
        self.qrreader.connect_camera(analyze_pixels_resolution=640,
                                     enable_analyze_pixels=True)

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
        if name == "" or last == "":
            print("write please data")
        else:
            print("Name:", name, "Last Name:", last)
            self.remove_widget(self.submit)
            MyApp().run()


Floatplace = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size

    Label:
        text:"you are in last pleace"
''')


class Placet(App):
    def build(self):
        return Floatplace


class Register(App):

    def build(self):
        return RegGrid()


class first(App):
    def build(self):
        global layout
        layout = BoxLayout(padding=100)
        button = Button(text='Start', font_size=40, on_press=self.callback)
        layout.add_widget(button)
        return layout

    def callback(self, event):
        global layout
        layout.clear_widgets()
        layout = BoxLayout(padding=100, orientation='vertical')
        place = Label(text='Place', font_size=40)
        numbeP = Label(text='10', font_size=60)
        layout.add_widget(place)
        layout.add_widget(numbeP)
        time = Label(text='time', font_size=40)
        numbeT = Label(text='10 years', font_size=60)
        layout.add_widget(time)
        layout.add_widget(numbeT)
        print("button pressed")
        Register().run()
        return layout


with open("HopeIllNeverDeleteItAgain.txt", "r") as f:
    if f is not None:
        gotit = 2
if gotit == 2:
    Placet().run()
else:
    first().run()
