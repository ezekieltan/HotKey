import tkinter as tk

from HotKeyClasses.MultiClipboardHotKeys import MultiClipboardHotKeys
from HotKeyClasses.SwitchFromMac import SwitchFromMac
from HotKeyClasses.VolumeHotKeys import VolumeHotKeys
from HotKeyClasses.MediaHotKeys import MediaHotKeys
from KBHandler import KBHandler


def afterFunc():
    print('starting loop')
    kbHandler.run_event_loop()


hks = [MultiClipboardHotKeys(), SwitchFromMac(), VolumeHotKeys(), MediaHotKeys()]
kbHandler = KBHandler()
kbHandler.addHks(hks)


def start_application():
    root = tk.Tk()
    root.geometry("300x0")
    root.resizable(False, False)
    root.title('HotKeyRunner')
    root.after(10, afterFunc)
    return root


if __name__ == '__main__':
    start_application().mainloop()  # pragma: no cover
