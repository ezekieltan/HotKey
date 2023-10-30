import platform
import time

class HotKeys:
    def __init__(self, ignoreFn=True):
        self.macros = {}
        self.operatingSystem = ''
        self.operatingSystem = 'mac' if platform.system() == "Darwin" else (
            'windows' if platform.system() == "Windows" else ('linux' if platform.system() == "Linux" else ''))
        self.CtrlOrCmd = 'cmd' if self.operatingSystem == 'mac' else 'ctrl'
        self.ignoreFn = ignoreFn
        self.cmdOrWindows = 'CMD' if self.operatingSystem == 'mac' else 'WIN'
        self.optionOrAlt = 'OPTION' if self.operatingSystem == 'mac' else 'ALT'
        self.modifiers = {
            self.cmdOrWindows: ['WINDOWS', 'WIN', 'CMD', 'COMMAND'],
            self.optionOrAlt: ['ALTERNATE', 'ALT', 'OPTION'],
            'CTRL': ['CONTROL', 'CTRL'],
            'SHIFT': ['SHIFT'],
        }
        self.lastExecuted = {}
        self.linuxTimeout = 0.05
    def linuxCheck(self, macroName):
        if(self.operatingSystem != 'linux'):
            return True
        if macroName not in self.lastExecuted:
            self.lastExecuted[macroName] = time.time()
            return True
        if(time.time() - self.linuxTimeout <= self.lastExecuted[macroName]):
            print(macroName, 'blocked')
            return False
        self.lastExecuted[macroName] = time.time()
        return True

    def getMacros(self):
        return self.macros

    def setMacros(self, newMacros):
        invalidKeys = []
        for macroName, macro in newMacros.items():

            if 'keys' in macro:
                macro['keys'] = [key.upper() for key in macro['keys']]
                for modifierName, modifierValues in self.modifiers.items():
                    macro['keys'] = [modifierName if key in modifierValues else key for key in macro['keys']]
            elif ('sequences' in macro):
                newSequences = []
                oldSequences = macro['sequences']
                for oldSequence in oldSequences:
                    for oldItem in oldSequence:
                        for modifierName, modifierValues in self.modifiers.items():
                            keyUppered = oldItem['key'].upper()
                            oldItem['key'] = modifierName if keyUppered in modifierValues else keyUppered
                    newSequences.append(oldSequence)
            else:
                print('macro not set')
                invalidKeys.append(macroName)

        for invalidKey in invalidKeys:
            newMacros.pop(invalidKey)

        self.macros.update(newMacros)

    def execute(self, macroName):
        raise NotImplementedError('subclasses must override execute()!')
