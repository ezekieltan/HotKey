import unittest
from hotkeys import HotKeys


class TestMacros(unittest.TestCase):

    def setUp(self):
        self.hotkeys = HotKeys()

    def testOptionAlt(self):
        macroDict = {
            'test': {'keys': ['ctrl', 'alt', 'c']},
            'test2': {'keys': ['ctrl', 'option', 'd']}
        }
        self.hotkeys.setMacros(macroDict)
        self.assertEqual({
            'test': {'keys': ['CTRL', self.hotkeys.optionOrAlt, 'C']},
            'test2': {'keys': ['CTRL', self.hotkeys.optionOrAlt, 'D']}
        }, self.hotkeys.getMacros())

    def testWinCmd(self):
        macroDict = {
            'test': {'keys': ['ctrl', 'win', 'c']},
            'test2': {'keys': ['ctrl', 'cmd', 'd']}
        }
        self.hotkeys.setMacros(macroDict)
        self.assertEqual({
            'test': {'keys': ['CTRL', self.hotkeys.cmdOrWindows, 'C']},
            'test2': {'keys': ['CTRL', self.hotkeys.cmdOrWindows, 'D']}
        }, self.hotkeys.getMacros())

    def testNothing(self):
        macroDict = {
            'test': {'abc': ['ctrl', 'win', 'c']},
            'test2': {'def': ['ctrl', 'cmd', 'd']}
        }
        self.hotkeys.setMacros(macroDict)
        self.assertEqual({}, self.hotkeys.getMacros())

    def testSetMacros(self):
        macroDict = {
            'testChain2': {'sequences': [[{'key': 'y', 'down': True}, {'key': 'Y', 'down': False}]]},
        }
        self.hotkeys.setMacros(macroDict)
        self.assertEqual({
            'testChain2': {
                    'sequences': [
                        [
                            {'down': True, 'key': 'Y'},
                            {'down': False, 'key': 'Y'},
                        ]
                    ]
                }
        },
            self.hotkeys.getMacros())

    def testOverrideExecute(self):
        class TestHotKeyNoOverrideExecute(HotKeys):
            pass

        with self.assertRaises(NotImplementedError) as context:  # noqa: F841
            TestHotKeyNoOverrideExecute().execute('')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
