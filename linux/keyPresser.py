import nixcommon
import vk


modifiers = {
    'WIN': ['WINDOWS', 'WIN', 'CMD', 'COMMAND'],
    'RWIN': ['RWINDOWS', 'RWIN', 'RCMD', 'RCOMMAND'],
    'ALT': ['ALTERNATE', 'ALT', 'OPTION'],
    'RALT': ['RALTERNATE', 'RALT', 'ROPTION'],
    'CTRL': ['CONTROL', 'CTRL'],
    'RCTRL': ['RCONTROL', 'RCTRL'],
    'SHIFT': ['SHIFT'],
    'RSHIFT': ['RSHIFT'],
}
modifierTranslator = {}
for k, v in modifiers.items():
    for x in v:
        modifierTranslator[x] = k


def write_event(scan_code, is_down):
    nixcommon.build_device()
    nixcommon.device.write_event(nixcommon.EV_KEY, scan_code, int(is_down))

def press(key):
    write_event(vk.charToVk[key.upper()], True)

def release(key):
    write_event(vk.charToVk[key.upper()], False)
def pressAndReleaseWithModifiers(key, modifiers):
    pressAndReleaseMultipleWithModifiers([key], modifiers)


def pressAndReleaseMultipleWithModifiers(keys, modifiers):
    for modifier in modifiers:
        press(modifierTranslator[modifier.upper()])
    for key in keys:
        press(key)
    for key in keys:
        release(key)
    for modifier in modifiers:
        release(modifierTranslator[modifier.upper()])
