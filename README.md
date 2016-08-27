![GPL v3.0](https://img.shields.io/github/license/patrick96/notification-mount.svg)

This script displays a notification for an unmounted drive with a button to mount it.

It might be wise to call the script from a listeners that fires every time a new block device is detected.

As an example, if you have [udevil](https://ignorantguru.github.io/udevil/) installed, you can run the following script (as a service maybe?) and it will show a notification whenever a new device is detected:

```
devmon --no-mount --no-unmount --exec-on-drive "./notification-mount.py -d %f"
```
Note: You will need to change the path to the script, if you do not run `devmon` in the same folder as the script.
