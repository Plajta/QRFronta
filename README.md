# EmptyRepo
vskutku

vskutku budeme používat redis lol
yo zde je nějakej redis setup:
```
$ curl -s -o redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
$ sudo su root
$ mkdir -p /usr/local/lib/
$ chmod a+w /usr/local/lib/
$ tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
$ rm redis-stable.tar.gz
$ cd /usr/local/lib/redis-stable/
$ make && make install
```

poté co tohle máme, tak redis spustíme:
`redis-server`

pokud chceme dělat nějaké queries do databáze:
`redis-cli`

# Android QR app

install qr_code app

have been installed kivy

install camera4kivy

## Windows

`pip3 install pillow pyzbar camera4kivy`

## MacOS

`brew install zbar`

`pip3 install pillow pyzbar camera4kivy`

## Linux

`sudo apt-get install libzbar0`

`pip3 install pillow pyzbar camera4kivy`

## Android

Camera4Kivy depends on Buildozer 1.3.0 or later

`pip3 install buildozer`

`sudo apt-get install gettext`  some hosts already have this installed.

The example includes a [camera provider](https://github.com/Android-for-Python/camera4kivy#android-camera-provider) and a [buildozer.spec](https://github.com/Android-for-Python/camera4kivy#buildozerspec).

## Camera Provider

Camera4Kivy depends on a 'camera provider' to access the OS camera api. On most platforms this uses the same provider as Kivy, with modified defaults.

| Platform    | Provider      | Requires       |
|-------------|---------------|----------------|
| Windows     | [OpenCV](https://github.com/Android-for-Python/camera4kivy#opencv)                      |
|             | [Gstreamer](https://github.com/Android-for-Python/camera4kivy#gstreamer)                      |
| Macos       | [AVFoundation](https://github.com/Android-for-Python/camera4kivy#avfoundation)| OSX >= 10.7    |   
| Linux       | [Gstreamer](https://github.com/Android-for-Python/camera4kivy#gstreamer)                      |
|             | [OpenCV](https://github.com/Android-for-Python/camera4kivy#opencv)                      |
| Rasberry    | [Picamera](https://github.com/Android-for-Python/camera4kivy#picamera)    | <= Buster      |
|             | [Gstreamer](https://github.com/Android-for-Python/camera4kivy#gstreamer)  |  <= Buster |
|             |[OpenCV](https://github.com/Android-for-Python/camera4kivy#opencv) |  <= Buster  |
|             | [Picamera2](https://github.com/Android-for-Python/camera4kivy#picamera2)    | >= Bullseye      |
| Android     | [CameraX](https://github.com/Android-for-Python/camera4kivy#android-camera-provider)                      |  Android >= 5.0 |
| iOS         | [AVFoundation](https://github.com/Android-for-Python/camera4kivy#avfoundation)                      |

Like Kivy, the first available provider is selected. Some camera provider specific behavior should be expected. For example a switch to a camera that does not exist will be ignored on MacOS and Rasberry Pi, but generate a screen message with OpenCV or GStreamer. Camera resolution defaults to the maximum available camera provider resolution, except on Raspberry Pi where the default is (1024, 768).

You can remove a camera provider ('picamera' in the example below) from the above lists by inserting this code **before** `from kivy.app import App`.

```python
from kivy import kivy_options
providers= list(kivy_options['camera'])
providers.remove('picamera')
kivy_options['camera'] = tuple(providers)
```

### Android Camera Provider

`cd <project directory>`

`git clone https://github.com/Android-for-Python/camerax_provider.git`

`rm -rf camerax_provider/.git`

Set `p4a.hook` to enable the app's use of the camera provider.

`p4a.hook = camerax_provider/gradle_options.py`

### OpenCV

`pip3 install opencv-python`

### GStreamer

Depends on the Linux flavor, but commonly:

`sudo apt-get install gstreamer-1.0`

`sudo apt-get install gstreamer1.0-dev`

