# Frequonta
Toto je software vytvořený na Co - Heckathonu v prosinci 2022 na SPŠE Plzeň.
Jedná se o virtuální frontu do které se přihlásíte naskenováním QR códu v mobilní aplikaci. Vidíte kolikátí ve frontě jste a aproximaci času kdy se dostanete na řadu. Máme zde i webový server s admin stránkou pro správu front.


# Tutoriál pro instalaci databáze redis
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

install camera4kivy

nainstaluje čtečku qr kódů a kivy 

## Windows      to jen pro Windows

`pip3 install pillow pyzbar camera4kivy`

## MacOS        to jen pro Mac 
`brew install zbar`

`pip3 install pillow pyzbar camera4kivy`

## Linux      to jen pro linux

`sudo apt-get install libzbar0`

`pip3 install pillow pyzbar camera4kivy`

## Android

Camera4Kivy závisí Buildozer 1.3.0 nebo pozdějších verzích

`pip3 install buildozer`

`sudo apt-get install gettext`  některá zařízení mají již nainstalováno ovšem dejte si pozor že u vás je instalován v opačném případě nazaručujeme funkčnost.

Tento příklad obsahuje [camera provider](https://github.com/Android-for-Python/camera4kivy#android-camera-provider) a také [buildozer.spec](https://github.com/Android-for-Python/camera4kivy#buildozerspec).

## Camera Provider

Camera4Kivy závysí na 'camera provider' pro zpřístupnění OS api. Na většině platforem využívá stejného přístupu jako Kivy, s upravenými defaultními hodnotami.

| Platforma   | Poskytovatel  | Požadavky      |
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

### OpenCV          pro startovani na linuxu

`pip3 install opencv-python`

### GStreamer         taky pro linux

Záleží na příchuti vašeho LInuxu, ale ve většině případů:

`sudo apt-get install gstreamer-1.0`

`sudo apt-get install gstreamer1.0-dev`     

používali jsme tyto package: 
`flask`, `flask-socketio`, `gevent-websocket`, `eventlet`, `redis`