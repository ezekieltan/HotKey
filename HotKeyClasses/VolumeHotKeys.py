from hotkeys import HotKeys
import keyPresser


class VolumeHotKeys(HotKeys):

    def __init__(self):
        super().__init__()
        self.setMacros({
            'up': {'keys': ['f4']},
            'down': {'keys': ['f3']}
        })
        print(self.getMacros())

    def execute(self, macroName):
        if(not self.linuxCheck(macroName)):
            return
        for depressedKey in self.macros[macroName]['keys']:
            keyPresser.release(depressedKey)
            pass
        if macroName == 'up':
            keyPresser.pressAndReleaseWithModifiers('volup', [])
        elif macroName == 'down':
            keyPresser.pressAndReleaseWithModifiers('voldown', [])
