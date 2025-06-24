# MFOC-Hardnested (with Cross-Card-Size Copy Support)

**MFOC** is an open-source implementation of the “offline nested” attack on MIFARE Classic cards, originally developed by **Nethemba**. It was later extended to include the powerful **hardnested** attack, designed by **Carlo Meijer** and **Roel Verdult**.

this project includes a complete **Win32 x64 port** using native Windows tools and builds with **Visual Studio 2019** and the **LLVM `clang-cl`** toolchain. GNU toolchain support is maintained using `autotools` + `gcc` (as in the original project).

This fork by **Amine Mahdane** introduces **support for copying across different MIFARE Classic card sizes**, such as:

* 1K → 4K
* 320B (Mini) → 1K or 4K

---

## ⚠️ Disclaimer

MFOC can **only recover keys** from a MIFARE Classic tag **if at least one sector uses a known key**:

* A **default key** (already built into MFOC), or
* A **custom key** provided by the user via command-line.

---

## 🔧 Features

* Hardnested attack support
* Cross-size cloning support (Mini to 1K/4K, 1K to 4K)
* Compatible with `nfc-mfclassic` for writing `.mfd` dumps
* Includes precompiled dependencies for Windows build

---

## 📦 Dependencies

* [`libnfc`](https://github.com/nfc-tools/libnfc/)
* [`libusb-win32`](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/)
* [`pthreads4w`](https://sourceforge.net/projects/pthreads4w/)
* [`liblzma`](https://tukaani.org/xz/)

> **Note:** `pthreads4w` and `liblzma` are statically linked. All required libraries are precompiled and included in `src\lib`.

---

## 🛠️ Build Instructions

### Windows

1. Install **Visual Studio 2019** with the following components:

   * Desktop Development with C++
   * C++ Clang Compiler for Windows
   * C++ Clang-cl for v142 Build Tools

2. Open the solution in Visual Studio.

3. Build the solution. The compiled zip package will appear in the `dist` folder.

---

### Linux

```sh
autoreconf -vis
./configure
make && sudo make install
```

---

## 🚀 Usage Guide

### Windows Setup

1. Ensure `libusb0.dll` and `nfc.dll` are in the same directory as the executable (or in your system PATH).

2. Install **libusbK v3.0.7.0** using [Zadig](https://zadig.akeo.ie/):

   * Go to **Options > List All Devices**
   * Select your NFC reader
   * Choose **libusbK (v3.0.7.0)** as the driver
   * Click **Replace Driver**

3. In **Device Manager**, disable the **power-saving option**:

   * Go to your reader under **libusbK USB Devices**
   * Right-click → Properties → Power Management
   * Uncheck "Allow the computer to turn off this device to save power"

---

### Reading a Card

1. Place the MIFARE Classic card on the reader.
2. Run:

```sh
mfoc-hardnested -h
```

To perform a full dump:

```sh
mfoc-hardnested -O mycard.mfd -k keys.txt -P 500 -T 5
```

---

### Writing to a New Card

#### ✅ If the card sizes are the same:

```sh
nfc-mfclassic W a mycard.mfd
```

#### ⚠️ If writing to a larger card (e.g., 320B → 1K):

You **must pad** the dump to match the size of the target card. Follow these steps:

1. Open the provided `padding.py` script.
2. Replace the block list with your copied data from the terminal output.
3. Run the script to generate a padded `.mfd` file:

```sh
python padding.py
```

This creates `mycard_1k.mfd`.

4. Write it to the new blank card:

```sh
nfc-mfclassic W a mycard_1k.mfd
```

---

## 🙏 Credits

This project is based on work by many contributors. Please see the `AUTHORS` file for full attribution.

Special thanks to:

* **vk496** for integrating `mylazycracker` into MFOC
* **Nethemba**, **Carlo Meijer**, and **Roel Verdult** for their foundational work
