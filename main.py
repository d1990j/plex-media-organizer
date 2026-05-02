from logic import *
from ui import *
from uiUpdated import *
from logicUpdated import persistantLogic
import tkinter as tk

def main():

    # set up UI
    root = tk.Tk()
    logic = persistantLogic()
    ui = PlexMediaOrganizerUIUPdated(root, logic)
    #ui = MediaOrganizerUI(root)

    # ui configuration

    # main ui loop
    root.mainloop()

if __name__ == "__main__":
    main()