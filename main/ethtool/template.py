pkgname = "ethtool"
pkgver = "5.15"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libmnl-devel", "linux-headers"]
pkgdesc = "Utility for controlling network drivers and hardware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org/pub/software/network/ethtool"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "686fd6110389d49c2a120f00c3cd5dfe43debada8e021e4270d74bbe452a116d"
