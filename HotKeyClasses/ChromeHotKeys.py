from hotkeys import HotKeys
import subprocess


class ChromeHotKeys(HotKeys):
    def __init__(self):
        super().__init__()
        self.setMacros({
            'Default': {'keys': ['alt', 'c']},
            'Profile 1': {'keys': ['alt', 'v']}
        })
        print(self.getMacros())

    def execute(self, macroName):
        if macroName in self.getMacros().keys():
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "--profile-directory="+macroName])
