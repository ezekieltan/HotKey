import macroIterator
import nixcommon
from lib_RecentOperations import RecentOperations
import vk

class KBHandler:
    def __init__(self):
        self.down = {}
        self.hks = []
        self.recentOperations = RecentOperations()

    def addHks(self, inp=[]):
        self.hks.extend(inp)

    # Define the callback function that will be called when an event occurs
    def new_event_linux(self, keyIsDown, code):
        key = vk.vkToChar[code]
        self.down[key] = keyIsDown
        self.recentOperations.addOperation(key, keyIsDown)
        self.logDown(self.down)
        return macroIterator.runMacros(self.hks, self.down, self.recentOperations)

    def logDown(self, down):
        print(down)  # pragma: no cover


    def run_event_loop(self):
        nixcommon.build_device()
        while True:
            time, type, scan_code, value, device_id = nixcommon.device.read_event()
            print(time, type, scan_code, value, device_id)
            if type != nixcommon.EV_KEY:
                continue

            event_type = 'down' if value else 'up'
            down = True if event_type=='down' else False

            block = self.new_event_linux(down, scan_code)