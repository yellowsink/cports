pkgname = "font-cozette-otb"
pkgver = "1.29.0"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "Bitmap programming font optimized for coziness"
subdesc = "OTB"
license = "MIT"
url = "https://github.com/the-moonwitch/Cozette"
source = [
    # we need to call these .txt to get cbuild to just copy them verbatim
    f"https://github.com/the-moonwitch/Cozette/releases/download/v.{pkgver}/cozette.otb>cozette.txt",
    f"https://github.com/the-moonwitch/Cozette/releases/download/v.{pkgver}/LICENSE>LICENSE.txt"
]
sha256 = [
    "7a2c99914e712513eded3a0e9f48dfe22288d5b47c557543504af1862fe92779",
    "cef7a837b15237cf9bbc74d691e1c8c479f4292413ca2319c8e3b145d6fc980b"
]


def install(self):

    self.do("mv", "cozette.txt", "cozette.otb")
    self.do("mv", "LICENSE.txt", "LICENSE")

    self.install_file(f"cozette.otb", "usr/share/fonts/misc", name="cozette.otb")

    self.install_license("LICENSE")
