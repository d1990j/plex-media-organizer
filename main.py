from uiUpdated import *
from logicUpdated import persistantLogic
import tkinter as tk
import constants as const

def main():

    # set up UI
    root = tk.Tk()
    logic = persistantLogic()
    ui = PlexMediaOrganizerUIUPdated(root, logic)

    # main ui loop
    root.mainloop()

if __name__ == "__main__":
    main()