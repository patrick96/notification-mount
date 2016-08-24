#!/usr/bin/env python2

# Copyright 2016 Patrick Ziegler
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk
import pynotify
import os

class MountDevice:

    def __init__(self):
        pynotify.init("Notification-mount")
        n = pynotify.Notification("Device Detected", "Do you want to mount it?", "drive-removable-media-usb-pendrive")
        n.set_urgency(pynotify.URGENCY_NORMAL)
        n.add_action("action_mount", "Mount to /xyz", self.mount)
        n.add_action("action_dismiss", "Dismiss", self.close)
        n.show()
        n.connect("closed", gtk.main_quit)
        gtk.main()

    def mount(self, notifyObj, action):
        self.close(notifyObj, action)

    def close(self, notifyObj, action):
        notifyObj.close()
        gtk.main_quit()

if __name__ == "__main__":
    obj = MountDevice()
