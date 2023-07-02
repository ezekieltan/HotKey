from AppKit import NSButton, NSApplication, NSRoundedBezelStyle, NSObject, NSMakeRect, NSWindow, NSTitledWindowMask, \
    NSClosableWindowMask, NSMiniaturizableWindowMask, NSBackingStoreBuffered, NSNormalWindowLevel
from KBHandler import KBHandler
from HotKeyClasses.MultiClipboardHotKeys import MultiClipboardHotKeys
from HotKeyClasses.KBOTPHotKeys import KBOTPHotKeys


class MyApp(NSObject):
    def init(self):
        self = super(MyApp, self).init()
        if self is None:
            return None
        return self

    def buildUI(self):
        # Create the main window
        frame = NSMakeRect(0, 0, 200, 100)
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame, NSTitledWindowMask | NSClosableWindowMask | NSMiniaturizableWindowMask, NSBackingStoreBuffered,
            False)
        self.window.setTitle_("HotKeyRunner")
        self.window.setLevel_(NSNormalWindowLevel)

        # Show the window
        self.window.makeKeyAndOrderFront_(None)

        # Create the Quit button and add it to the window
        quitButton = NSButton.alloc().initWithFrame_(NSMakeRect(50, 50, 100, 40))
        quitButton.setTitle_("Quit")
        quitButton.setBezelStyle_(NSRoundedBezelStyle)
        quitButton.setTarget_(NSApplication.sharedApplication())
        quitButton.setAction_("terminate:")
        self.window.contentView().addSubview_(quitButton)

    def applicationDidFinishLaunching_(self, notification):
        self.buildUI()
        kbHandler = KBHandler()
        hks = [MultiClipboardHotKeys(), KBOTPHotKeys()]
        kbHandler.addHks(hks)
        kbHandler.run_event_loop()


# Start the application
app = NSApplication.sharedApplication()
delegate = MyApp.alloc().init()
app.setDelegate_(delegate)
app.activateIgnoringOtherApps_(True)

if __name__ == '__main__':
    app.run()
