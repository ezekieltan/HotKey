from hotkeys import HotKeys
import pyperclip
import keyPresser
import pyotp


class KBOTPHotKeys(HotKeys):

    def __init__(self):
        super().__init__()
        self.setMacros({
            'copyToClipboard': {'keys': ['ctrl', 'f1']},
            'inject': {'keys': ['ctrl', 'f2'], 'hold': ['ctrl']}
        })
        print(self.getMacros())

    def execute(self, macroName):
        for depressedKey in self.macros[macroName]['keys']:
            keyPresser.release(depressedKey)
            pass
        secret = "JBSWY3DPEHPK3PXP"
        totp = pyotp.TOTP(secret)
        otp = totp.now()
        if macroName == 'copyToClipboard':
            pyperclip.copy(str(otp))
        elif macroName == 'inject':
            pyperclip.copy(str(otp))
            keyPresser.pressAndReleaseWithModifiers('V', [self.CtrlOrCmd])
            self.hold(macroName)  # to allow holding and repeating

    def hold(self, macroName):
        print(self.macros[macroName])
        if ('hold' in self.macros[macroName]):
            for holdKey in self.macros[macroName]['hold']:
                keyPresser.press(holdKey)  # to allow repeating
