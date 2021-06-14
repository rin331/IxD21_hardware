import os #used to all external commands
import sys # used to exit the script
import dbus
import evdev
import keymap
import time
from time import sleep

HID_DBUS = 'org.yaptb.btkbservice'
HID_SRVC = '/org/yaptb/btkbservice'
debugFilePath="./Debug/"
debugLine=''

class SendKeycode:
    """
    Send the HID messages to the keyboard D-Bus server for specified button
    """
    #setup 
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.btkobject = self.bus.get_object(HID_DBUS,
                                             HID_SRVC)
        self.btk_service = dbus.Interface(self.btkobject,
                                          HID_DBUS)

    """
    send key 
    """
    def popinSendKey(self, send_string):
        targetCode = int(keymap.keytable[ send_string ])
        targetKeys = [161, 1, 0, 0, targetCode, 0, 0, 0, 0, 0]
        all_keys_up = [161, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        
        self.btk_service.send_keys(targetKeys)
        time.sleep(0.001)
        self.btk_service.send_keys(all_keys_up)

    """
    debug send key (save send key by txtfile)
    """
    def DebugPopinSendKey(self.send_string):
        popinSendKey(self,send_string)

    def writeText(self,filePath,text):
        with open(filePath, mode='a') as f:
            f.write(text+"\n")



if __name__ == '__main__':
    
    #送るためのクラスを用意
    skc = SendKeycode()

    print ("Sending " + string_to_send)

    skc.popinSendKey(string_to_send)

    print ("Done " + string_to_send)