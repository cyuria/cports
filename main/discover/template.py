pkgname = "discover"
pkgver = "6.2.2"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# fails in chroot env, needs some testdata
make_check_args = ["-E", "flatpaktest|CategoriesTest"]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "appstream-qt-devel",
    "attica-devel",
    "flatpak-devel",
    "fwupd-devel",
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidletime-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kuserfeedback-devel",
    "kxmlgui-devel",
    "purpose-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    "kirigami-addons",
    "purpose",
]
checkdepends = [
    "dbus",
    "xwayland-run",
    *depends,
]
pkgdesc = "KDE application manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "(GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://userbase.kde.org/Discover"
source = f"$(KDE_SITE)/plasma/{pkgver}/discover-{pkgver}.tar.xz"
sha256 = "d4fefafaa9b5b98005222a298cfcb7e3e1c89820d0ef8c02540e1a82108d5aae"


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebview-devel"]
