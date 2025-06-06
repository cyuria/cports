pkgname = "libfreeaptx"
pkgver = "0.1.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Free implementation of aptX codec"
license = "LGPL-2.1-or-later"
url = "https://github.com/iamthehorker/libfreeaptx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7acf514446cae59585d9bc21e4f98f4a3856f4741c3a7a09d06e8ac5bf2f7315"
# no test suite
options = ["!check"]


@subpackage("libfreeaptx-devel")
def _(self):
    return self.default_devel()
