import ctypes
import vk

user32 = ctypes.WinDLL('user32', use_last_error=True)

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


def release(key):
    user32.keybd_event(vk.charToVk[key.upper()], 2, 2, 0)


def press(key):
    user32.keybd_event(vk.charToVk[key.upper()], 0, 0, 0)


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
