![GPL v3.0](https://img.shields.io/github/license/patrick96/notification-mount.svg)

This script displays a notification for an unmounted drive with a button to mount it.

It might be wise to call the script from a listeners that fires every time a new block device is detected.

As an example, if you have [udevil][udevil] installed, you can run the following script (as a service maybe?) and it will show a notification whenever a new device is detected:

```bash
devmon --no-mount --no-unmount --exec-on-drive "./notification-mount -d %f"
```
Note: You will need to change the path to the script, if you do not run `devmon` in the same folder as the script.

## Installation
If you are not using **Arch** then you will need to copy or symlink the `notification-mount` file to somewhere that is in your `$PATH` (see below in the example for more info on the `PATH`).

For how to install and start the system service see the [example](#systemd-unit) below.
### Arch Linux
If you are using **Arch Linux** either install [notification-mount][notification-mount] or [notification-mount-git][notification-mount-git] from the AUR.
You should now also have a user systemd service which you can enable and start like this:
```
systemctl --user enable notification-mount.service
systemctl --user start notification-mount.service
```
This service is the same as the one in the example below. 
### Requirements
* Linux
* python3
* [python-gobject](https://wiki.gnome.org/Projects/PyGObject)
* [python-notify2](https://pypi.python.org/pypi/notify2)
* [udevil][udevil]

## Examples
### Systemd Unit
Systemd service using [udevil][udevil]:
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
Fot this you will need to have the `notification-mount` in a folder that is part of the `$PATH`

**Note:** This should be the default `$PATH`. Alternatively you can set your modified `PATH` on the systemd environment like described [here](https://wiki.archlinux.org/index.php/Systemd/User#PATH). 

After that just enable and start the service:
```
systemctl --user enable notification-mount.service
systemctl --user start notification-mount.service
```

[udevil]: https://ignorantguru.github.io/udevil/
[notification-mount]: https://aur.archlinux.org/packages/notification-mount
[notification-mount-git]: https://aur.archlinux.org/packages/notification-mount-git
