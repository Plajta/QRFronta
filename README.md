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
