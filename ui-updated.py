import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()

root.title("Plex Media Organizer")

#################### Current Directory Widget ######################
# Set up current directory frame
current_directory_frame = tk.LabelFrame(root, text="Current Directory")

# Set up buttons
browser_button = tk.Button(current_directory_frame, text="Browse Folder")
default_button = tk.Button(current_directory_frame, text="Set Default")

# Set up current directory label
current_directory_label = tk.Label(current_directory_frame, text="file/path/here")

# Pack current directory frame items
current_directory_frame.pack(pady=10,padx=10)
browser_button.pack(side=tk.LEFT, padx=5, pady=5)
default_button.pack(side=tk.LEFT, padx=5, pady=5)
current_directory_label.pack(side=tk.LEFT, padx=5, pady=5)

##################### Middle Frame ##############################
middle_frame = tk.Frame(root)

### File Listbox
file_listbox = tk.Listbox(middle_frame, width=50, height=15)

### Movie/TV Show Tabs
tabControl = ttk.Notebook(middle_frame)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Movie')
tabControl.add(tab2, text='TV Show')

ttk.Label(tab1, text="Welcome").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2, text="Hello world").grid(column=0, row=0, padx=30, pady=30)

# Pack Middle Frame items
middle_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
tabControl.pack(expand=1, fill="both", side=tk.RIGHT, padx=10)

root.mainloop()