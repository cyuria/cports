pkgname = "jj"
pkgver = "0.28.2"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "libssh2-devel",
    "openssl3-devel",
    "rust-std",
]
checkdepends = ["git", "openssh"]
pkgdesc = "Git-compatible VCS frontend"
license = "Apache-2.0"
url = "https://martinvonz.github.io/jj"
source = f"https://github.com/martinvonz/jj/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dae80d2629a9f430a9ea795c8cd378ced6ce1c870ab9ffe3b61f64cdd636a2bc"
# generates completions with host binary
options = ["!cross"]

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"


def post_prepare(self):
    from cbuild.util import cargo, patch

    # done separately because we need to patch lockfile before vendoring :/
    patch.patch_git(self, [self.files_path / "bser.patch"])

    cargo.clear_vendor_checksums(self, "serde_bser")


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(f"{self.cwd}/jj.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/jj",
                "util",
                "completion",
                shell,
                stdout=o,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jj")
    self.do(
        f"target/{self.profile().triplet}/release/jj",
        "util",
        "install-man-pages",
        f"{self.chroot_destdir}/usr/share/man",
    )
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"jj.{shell}", shell)
