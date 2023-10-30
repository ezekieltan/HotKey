import platform

operatingSystem = 'mac' if platform.system() == "Darwin" else (
    'windows' if platform.system() == "Windows" else ('linux' if platform.system() == "Linux" else ''))

vkToCharMac = {
    0: 'A',
    1: 'S',
    2: 'D',
    3: 'F',
    4: 'H',
    5: 'G',
    6: 'Z',
    7: 'X',
    8: 'C',
    9: 'V',
    11: 'B',
    12: 'Q',
    13: 'W',
    14: 'E',
    15: 'R',
    16: 'Y',
    17: 'T',
    18: '1',
    19: '2',
    20: '3',
    21: '4',
    22: '6',
    23: '5',
    24: '=',
    25: '9',
    26: '7',
    27: '-',
    28: '8',
    29: '0',
    30: ']',
    31: 'O',
    32: 'U',
    33: '[',
    34: 'I',
    35: 'P',
    36: 'return',
    37: 'L',
    38: 'J',
    39: "'",
    40: 'K',
    41: ';',
    42: '\\',
    43: ',',
    44: '/',
    45: 'N',
    46: 'M',
    47: '.',
    48: 'tab',
    49: ' ',
    50: '`',
    51: 'delete',
    53: 'esc',
    54: 'rcmd',
    55: 'cmd',
    56: 'shift',
    57: 'capslock',
    58: 'option',
    59: 'ctrl',
    60: 'rshift',
    61: 'roption',
    63: 'fn',
    123: 'left',
    124: 'right',
    125: 'down',
    126: 'up',
    122: 'F1',
    120: 'F2',
    99: 'F3',
    118: 'F4',
    96: 'F5',
    97: 'F6',
    98: 'F7',
    100: 'F8',
    101: 'F9',
    109: 'F10',
    103: 'F11',
    111: 'F12',
    105: 'F13',
    107: 'F14',
    113: 'F15',
    106: 'F16',
    64: 'F17',
    79: 'F18',
    80: 'F19',
    90: 'F20',
    179: 'fn',
}

vkToCharWindows = {
    0: 'reserved',
    1: 'lmouse',
    2: 'rmouse',
    3: 'controlbreakprocessing',
    4: 'mmouse',
    5: 'x1mouse',
    6: 'x2mouse',
    8: 'backspace',
    9: 'tab',
    12: 'clear',
    13: 'enter',
    14: 'clear',
    16: 'shift',
    17: 'control',
    18: 'alt',
    19: 'pause',
    20: 'capslock',
    21: 'imekana',
    23: 'imejunja',
    24: 'imefinal',
    25: 'imehanja',
    27: 'escape',
    29: 'imekanji',
    32: 'space',
    33: 'pgup',
    34: 'pgdown',
    35: 'end',
    36: 'home',
    37: 'left',
    38: 'up',
    39: 'right',
    40: 'down',
    41: 'select',
    42: 'print',
    43: 'execute',
    44: 'printscreen',
    45: 'insert',
    46: 'delete',
    47: 'help',
    48: '0',
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',
    65: 'A',
    66: 'B',
    67: 'C',
    68: 'D',
    69: 'E',
    70: 'F',
    71: 'G',
    72: 'H',
    73: 'I',
    74: 'J',
    75: 'K',
    76: 'L',
    77: 'M',
    78: 'N',
    79: 'O',
    80: 'P',
    81: 'Q',
    82: 'R',
    83: 'S',
    84: 'T',
    85: 'U',
    86: 'V',
    87: 'W',
    88: 'X',
    89: 'Y',
    90: 'Z',
    91: 'win',
    92: 'rwin',
    93: 'apps',
    95: 'sleep',
    96: 'numpad0',
    97: 'numpad1',
    98: 'numpad2',
    99: 'numpad3',
    100: 'numpad4',
    101: 'numpad5',
    102: 'numpad6',
    103: 'numpad7',
    104: 'numpad8',
    105: 'numpad9',
    106: 'multiply',
    107: 'add',
    109: 'subtract',
    110: 'decimal',
    111: 'divide',
    112: 'F1',
    113: 'F2',
    114: 'F3',
    115: 'F4',
    116: 'F5',
    117: 'F6',
    118: 'F7',
    119: 'F8',
    120: 'F9',
    121: 'F10',
    122: 'F11',
    123: 'F12',
    124: 'F13',
    125: 'F14',
    126: 'F15',
    127: 'F16',
    128: 'F17',
    129: 'F18',
    130: 'F19',
    131: 'F20',
    132: 'F21',
    133: 'F22',
    134: 'F23',
    135: 'F24',
    144: 'numlock',
    145: 'scrolllock',
    160: 'shift',
    161: 'rshift',
    162: 'ctrl',
    163: 'rctrl',
    164: 'alt',
    165: 'ralt',
    166: 'browserback',
    167: 'browserforward',
    168: 'browserrefresh',
    169: 'browserstop',
    170: 'browsersearch',
    171: 'browserfavourites',
    172: 'browserhome',
    173: 'mute',
    174: 'voldown',
    175: 'volup',
    176: 'forward',
    177: 'rewind',
    178: 'stop',
    179: 'play',
    180: 'mail',
    181: 'media',
    182: 'app1',
    183: 'app2',
    186: 'semicolon',
    187: 'plus',
    188: 'comma',
    189: 'minus',
    190: 'period',
    191: 'slash',
    192: 'tilde',
    219: 'opensquarebracket',
    220: 'backslash',
    221: 'closesquarebracket',
    222: 'apostrophe',
}


vkToCharLinux = {
    1: 'esc',
    2: '1',
    3: '2',
    4: '3',
    5: '4',
    6: '5',
    7: '6',
    8: '7',
    9: '8',
    10: '9',
    11: '0',
    12: 'minus',
    13: 'equals',
    14: 'backspace',
    15: 'tab',
    16: 'Q',
    17: 'W',
    18: 'E',
    19: 'R',
    20: 'T',
    21: 'Y',
    22: 'U',
    23: 'I',
    24: 'O',
    25: 'P',
    26: 'opensquarebracket',
    27: 'closedsquarebracket',
    28: 'enter',
    29: 'ctrl',
    30: 'A',
    31: 'S',
    32: 'D',
    33: 'F',
    34: 'G',
    35: 'H',
    36: 'J',
    37: 'K',
    38: 'L',
    39: 'semicolon',
    40: '\'',
    41: 'tilde',
    42: 'shift',
    43: '\\',
    44: 'Z',
    45: 'X',
    46: 'C',
    47: 'V',
    48: 'B',
    49: 'N',
    50: 'M',
    51: 'comma',
    52: 'period',
    53: 'slash',
    54: 'rshift',
    56: 'alt',
    57: 'space',
    58: 'capslock',
    59: 'F1',
    60: 'F2',
    61: 'F3',
    62: 'F4',
    63: 'F5',
    64: 'F6',
    65: 'F7',
    66: 'F8',
    67: 'F9',
    68: 'F10',
    69: 'numlock',
    87: 'F11',
    88: 'F12',
    100: 'ralt',
    82: 'numpad0',
    79: 'numpad1',
    80: 'numpad2',
    81: 'numpad3',
    75: 'numpad4',
    76: 'numpad5',
    77: 'numpad6',
    71: 'numpad7',
    72: 'numpad8',
    73: 'numpad9',
    55: 'multiply',
    78: 'add',
    74: 'subtract',
    83: 'decimal',
    70: 'scrolllock',
    119: 'pause',
    98: 'divide',
    96: 'enter',
    99: 'printscreen',
    102: 'home',
    110: 'insert',
    113: 'mute',
    115: 'volup',
    114: 'voldown',
    125: 'win',
    127: 'menu',
    104: 'pgup',
    109: 'pgdown',
    111: 'delete',
    107: 'end',
    103: 'up',
    108: 'down',
    105: 'left',
    106: 'right',
    164: 'play',
    165: 'rewind',
    163: 'forward',
    166: 'stop',
}

vkToChar = vkToCharMac if operatingSystem == 'mac' else vkToCharWindows if operatingSystem == 'windows' else vkToCharLinux

vkToChar = {key: value.upper() for key, value in vkToChar.items()}

charToVk = {value.upper(): key for key, value in vkToChar.items()}