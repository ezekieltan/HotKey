from hotkeys import HotKeys
import pyperclip
import time
import keyPresser


class MultiClipboardHotKeys(HotKeys):
    # Windows and Mac only
    def __init__(self):
        super().__init__(False)
        middleMacros = {'middle' + str(x): {'sequences': [
            [{'key': 'ctrl', 'down': True}, {'key': str(x), 'down': True}, {'key': 'ctrl', 'down': False},
             {'key': str(x), 'down': False}],
            [{'key': 'CONTROL', 'down': True}, {'key': str(x), 'down': True}, {'key': str(x), 'down': False},
             {'key': 'ctrl', 'down': False}]
        ]} for x in range(0, 10)}
        outMacros = {'out' + str(x): {'keys': ['ctrl', 'shift', str(x)], 'hold': ['ctrl', 'shift']} for x in
                     range(0, 10)}
        inMacros = {'in' + str(x): {'keys': [self.CtrlOrCmd, 'ralt', str(x)]} for x in range(0, 10)}
        blockers = {'blocker' + str(x): {'keys': ['ctrl', str(x)]} for x in range(0, 10)}
        self.setMacros(inMacros)
        self.setMacros(outMacros)
        self.setMacros(middleMacros)
        self.setMacros(blockers)

    def execute(self, macroName):
        if macroName.startswith('blocker'):
            pass
        elif macroName.startswith('middle'):
            keyPresser.pressAndReleaseWithModifiers('c', [self.CtrlOrCmd])
            keyPresser.pressAndReleaseWithModifiers(macroName[6:], [self.CtrlOrCmd, 'ralt'])

        elif macroName.startswith('in'):
            for depressedKey in self.macros[macroName]['keys']:
                keyPresser.release(depressedKey)
                pass
            print('in')
            time.sleep(0.05)
            clipboard = pyperclip.waitForPaste()
            print(clipboard)
            self.store(macroName[2:], clipboard)
        elif macroName.startswith('out'):
            for depressedKey in self.macros[macroName]['keys']:
                keyPresser.release(depressedKey)
                pass
            # keyPresser.release('1')
            toPaste = self.retrieve(macroName[3:])
            pyperclip.copy(toPaste)
            keyPresser.pressAndReleaseWithModifiers('V', [self.CtrlOrCmd])
            self.hold(macroName)  # to allow holding and repeating

    def store(self, id, value):
        if not hasattr(self, "storage"):
            self.storage = {}
        self.storage[id] = value

    def retrieve(self, id):
        if not hasattr(self, "storage"):
            self.storage = {}
        return self.storage[id]

    def hold(self, macroName):
        print(self.macros[macroName])
        if ('hold' in self.macros[macroName]):
            for holdKey in self.macros[macroName]['hold']:
                keyPresser.press(holdKey)  # to allow repeating
