from hotkeys import HotKeys
import vk


class KeyboardCleanerHotKeys(HotKeys):

    def __init__(self):
        super().__init__()
        self.setMacros({x: {'sequences': [[{'key': x, 'down': True}]]} for x in list(vk.vkToChar.values())})

    def execute(self, macroName):
        pass
