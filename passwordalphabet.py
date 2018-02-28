import pyperclip as pc
import Tkinter
import tkMessageBox as tkbox

full = []
clipboard = pc.paste()

alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima (lee-ma)',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec (keh-beck)',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X:ray',
    'Y': 'Yankee',
    'Z': 'Zulu',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero',
    '$': 'Dollar Sign',
    ':': 'Colon',
    ';': 'Semicolon',
    '`': 'Backtick',
    '~': 'Tilde',
    '\'': 'Single Quote',
    '"': 'Double Quote',
    '!': 'Exclamation Point',
    '@': 'At Sign',
    '#': 'Pound Sign',
    '$': 'Dollar Sign',
    '%': 'Percent Sign',
    '^': 'Carat',
    '&': 'Ampersand',
    '*': 'Asterisk',
    '(': 'Left Parenthesis',
    ')': 'Right Parenthesis',
    '[': 'Left Bracket',
    ']': 'Right Bracket',
    '{': 'Left Curly Brace',
    '}': 'Right Curly Brace',
    '/': 'Forward Slash',
    '\\': 'Backslash',
    '?': 'Question Mark',
    ',': 'Comma',
    '.': 'Dot',
    '-': 'Dash or Hyphen',
    '_': 'Underscore',
    '+': 'Plus',
    '=': 'Equal Sign',
    ' ': 'Space'
}

if not clipboard:
    print('no clipboard found')
else:
    for i in clipboard:
        msg = ''
        if i.isalpha():
            if i.isupper():
                msg += 'Upper Case '
            else:
                msg += 'Lower Case '
        try:
            msg += alphabet[i.upper()]
        except KeyError as e:
            print('invalid character: %s',i)
            continue
        full.append(msg)
    tkbox.showinfo('', message='\n'.join(full))
