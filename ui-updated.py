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
listbox_labelframe = tk.LabelFrame(middle_frame, text="Media Files")

### File Listbox
file_listbox = tk.Listbox(listbox_labelframe, width=50, height=15)

### Movie/TV Show Tabs
tabControl = ttk.Notebook(middle_frame)

movieTab = ttk.Frame(tabControl)
tvTab = ttk.Frame(tabControl)

tabControl.add(movieTab, text='Movie')
tabControl.add(tvTab, text='TV Show')

ttk.Label(movieTab, text="Welcome").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tvTab, text="Hello world").grid(column=0, row=0, padx=30, pady=30)

# Pack Middle Frame items
middle_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
listbox_labelframe.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=1)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
tabControl.pack(expand=1, fill="both", side=tk.RIGHT, padx=10)

######################### Bottom Frame #################################
bottom_frame = tk.Frame(root)

# Buttons
play_button = tk.Button(bottom_frame, text="Play")
organize_button =  tk.Button(bottom_frame, text="Organize")

# Pack items
bottom_frame.pack(padx=10, pady=10, fill=tk.X)
play_button.pack(side=tk.LEFT, padx=5, pady=5)
organize_button.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()