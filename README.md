# EmptyRepo
vskutku

vskutku budeme používat redis lol
yo zde je nějakej redis setup:
´´´
$ curl -s -o redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
$ sudo su root
$ mkdir -p /usr/local/lib/
$ chmod a+w /usr/local/lib/
$ tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
$ rm redis-stable.tar.gz
$ cd /usr/local/lib/redis-stable/
$ make && make install
´´´