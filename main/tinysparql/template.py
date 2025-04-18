pkgname = "tinysparql"
pkgver = "3.9.1"
pkgrel = 2
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddocs=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    "-Dstemmer=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "asciidoc",
    "libxslt-progs",
    "dbus",
    "gobject-introspection",
    "python-gobject",
]
makedepends = [
    "glib-devel",
    "dbus-devel",
    "icu-devel",
    "json-glib-devel",
    "libxml2-devel",
    "sqlite-devel",
    "libsoup-devel",
    "bash-completion",
]
depends = ["shared-mime-info"]
checkdepends = ["mandoc"]
provides = [self.with_pkgver("tracker")]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tinysparql"
source = f"$(GNOME_SITE)/tinysparql/{pkgver[:-2]}/tinysparql-{pkgver}.tar.xz"
sha256 = "98e8933b946d8c54a77eadabd7f1d14cddd88fa43eef0d0ace3c0fcce646722b"
# check may be disabled
options = ["!cross"]


if self.profile().arch == "ppc64le":
    # https://gitlab.gnome.org/GNOME/tinysparql/-/issues/474
    options += ["!check"]


@subpackage("tinysparql-devel")
def _(self):
    self.provides = [self.with_pkgver("tracker-devel")]
    return self.default_devel()


@subpackage("tinysparql-libs")
def _(self):
    self.provides = [self.with_pkgver("tracker-libs")]
    return self.default_libs()
