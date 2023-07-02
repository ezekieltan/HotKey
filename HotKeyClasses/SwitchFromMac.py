from hotkeys import HotKeys
import keyPresser


class SwitchFromMac(HotKeys):

    def __init__(self):
        super().__init__()
        self.setMacros({
            'spotlight': {'keys': ['rctrl', 'space']},
            'altToCtrlDown': {'sequences': [[{'key': 'alt', 'down': True}]]},
            'altToCtrlUp': {'sequences': [[{'key': 'alt', 'down': False}]]},
            'altTab': {'keys': ['rctrl', 'tab']},
            'altF4': {'keys': ['rctrl', 'f4']},
        })
        print(self.getMacros())

    def execute(self, macroName):
        if macroName == 'spotlight':
            for key in self.getMacros()['spotlight']['keys']:
                keyPresser.release(key)
            keyPresser.pressAndReleaseWithModifiers('win', [])
        elif macroName == 'altTab':
            for key in self.getMacros()['altTab']['keys']:
                keyPresser.release(key)
            keyPresser.press('ralt')
            keyPresser.pressAndReleaseWithModifiers('tab', [])
        elif macroName == 'altF4':
            for key in self.getMacros()['altF4']['keys']:
                keyPresser.release(key)
            keyPresser.press('ralt')
            keyPresser.pressAndReleaseWithModifiers('f4', [])
        elif macroName == 'altToCtrlDown':
            keyPresser.release('alt')
            keyPresser.release('ralt')
            keyPresser.press('rctrl')
        elif macroName == 'altToCtrlUp':
            keyPresser.release('alt')
            keyPresser.release('ralt')
            keyPresser.release('rctrl')
