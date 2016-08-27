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

import sys
import os
from os import *
import os.path
from os.path import *
import argparse
import subprocess
from subprocess import call, check_output

import notify2
from notify2 import *

import gtk

from dbus.mainloop.glib import DBusGMainLoop


class MountDevice:

    def __init__(self, device, label):
        self.device = device
        self.label = label
        notify2.init("Notification-Mount", DBusGMainLoop())
        n = Notification("Device Detected", device + ": " + label + "\nDo you want to mount it?", "drive-removable-media-usb-pendrive")
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.add_action("action_mount", "Mount", self.mount)
        n.add_action("action_dismiss", "Dismiss", self.close)
        n.show()
        n.connect("closed", gtk.main_quit)
        gtk.main()

    def mount(self, notifyObj, action):
        call(["udevil", "mount", self.device])
        self.close(notifyObj, action)

    def close(self, notifyObj, action):
        notifyObj.close()
        gtk.main_quit()


def getLabel(label, device):
    if label.strip() != "":
        return label

    dirs = ["/dev/disk/by-label", "/dev/disk/by-uuid", "/dev/disk/by-id"]

    for directory in dirs:
        label = findSymlinkInDir(device, directory)
        if label != "" and label != None:
            break

    return label

def findSymlinkInDir(needle, directory):
    for f in listdir(directory):
        path = join(directory, f)
        if islink(path) and realpath(path) == needle:
            return f

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", "-d", help="Device name (e.g. /dev/sda1)", required=True, dest="device")
    parser.add_argument("--label", "-l", help="Label to use for the device. Defaults to volume label and if not set to UUID.", required=False, dest="label", default="")

    args = parser.parse_args()


    args.label = getLabel(args.label, args.device)

    obj = MountDevice(args.device, args.label)
