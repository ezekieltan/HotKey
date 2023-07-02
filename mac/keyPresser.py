import Quartz
from functools import reduce
import vk


def getModifierMask(modifier):
    modifier = modifier.upper()
    if modifier == 'SHIFT':
        return Quartz.kCGEventFlagMaskShift
    elif modifier == 'CTRL' or modifier == 'CONTROL':
        return Quartz.kCGEventFlagMaskControl
    elif modifier == 'OPTION' or modifier == 'ALT' or modifier == 'ALTERNATE':
        return Quartz.kCGEventFlagMaskAlternate
    elif modifier == 'COMMAND' or modifier == 'CMD' or modifier == 'WINDOWS' or modifier == 'WIN':
        return Quartz.kCGEventFlagMaskCommand
    elif modifier == 'FN' or modifier == 'FUNCTION':
        return Quartz.kCGEventFlagMaskSecondaryFn


def press(key):
    key_down = Quartz.CGEventCreateKeyboardEvent(None, vk.charToVk[key.upper()], True)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, key_down)


def release(key):
    key_up = Quartz.CGEventCreateKeyboardEvent(None, vk.charToVk[key.upper()], False)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, key_up)


def pressAndReleaseWithModifiers(key, modifiers=[]):
    pressAndReleaseMultipleWithModifiers([key], modifiers)


def pressAndReleaseMultipleWithModifiers(keys, modifiers=[]):
    flags = [getModifierMask(modifier) for modifier in modifiers]
    flagsOred = reduce(lambda x, y: x | y, flags) if len(flags) > 0 else 0
    for key in keys:
        v_down_event = Quartz.CGEventCreateKeyboardEvent(None, vk.charToVk[key.upper()], True)
        Quartz.CGEventSetFlags(v_down_event, flagsOred)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, v_down_event)
    for key in keys:
        v_up_event = Quartz.CGEventCreateKeyboardEvent(None, vk.charToVk[key.upper()], False)
        Quartz.CGEventSetFlags(v_up_event, flagsOred)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, v_up_event)
