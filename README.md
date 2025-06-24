MFOC is an open source implementation of "offline nested" attack by Nethemba.
Later was added so called "hardnested" attack by Carlo Meijer and Roel Verdult.

This program allow to recover authentication keys from MIFARE Classic card.

Please note MFOC is able to recover keys from target only if it have a known key: default one (hardcoded in MFOC) or custom one (user provided using command line).

This is a port to win32 x64 platform using native tools (Visual Studio 2019 + LLVM clang-cl toolchain).
This tree was also reworked for gnu toolchain (autotool + gcc like the original).
 
Based on the idea by vk496 to integrate mylazycracker into mfoc, forked from his tree.

For credits (there are many) just look at the AUTHORS file.

Uses 
		libnfc 			https://github.com/nfc-tools/libnfc/
		libusb-win32 	https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/
		pthreads4w		https://sourceforge.net/projects/pthreads4w/
		liblzma			https://tukaani.org/xz/

pthreads4w and liblzma are static linked.
All these libs are precompiled and included in src\lib

# Build from source
Windows:
Make sure you have Visual Studio 2019 with Desktop developement with C++, C++ Clang Compiler for Windows and C++ Clang-cl for v142 build tools installed.
Open the solution and start compile.
The compiled zip package will be in dist.

Linux:
```
autoreconf -vis
./configure
make && sudo make install
```

# Usage #
Needs libusb0.dll and nfc.dll in the path, better on the same directory.
Needs to install libusbK v3.0.7.0, using Zadig https://zadig.akeo.ie/, go to Option, List All Devices, select your reader, select libusbK(v3.0.7.0) and click on replace driver.
Then go in device manager and disable "Allow the computer to turn off this device to save power" in your reader under libusbK USB Devices.
Put one MIFARE Classic tag that you want keys recovering;
Lauching mfoc, you will need to pass options, see:
```
mfoc-hardnested -h
```
to copy a new card you can use :
```
mfoc-hardnested -O mycard.mfd -k keys.txt -P 500 -T 5
```
you will get an output in the terminal, save it as you will need it later, if the card you are copying has the same number of sectors as the one your are copying to you can directly use this command to write to the new card :
```
nfc-mfclassic W a mycard.mfd
```
if the cards have different sector numbers, the card you are copying to needs to have a larger number of sectors, and you MUST create a new .mfd file to make the old dump the same size expected by nfc-mfclassic, to do that, modify the python script named padding.py to use the actual data you copied from your terminal earlier and run it, this will create a 1K .mfd file (the most common size in chinese NFC clones) and then run the following command to write it to your new blank card :

```
nfc-mfclassic W a mycard_1k.mfd
```
