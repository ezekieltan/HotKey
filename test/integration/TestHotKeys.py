from hotkeys import HotKeys
import keyPresser


class TestHotKeys(HotKeys):

    def __init__(self):
        super().__init__()
        self.macroDict = {
            'test': {'keys': ['ctrl', 'alt', 'c']},
            'testChain': {'keys': ['win', 'shift', 'r']},
            'testChain2': {'sequences': [
                [{'key': 'alt', 'down': True}, {'key': 'y', 'down': True}, {'key': 'y', 'down': False},
                 {'key': 'alt', 'down': False}]]},
        }
        self.setMacros(self.macroDict)
        print(self.getMacros())

    def execute(self, macroName):
        if macroName == 'test':
            for key in self.getMacros()['test']['keys']:
                keyPresser.release(key)
            keyPresser.pressAndReleaseWithModifiers('r', ['win', 'shift'])
        if macroName == 'testChain':
            for key in self.getMacros()['testChain']['keys']:
                keyPresser.release(key)
            keyPresser.press('alt')
            keyPresser.press('y')
            keyPresser.release('y')
            keyPresser.release('alt')
        if macroName == 'testChain2':
            keyPresser.press('ctrl')
            keyPresser.press('c')
            keyPresser.release('c')
            keyPresser.release('ctrl')
