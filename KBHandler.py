import macroIterator
from lib_RecentOperations import RecentOperations
import vk
import ctypes
import atexit


# Define the CWPSTRUCT structure
class CWPSTRUCT(ctypes.Structure):
    _fields_ = [
        ("lParam", ctypes.c_long),
        ("wParam", ctypes.c_int),
        ("message", ctypes.c_uint),
        ("hwnd", ctypes.c_void_p)
    ]


class KBHandler:
    def __init__(self):
        self.down = {}
        self.hks = []
        self.recentOperations = RecentOperations()

    def addHks(self, inp=[]):
        self.hks.extend(inp)

    # Define the callback function that will be called when an event occurs
    def new_event_windows(self, message, lParam):
        keyIsDown = message // 128 == 0
        key = vk.vkToChar[lParam]
        self.down[key] = keyIsDown
        self.recentOperations.addOperation(key, keyIsDown)
        self.logDown(self.down)
        return macroIterator.runMacros(self.hks, self.down, self.recentOperations)

    def logDown(self, down):
        print(down)  # pragma: no cover

    def callback(self, nCode, wParam, lParam):
        cwstruct = ctypes.cast(lParam, ctypes.POINTER(CWPSTRUCT)).contents
        message = cwstruct.message
        hwnd = cwstruct.hwnd
        wParam = cwstruct.wParam
        lParam = cwstruct.lParam
        print(message, wParam, lParam, hwnd)
        block = self.new_event_windows(message, lParam)
        if block:
            return 1  # to block
        else:
            return ctypes.windll.user32.CallNextHookEx(None, nCode, wParam, lParam)

    def run_event_loop(self):
        # Define the hook function
        hook_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))(
            self.callback)

        # Set the hook
        hook_id = ctypes.windll.user32.SetWindowsHookExW(  # noqa: F841
            13,  # The type of hook to set (13 is the code for a keyboard hook)
            hook_func,  # The hook function to call
            None,  # The handle to the DLL that contains the hook function (not needed for a global hook)
            0  # The thread identifier (0 indicates that the hook function is associated with all existing threads)
        )

        atexit.register(ctypes.windll.user32.UnhookWindowsHookEx, hook_func)
