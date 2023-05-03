# Lab07

## PoC

[FILE](/out/crashes/id:000000,sig:06,src:000000,op:flip1,pos:18)

```
$ ./bmpgrayscale out/crashes/id\:000000* a.bmp
```

## Commands

```
$ cd ~
$ git clone https://github.com/google/AFL.git
$ cd AFL/
$ make
$ sudo make install
$ cd ~
$ cd /Users/alardutp/Documents/NYCU/ST/labs/Lab07/
$ export CC=afl-gcc
$ export AFL_USE_ASAN=1
$ make
$ mkdir in
$ mv test.bmp in
$ afl-fuzz -i in -o out -m none -- ./bmpgrayscale @@ a.bmp
$ ./bmpgrayscale out/crashes/id\:000000* a.bmp
```

## Screenshots

### fuzzing

![](/Screenshot1.png)

### crash

![](/Screenshot2.png)