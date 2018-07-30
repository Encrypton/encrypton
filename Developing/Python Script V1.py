######IMPORT######

#from gpiozero import Button
import subprocess, os, string, time, dbus, gobject,sys
from dbus.mainloop.glib import DBusGMainLoop

######VARS######

#encrypt = Button(2)


#######SETUP######
def waitforusb():
  DBusGMainLoop(set_as_default=True)
  bus = dbus.SystemBus()
  proxy = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
  iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
  devices = iface.get_dbus_method('EnumerateDevices')()
  iface.connect_to_signal('DeviceAdded', device_added_callback)
  global mainloop
  mainloop = gobject.MainLoop()
  mainloop.run()

def device_added_callback(device):
  usbdev = "".join(device.split("/")[5:6])
  if usbdev.endswith("1") == 1:
    mainloop.quit()

print("Please insert the device you wish to encrypt")

waitforusb()




######EXECUTING SHELL######

#encrypt.wait_for_press()
print("ENCRYPT! ENCRYPT! ENCRYPT!")
#subprocess.getoutput(#SHELL#)

#shell.stdin.write("YES")
