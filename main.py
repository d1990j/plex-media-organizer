from logic import *
from ui import *
import tkinter as tk

def main():

    # set up UI
    root = tk.Tk()
    ui = MediaOrganizerUI(root)

    # ui configuration

    # main ui loop
    root.mainloop()

if __name__ == "__main__":
    main()