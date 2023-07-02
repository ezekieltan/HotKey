import unittest
import threading
import HotKeyRunner
from unittest.mock import patch
import time
import copy

from KBHandler import KBHandler
from test.integration.TestHotKeys import TestHotKeys


class TestIntegration(unittest.TestCase):

    def runApp(self):
        HotKeyRunner.kbHandler = KBHandler()
        HotKeyRunner.kbHandler.addHks([TestHotKeys()])
        app = HotKeyRunner.start_application()
        app.after(500, app.destroy)
        with patch.object(HotKeyRunner.KBHandler, 'logDown') as mockFn:
            mockFn.side_effect = lambda down: self.processDown(down)
            app.mainloop()

    def setUp(self):
        self.t = threading.Thread(target=self.runApp)
        self.t.start()

    def tearDown(self):
        self.t.join()

    def processDown(self, down):
        downCopy = copy.deepcopy(down)
        toAppend = [{k: v for k, v in downCopy.items() if v is True}]
        if toAppend != [{}]:
            self.downList.extend(toAppend)
        print(self.downList)

    def testAll(self):
        import keyboard
        self.downList = []
        keyboard.press('ctrl')
        keyboard.press('alt')
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release('alt')
        keyboard.release('ctrl')
        self.assertEqual([{'CTRL': True},
                          {'ALT': True, 'CTRL': True},
                          {'ALT': True, 'C': True, 'CTRL': True},
                          {'ALT': True, 'C': True},
                          {'C': True},
                          {'WIN': True},
                          {'SHIFT': True, 'WIN': True},
                          {'R': True, 'SHIFT': True, 'WIN': True},
                          {'R': True, 'SHIFT': True},
                          {'R': True},
                          {'ALT': True},
                          {'ALT': True, 'Y': True},
                          {'ALT': True},
                          {'CTRL': True},
                          {'C': True, 'CTRL': True},
                          {'CTRL': True}],
                         self.downList)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
