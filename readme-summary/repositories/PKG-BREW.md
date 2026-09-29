# PKG-BREW

Summary:

PKG-BREW is an experimental source-based package manager designed specifically for Linux from Scratch (LFS) based systems. It resides in the directory `/usr/bin` and operates by allowing users to input a desired package name, such as `bpkg-brew xorg`. This triggers the download of the specified package's source code (e.g., Xorg) from a user-defined mirror via `wget`, storing it in `/usr/bpkg/source/$PACKAGE_NAME`. A separate build directory (`/usr/bpkg/source/$PACKAGE_NAME/BUILD`) is created for compiling and installing the package using standard GNU autotools commands: `./configure`, `make`, and `make install`. The final installation destination is set to `/usr/--DESTDIR`.

KEYWORDS:
PKG-BREW, Linux from Scratch, LFS, source-based package manager, wget, Xorg, build directory, DESTDIR
