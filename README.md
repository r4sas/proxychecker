Proxy checker
=====

Written on python, requires at least version 3.4.

For work needed PySocks and urllib3, install it with pip:
```
$ python3 -m pip install PySocks
$ python3 -m pip install urllib3
```

That script written primary for checking I2P proxy tunnels.

Configuring
-----

Fill `list.ini` with your tunnels options as in example file.

At same time you need that tunnels configured in your tunnels.conf (i2pd) or tunnels page (i2p).

Example for *false.i2p* outproxy usage in i2pd:
```
[FALSE]
type = httpproxy
address = 127.0.0.1
port = 4450
outproxy = http://77mpz4z6s4eenjexleclqb36uxvqjtztqikjfqa4sovojh6gwwha.b32.i2p
keys = false.dat
```

And, according to that tunnel, proxy checker config:
```
[4450]
type    = http
address = 77mpz4z6s4eenjexleclqb36uxvqjtztqikjfqa4sovojh6gwwha.b32.i2p
name    = false.i2p
owner   = meeh
info    = httpproxy
```

**Note that fields PORT and TYPE is required!** Other fields is not required and used only for filling table output.
