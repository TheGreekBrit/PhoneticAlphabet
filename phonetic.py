try:
    import Tkinter as tk
    import tkMessageBox as tkbox
except ImportError as e:
    print(e)
    import tkinter as tk
import sys,json

with open('alphabet.json', 'r') as f:
    alphabet = json.load(f)

root = tk.Tk()

try:
    clipboard = root.clipboard_get()
except:
    print('no clipboard found')
    root.destroy()
    sys.exit()

full = []

if not clipboard:
    print('no clipboard found')
else:
    full.append(clipboard)
    full.append('')
    for i in clipboard:
        msg = ''
        try:
            if i.isalpha():
                full.append('%s as in %s' % (i, alphabet[i.upper()]))
            elif i.isdigit():
                full.append('The number %s' % alphabet[i.upper()])
            else:
                full.append(alphabet[i])
        except KeyError as e:
            print('invalid character: %s' % i)
            continue
    if tkbox.showinfo(clipboard,message='\n'.join(full)):
        root.destroy()
