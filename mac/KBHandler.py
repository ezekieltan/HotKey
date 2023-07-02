import Quartz
import macroIterator
from lib_RecentOperations import RecentOperations
import vk


class KBHandler:
    def __init__(self):
        self.down = {}
        self.hks = []
        self.recentOperations = RecentOperations()

    def addHks(self, inp=[]):
        self.hks.extend(inp)

    def event_callback(self, eventTapProxy, eventTypeId, event, userdata):
        public_vars = [var for var in dir(event) if not var.startswith("_")]  # noqa: F841
        keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        flags = Quartz.CGEventGetFlags(event)
        self.down['SHIFT'] = (flags & (Quartz.kCGEventFlagMaskShift | 2)) == (Quartz.kCGEventFlagMaskShift | 2) or (
                    flags & (Quartz.kCGEventFlagMaskShift | 2 ** 29)) == (Quartz.kCGEventFlagMaskShift | 2 ** 29)
        self.down['RSHIFT'] = (flags & (Quartz.kCGEventFlagMaskShift | 4)) == (Quartz.kCGEventFlagMaskShift | 4)
        self.down['CAPSLOCK'] = (flags & Quartz.kCGEventFlagMaskAlphaShift) != 0
        self.down['OPTION'] = (flags & (Quartz.kCGEventFlagMaskAlternate | 32)) == (
                Quartz.kCGEventFlagMaskAlternate | 32) or (
                                          flags & (Quartz.kCGEventFlagMaskAlternate | 2 ** 29)) == (
                                          Quartz.kCGEventFlagMaskAlternate | 2 ** 29)
        self.down['ROPTION'] = (flags & (Quartz.kCGEventFlagMaskAlternate | 64)) == (
                    Quartz.kCGEventFlagMaskAlternate | 64)
        self.down['CTRL'] = (flags & Quartz.kCGEventFlagMaskControl) != 0
        self.down['CMD'] = (flags & (Quartz.kCGEventFlagMaskCommand | 8)) == (Quartz.kCGEventFlagMaskCommand | 8) or (
                    flags & (Quartz.kCGEventFlagMaskCommand | 2 ** 29)) == (Quartz.kCGEventFlagMaskCommand | 2 ** 29)
        self.down['RCMD'] = (flags & (Quartz.kCGEventFlagMaskCommand | 16)) == (Quartz.kCGEventFlagMaskCommand | 16)
        self.down['FN'] = (flags & Quartz.kCGEventFlagMaskSecondaryFn) != 0
        self.down['HELP'] = (flags & Quartz.kCGEventFlagMaskHelp) != 0
        self.down['NUMPAD'] = (flags & Quartz.kCGEventFlagMaskNumericPad) != 0

        try:
            if (eventTypeId == 11):
                self.recentOperations.addOperation(vk.vkToChar[keycode], False)
                self.down[vk.vkToChar[keycode]] = False
            if (eventTypeId == 10):
                self.recentOperations.addOperation(vk.vkToChar[keycode], True)
                self.down[vk.vkToChar[keycode]] = True
            if (eventTypeId == 12):
                self.recentOperations.addOperation(vk.vkToChar[keycode], self.down[vk.vkToChar[keycode]])
            block = macroIterator.runMacros(self.hks, self.down, self.recentOperations)
            if block is False:
                return event
            else:
                return
        except Exception as e:
            print("listening error: " + str(e))
        return event

    def run_event_loop(self):
        # https://gist.github.com/cosven/75523f1e970edcc4da8cf1908a9c1463
        # https://www.programcreek.com/python/example/13741/objc.loadBundle
        print('try to load mac hotkey event loop')
        # Set up a tap, with type of tap, location, options and event mask
        event_mask = (1 << Quartz.kCGEventKeyDown) | (1 << Quartz.kCGEventKeyUp) | (1 << Quartz.kCGEventFlagsChanged)

        def create_tap():
            return Quartz.CGEventTapCreate(
                Quartz.kCGSessionEventTap,  # Session level is enough for our needs
                Quartz.kCGHeadInsertEventTap,  # Insert wherever, we do not filter
                Quartz.kCGEventTapOptionDefault,
                # NSSystemDefined for media keys
                event_mask,
                self.event_callback,
                None
            )

        tap = create_tap()
        if tap is None:
            print('Error occurred when trying to listen global hotkey. '
                  'trying to popup a prompt dialog to ask for permission.')
            # we do not use pyobjc-framework-ApplicationServices directly, since it
            # causes segfault when call AXIsProcessTrustedWithOptions function
            import objc
            AS = objc.loadBundle('CoreServices', globals(),
                                 '/System/Library/Frameworks/ApplicationServices.framework')
            objc.loadBundleFunctions(AS, globals(),
                                     [('AXIsProcessTrustedWithOptions', b'Z@')])
            objc.loadBundleVariables(AS, globals(),
                                     [('kAXTrustedCheckOptionPrompt', b'@')])
            trusted = AXIsProcessTrustedWithOptions({kAXTrustedCheckOptionPrompt: True})  # noqa
            if not trusted:
                print('Have popuped a prompt dialog to ask for accessibility.'
                      'You can restart feeluown after you grant access to it.')
            else:
                print('Have already grant accessibility, '
                      'but we still can not listen global hotkey,'
                      'theoretically, this should not happen.')
            return

        run_loop_source = Quartz.CFMachPortCreateRunLoopSource(
            None, tap, 0)
        Quartz.CFRunLoopAddSource(
            Quartz.CFRunLoopGetCurrent(),
            run_loop_source,
            Quartz.kCFRunLoopDefaultMode
        )
        # Enable the tap
        Quartz.CGEventTapEnable(tap, True)
        Quartz.CFRunLoopRun()
        print('mac hotkey event loop exit')
        return []
