ALDOS Firstboot.
===============

The firstboot utility runs after ALDOS installation. It guides the user
through a series of steps that allows easier configuration of a newly
installed machine.

NOTICE: this program is specific to ALDOS Linux distribution. Don't expect it
to work in other Linux distros (without modifications), unless your distro
uses SysVinit or any SysVinit-compatible init system (e.g. upstart) and it
has installed the required components. The SysVinit stuff consists of
sysvinit/fistboot init script and a hard-coded command at progs/firstboot
file.

This project is based on the now deprecated 'firstboot' v18.6 by Martin Gracik
from Red Hat. I just removed the SystemD stuff, back-ported the sysvinit
stuff, re-branded .po and some .py files, and customize interface for
ALDOS(1).

(1) ALDOS is a custom distribution I mantain. Based on non-SystemD Fedora.

You are welcome to contribute to this project or use it in your own project.

Features.
========

- Shows welcome splash. See modules/welcome.py file.
- Shows the EULA (currently GNU/GPLv2). See modules/eula.py file.
- (Re)Configure keyboard in case you missed it during installation.
  See firstboot/frontend.py file.
- Create new user and (re)setup authconfig. See modules/create_user.py file.
- Set date and local time and (optionally) setup sync with ntp servers.
  See modules/date.py.

Options.
=======

- -m, --moduledir        use an alternative module directory.
- -r, --reconfig         Run wizard again to re-configure system.
- -s, --autoscreenshot   Take automatic screenshots and save them into
                         /root/firstboot-screenshots.
- -t, --test             Run in test mode.
- --themedir             Use an alternative theme directory.

Requirements.
=============

To build:

- gettext
- make
- python2-devel
- python2-setuptools

Run-time:

- authconfig-gtk
- cracklib-python
- initscripts (specifically /etc/init.d/functions)
- libuser-python
- pygtk2
- python2 >= 2.6
- python-ethtool
- python-meh
- setuptool
- system-config-date
- system-config-keyboard
- system-config-users

TODO (need help with this!).
===========================

- Try to migrate to pygobject.

