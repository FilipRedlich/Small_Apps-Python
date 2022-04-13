# program that adds something on the start of the lines of text in your clipboard

import pyperclip
text = pyperclip.paste()        # writes text from the clipboard

lines = text.split('\n')        # splits "lines"
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)         # joins "lines"

pyperclip.copy(text)            # copies 'text' to the clipboard