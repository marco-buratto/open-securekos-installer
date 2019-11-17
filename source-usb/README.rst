Resilient Linux USB Installer
=============================

**Resilient Linux USB Installer** is the deployment system for writing Resilient Linux ISO image onto a USB key instead on installing onto the hard drive.


Building (Debian Buster)
^^^^^^^^^^^^^^^^^^^^^^^^

The Resilient Linux USB Installer codebase comes with a quick-and-dirty Debian Buster package builder - only the binary .deb package is built. 

In order to build the Debian package, open the terminal emulator as root::

    cd /path/to/resilientlinux-usb-installer/source
    ./debian-pkg/make-release.sh

The *resilientlinux-usb-installer_version-release_all.deb* file will be created. 
