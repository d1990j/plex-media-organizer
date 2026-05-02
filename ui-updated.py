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
mediaTabs = ttk.Notebook(middle_frame)

movieTab = ttk.Frame(mediaTabs)
tvTab = ttk.Frame(mediaTabs)

mediaTabs.add(movieTab, text='Movie')
mediaTabs.add(tvTab, text='TV Show')

# Movie Tab Components
movie_title_label_frame = tk.LabelFrame(movieTab, text="Title")
movie_title_entry = tk.Entry(movie_title_label_frame)
movie_title_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
movie_title_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

movie_year_label_frame = tk.LabelFrame(movieTab, text="Year")
movie_year_entry = tk.Entry(movie_year_label_frame)
movie_year_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
movie_year_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

movie_stage_button = tk.Button(movieTab, text="Stage Change")
movie_stage_button.pack(side=tk.BOTTOM, padx=5, pady=5)

# TV Tab Components
tv_title_label_frame = tk.LabelFrame(tvTab, text="Series Title")
tv_title_entry = tk.Entry(tv_title_label_frame)
tv_title_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
tv_title_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

tv_year_label_frame = tk.LabelFrame(tvTab, text="Year")
tv_year_entry = tk.Entry(tv_year_label_frame)
tv_year_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
tv_year_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

tv_season_label_frame = tk.LabelFrame(tvTab, text="Season")
tv_season_entry = tk.Entry(tv_season_label_frame)
tv_season_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
tv_season_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

tv_episode_label_frame = tk.LabelFrame(tvTab, text="Episode")
tv_episode_entry = tk.Entry(tv_episode_label_frame)
tv_episode_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
tv_episode_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

tv_stage_button = tk.Button(tvTab, text="Stage Change")
tv_stage_button.pack(side=tk.BOTTOM, padx=5, pady=5)

# Pack Middle Frame items
middle_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
listbox_labelframe.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=1)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5, pady=5)
mediaTabs.pack(expand=1, fill="both", side=tk.RIGHT, padx=10)

######################### Bottom Frame #################################
bottom_frame = tk.Frame(root)

# Buttons
play_button = tk.Button(bottom_frame, text="Play")
organize_button =  tk.Button(bottom_frame, text="Organize")

# Pack items
bottom_frame.pack(padx=10, pady=10, fill=tk.X)
play_button.pack(side=tk.LEFT, padx=5, pady=5)
organize_button.pack(side=tk.RIGHT, padx=5, pady=5)





####################### Commands ##########################


root.mainloop()