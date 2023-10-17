from hotkeys import HotKeys
import subprocess
import re


class UnderclockingHotKeys(HotKeys):
    def __init__(self):
        super().__init__()
        self.setMacros({
            'b'+str(x*10): {'keys': ['ctrl', 'win', str(x)]} for x in range(1, 10)
        })
        self.setMacros({
            'p'+str(x*10): {'keys': ['alt', 'win', str(x)]} for x in range(1, 10)
        })
        self.setMacros({
            'b'+str(100): {'keys': ['ctrl', 'win', '0']}
        })
        self.setMacros({
            'p'+str(100): {'keys': ['alt', 'win', '0']}
        })

        s = subprocess.check_output(['powercfg','/q']).decode('utf-8')
        uuidRegex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.powerSchemeGUID = re.findall(uuidRegex, re.findall('Power Scheme GUID: '+uuidRegex, s)[0])[0]
        self.subGroupGUID = re.findall(uuidRegex, re.findall('Subgroup GUID: '+uuidRegex+'  \(Processor power management\)', s)[0])[0]
        self.powerSettingGUID = re.findall(uuidRegex, re.findall('Power Setting GUID: '+uuidRegex+'  \(Maximum processor state\)', s)[0])[0]
        self.cmdDCList = ['powercfg', '/SETDCVALUEINDEX', self.powerSchemeGUID, self.subGroupGUID, self.powerSettingGUID]
        self.cmdACList = ['powercfg', '/SETACVALUEINDEX', self.powerSchemeGUID, self.subGroupGUID, self.powerSettingGUID]
        print(self.getMacros())

    def execute(self, macroName):
        if(macroName.startswith('b')):
            subprocess.Popen(self.cmdDCList + [macroName[1:]])
        if(macroName.startswith('p')):
            subprocess.Popen(self.cmdACList + [macroName[1:]])
        subprocess.Popen(['powercfg', '/s', self.powerSchemeGUID])