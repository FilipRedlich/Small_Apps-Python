import webbrowser
import pyperclip
browserPath = 'C:/Program Files (x86)/Opera/launcher.exe %s'

while True:
    print("""
        What do you want to do?
        1.  Enter website
        2.  Check map
    """)
    choice = input("")
    if choice.isdecimal and choice == "1":
        url = input("Enter url \n")
        webbrowser.get(browserPath).open_new_tab(url)
        break
    elif choice.isdecimal and choice == "2":
        address = input("Enter adress or leave empty to import from clipboard \n ")
        if address == '':
            address = pyperclip.paste()
        webbrowser.get(browserPath).open_new_tab('https://www.google.com/maps/search/' + address)
        break
    else:
        print("Niepoprawny wybór")
