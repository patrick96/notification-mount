notification-mount
==================

![GPL v3.0](https://img.shields.io/github/license/patrick96/notification-mount.svg)

This is a script that displays a notification for a drive with a button to mount it.

It might be wise to call the script from a listeners that fires every time a new block device is detected (see [examples](#examples)).

Table of Contents
=================

  * [notification-mount](#notification-mount)
  * [Table of Contents](#table-of-contents)
  * [Installation](#installation)
    * [Requirements](#requirements)
    * [General](#general)
    * [Arch Linux](#arch-linux)
  * [Examples](#examples)
    * [Devmon Script](#devmon-script)
    * [Systemd Unit](#systemd-unit)

Installation
============

## Requirements
* Linux
* python3
* [python-gobject](https://wiki.gnome.org/Projects/PyGObject)
* [python-notify2](https://pypi.python.org/pypi/notify2)
* [udevil][udevil]

## General

There is a pip package [here](https://pypi.python.org/pypi/notification-mount) that you can install like this:
```bash
sudo pip install notification-mount
```
This will only install the `notification-mount` script but not the system service. For how to install and start the system service, see the [example](#systemd-unit) below.

If you are using **Arch Linux**, I would highly recommend using the method described [below]("#arch-linux") since it already installs the systemd service.

## Arch Linux
If you are using **Arch Linux** either install [notification-mount][notification-mount] or [notification-mount-git][notification-mount-git] from the AUR.
You should now also have a user systemd service which you can enable and start like this:
```bash
systemctl --user enable notification-mount.service
systemctl --user start notification-mount.service
```
This service is the same as the one in the example below. 

Examples
========

## Devmon Script
If you have [udevil][udevil] installed, you can run the following script and it will show a notification whenever a new device is detected:

```bash
devmon --no-mount --no-unmount --exec-on-drive "./notification-mount -d %f" &
```
You could at this to your `.xinitrc` or any other script that runs whenever your system starts up.

You may need to change the path to the script depending on where you run this piece of code from.
## Systemd Unit
Systemd service using the previous example and [udevil][udevil]:
```ini
notification-mount.service
--------------------------
[Unit]
Description=Notification when new block device is detected with button to mount

[Service]
Type=simple
ExecStart=/usr/bin/devmon --no-mount --no-unmount --exec-on-drive "notification-mount -d %%f"

[Install]
WantedBy=default.target
```
Fot this you will need to have the `notification-mount` in a folder that is part of the `PATH`

**Note:** This should be the default `PATH`. Alternatively you can set your modified `PATH` on the systemd environment like described [here](https://wiki.archlinux.org/index.php/Systemd/User#PATH). 

After that just enable and start the service:
```bash
systemctl --user enable notification-mount.service
systemctl --user start notification-mount.service
```

[udevil]: https://ignorantguru.github.io/udevil/
[notification-mount]: https://aur.archlinux.org/packages/notification-mount
[notification-mount-git]: https://aur.archlinux.org/packages/notification-mount-git
