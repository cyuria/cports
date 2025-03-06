pkgname = "base-cbuild-host"
pkgver = "0.1"
pkgrel = 3
build_style = "meta"
depends = [
    "apk-tools",
    "openssl3",
    "git",
    "bubblewrap",
    "chimerautils",
    "python",
]
pkgdesc = "Everything one needs to use cbuild and cports"
license = "custom:meta"
url = "https://chimera-linux.org"
