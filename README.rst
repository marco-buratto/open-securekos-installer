Resilient Linux Installer
=========================

**Resilient Linux Installer** is the deployment system for writing the Resilient Linux ISO image onto a hard drive - it will create the **liveng partitioning scheme**.

This program must be launched from the Resilient Linux live installer system.


Building (Debian Buster)
^^^^^^^^^^^^^^^^^^^^^^^^

The Resilient Linux Installer codebase comes with a quick-and-dirty Debian Buster (binary) package builder.

In order to build the Debian package, open the terminal emulator as root::

    cd /path/to/resilientlinux-installer/source
    ./debian-pkg/make-release.sh

The *resilientlinux-installer_version-release_all.deb* file will be created. 


Resilient Linux USB  Installer
==============================

In the *source-usb* folder, the Resilient Linux USB Installer is stored. 
**Resilient Linux USB Installer** is the deployment system for writing Resilient Linux ISO image onto a USB key instead on installing onto the hard drive.
