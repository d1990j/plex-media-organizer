from logic import *
from ui import *
import tkinter as tk

# TODO
# Reconfiure the files to run as instances. The UI will be an instance that simply builds the UI.
# For functionality of buttons, make a file for button logic that has an instane connected to the UI
# so that the appropriate calls can be made back and forth for changes.
# Make proper get/set functions in each, as needed, to allow safe access and changes.

def main():

    # set up UI
    root = tk.Tk()
    ui = MediaOrganizerUI(root)

    # ui configuration

    # main ui loop
    root.mainloop()

if __name__ == "__main__":
    main()