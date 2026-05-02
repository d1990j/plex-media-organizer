import tkinter as tk
from tkinter import *
from tkinter import ttk

class PlexMediaOrganizerUIUPdated:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Plex Media Organizer")

        #################### Current Directory Widget ######################
        # Set up current directory frame
        current_directory_frame = tk.LabelFrame(root, text="Current Directory")

        # Set up buttons
        browser_button = tk.Button(current_directory_frame, text="Browse Folder", command=self.browse_button_clicked)
        default_button = tk.Button(current_directory_frame, text="Set Default", command=self.default_button_clicked)

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
        self.movie_title_entry = tk.Entry(movie_title_label_frame)
        movie_title_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.movie_title_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

        movie_year_label_frame = tk.LabelFrame(movieTab, text="Year")
        self.movie_year_entry = tk.Entry(movie_year_label_frame)
        movie_year_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.movie_year_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

        movie_stage_button = tk.Button(movieTab, text="Stage Change", command=self.movie_stage_button_clicked)
        movie_stage_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        # TV Tab Components
        tv_title_label_frame = tk.LabelFrame(tvTab, text="Series Title")
        self.tv_title_entry = tk.Entry(tv_title_label_frame)
        tv_title_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.tv_title_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

        tv_year_label_frame = tk.LabelFrame(tvTab, text="Year")
        self.tv_year_entry = tk.Entry(tv_year_label_frame)
        tv_year_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.tv_year_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

        tv_season_label_frame = tk.LabelFrame(tvTab, text="Season")
        self.tv_season_entry = tk.Entry(tv_season_label_frame)
        tv_season_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.tv_season_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

        tv_episode_label_frame = tk.LabelFrame(tvTab, text="Episode")
        self.tv_episode_entry = tk.Entry(tv_episode_label_frame)
        tv_episode_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.tv_episode_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

        tv_stage_button = tk.Button(tvTab, text="Stage Change", command=self.tv_stage_button_clicked)
        tv_stage_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        # Pack Middle Frame items
        middle_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
        listbox_labelframe.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=1)
        file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5, pady=5)
        mediaTabs.pack(expand=1, fill="both", side=tk.RIGHT, padx=10)

        ######################### Bottom Frame #################################
        bottom_frame = tk.Frame(root)

        # Buttons
        play_button = tk.Button(bottom_frame, text="Play", command=self.play_button_clicked)
        organize_button =  tk.Button(bottom_frame, text="Organize", command=self.organize_button_clicked)

        # Pack items
        bottom_frame.pack(padx=10, pady=10, fill=tk.X)
        play_button.pack(side=tk.LEFT, padx=5, pady=5)
        organize_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def browse_button_clicked(self):
        print("Browse Clicked")

    def default_button_clicked(self):
        print("Default clicked")

    def movie_stage_button_clicked(self):
        # Send to console for testing
        print("Stage movie")

        # Get a reference to the data entered
        movie_title = self.movie_title_entry.get()
        movie_year = self.movie_year_entry.get()

        # Print for testing
        print(movie_title, movie_year)

        # Initiate function here

        # Clear fields
        self.movie_title_entry.delete(0, END)
        self.movie_year_entry.delete(0, END)

    def tv_stage_button_clicked(self):
        # Send to console for testing
        print("Stage tv")

        # Get a reference to the data entry fields
        tv_title = self.tv_title_entry.get()
        tv_year = self.tv_year_entry.get()
        tv_season = self.tv_season_entry.get()
        tv_episode = self.tv_episode_entry.get()

        # Print for testing
        print(tv_title, tv_year, tv_season, tv_episode)

    def play_button_clicked(self):
        print("Play media")

    def organize_button_clicked(self):
        print("Organize media")

# root = tk.Tk()

# root.title("Plex Media Organizer")

# #################### Current Directory Widget ######################
# # Set up current directory frame
# current_directory_frame = tk.LabelFrame(root, text="Current Directory")

# # Set up buttons
# browser_button = tk.Button(current_directory_frame, text="Browse Folder")
# default_button = tk.Button(current_directory_frame, text="Set Default")

# # Set up current directory label
# current_directory_label = tk.Label(current_directory_frame, text="file/path/here")

# # Pack current directory frame items
# current_directory_frame.pack(pady=10,padx=10)
# browser_button.pack(side=tk.LEFT, padx=5, pady=5)
# default_button.pack(side=tk.LEFT, padx=5, pady=5)
# current_directory_label.pack(side=tk.LEFT, padx=5, pady=5)

# ##################### Middle Frame ##############################
# middle_frame = tk.Frame(root)
# listbox_labelframe = tk.LabelFrame(middle_frame, text="Media Files")

# ### File Listbox
# file_listbox = tk.Listbox(listbox_labelframe, width=50, height=15)

# ### Movie/TV Show Tabs
# mediaTabs = ttk.Notebook(middle_frame)

# movieTab = ttk.Frame(mediaTabs)
# tvTab = ttk.Frame(mediaTabs)

# mediaTabs.add(movieTab, text='Movie')
# mediaTabs.add(tvTab, text='TV Show')

# # Movie Tab Components
# movie_title_label_frame = tk.LabelFrame(movieTab, text="Title")
# self.movie_title_entry = tk.Entry(movie_title_label_frame)
# movie_title_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# self.movie_title_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

# movie_year_label_frame = tk.LabelFrame(movieTab, text="Year")
# self.movie_year_entry = tk.Entry(movie_year_label_frame)
# movie_year_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# self.movie_year_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

# movie_stage_button = tk.Button(movieTab, text="Stage Change")
# movie_stage_button.pack(side=tk.BOTTOM, padx=5, pady=5)

# # TV Tab Components
# tv_title_label_frame = tk.LabelFrame(tvTab, text="Series Title")
# self.tv_title_entry = tk.Entry(tv_title_label_frame)
# tv_title_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# self.tv_title_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

# tv_year_label_frame = tk.LabelFrame(tvTab, text="Year")
# self.tv_year_entry = tk.Entry(tv_year_label_frame)
# tv_year_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# self.tv_year_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

# tv_season_label_frame = tk.LabelFrame(tvTab, text="Season")
# self.tv_season_entry = tk.Entry(tv_season_label_frame)
# tv_season_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# self.tv_season_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

# tv_episode_label_frame = tk.LabelFrame(tvTab, text="Episode")
# self.tv_episode_entry = tk.Entry(tv_episode_label_frame)
# tv_episode_label_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# self.tv_episode_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

# tv_stage_button = tk.Button(tvTab, text="Stage Change")
# tv_stage_button.pack(side=tk.BOTTOM, padx=5, pady=5)

# # Pack Middle Frame items
# middle_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
# listbox_labelframe.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=1)
# file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5, pady=5)
# mediaTabs.pack(expand=1, fill="both", side=tk.RIGHT, padx=10)

# ######################### Bottom Frame #################################
# bottom_frame = tk.Frame(root)

# # Buttons
# play_button = tk.Button(bottom_frame, text="Play")
# organize_button =  tk.Button(bottom_frame, text="Organize")

# # Pack items
# bottom_frame.pack(padx=10, pady=10, fill=tk.X)
# play_button.pack(side=tk.LEFT, padx=5, pady=5)
# organize_button.pack(side=tk.RIGHT, padx=5, pady=5)

# root.mainloop()