from hotkeys import HotKeys
import keyPresser


class MediaHotKeys(HotKeys):
    # Only available on Windows
    def __init__(self):
        super().__init__()
        self.setMacros({
            'rewind': {'keys': ['f6']},
            'play': {'keys': ['f7']},
            'forward': {'keys': ['f8']}
        })
        print(self.getMacros())

    def execute(self, macroName):
        for depressedKey in self.macros[macroName]['keys']:
            keyPresser.release(depressedKey)
            pass

        if macroName == 'play':
            keyPresser.pressAndReleaseWithModifiers('play', [])
        elif macroName == 'rewind':
            keyPresser.pressAndReleaseWithModifiers('rewind', [])
        elif macroName == 'forward':
            keyPresser.pressAndReleaseWithModifiers('forward', [])
