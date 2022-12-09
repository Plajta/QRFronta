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

## Windows      to jen pro okna

`pip3 install pillow pyzbar camera4kivy`

## MacOS         tohle nikdo ne ma

`brew install zbar`

`pip3 install pillow pyzbar camera4kivy`

## Linux      to jen pro linux

`sudo apt-get install libzbar0`

`pip3 install pillow pyzbar camera4kivy`

## Android

Camera4Kivy depends on Buildozer 1.3.0 or later

`pip3 install buildozer`

`sudo apt-get install gettext`  some hosts already have this installed. bez toho u mě nefungovalo

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


### Android Camera Provider    to musi byt v každem projektu

`cd <project directory>`

`git clone https://github.com/Android-for-Python/camerax_provider.git`

`rm -rf camerax_provider/.git`

### OpenCV          pro startovani na linuksu

`pip3 install opencv-python`

### GStreamer         taky pro linuks

Depends on the Linux flavor, but commonly:

`sudo apt-get install gstreamer-1.0`

`sudo apt-get install gstreamer1.0-dev`     

