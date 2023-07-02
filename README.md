# HotKey

Map keys and sequences to execute Python code

How to use:

1. OS<br>
   For Windows: Delete the mac folder<br>
   For Mac: Replace the files in the root folder with files from the mac folder
2. HotKeys<br>
   Configure hotkeys in HotKeyClasses folder
3. Bind HotKey classes in HotKeyRunner.py
4. Run pyinstaller with -w and -i hkr.png
5. Run application on startup

Examples:<br>
- KeyboardCleaner <br>Disables the entire keyboard to facilitate cleaning
- KBOTP <br>Generates and injects an OTP into a text box
- MultiClipboard <br>Clipboard manager
- SwtichFromMac <br>Maps alt key to ctrl key so muscle memory is maintaned from using a Mac
- Volume <br>Maps 2 function keys (or any 2 keys) to volume up and volume down
