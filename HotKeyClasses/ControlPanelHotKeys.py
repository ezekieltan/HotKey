from hotkeys import HotKeys
import subprocess


class ControlPanelHotKeys(HotKeys):
    def __init__(self):
        super().__init__()
        self.setMacros({
            'powerOptions': {'keys': ['ctrl', 'win', 'e']},
            'programsAndFeatures': {'keys': ['ctrl', 'win', 'p']},
        })
        print(self.getMacros())

    def execute(self, macroName):
        if macroName == 'powerOptions':
            subprocess.Popen(['C:\\Windows\\system32\\control.exe', '/name', 'Microsoft.PowerOptions'])
        if macroName == 'programsAndFeatures':
            subprocess.Popen(['C:\\Windows\\System32\\control.exe', '/name', 'Microsoft.ProgramsAndFeatures'])
