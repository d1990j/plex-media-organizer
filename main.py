from logic import *
from ui import *
from uiUpdated import *
import tkinter as tk

def main():

    # set up UI
    root = tk.Tk()
    ui = PlexMediaOrganizerUIUPdated(root)

    # ui configuration

    # main ui loop
    root.mainloop()

if __name__ == "__main__":
    main()