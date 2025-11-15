import tkinter as tk
from tkinter import filedialog, messagebox
import os
import logic
import subprocess
from configparser import ConfigParser

class MediaOrganizerUI:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Plex Media Organizer")
        self.root.geometry("850x600")

        # Set up variables
        self.current_directory = logic.get_default_directory()
        self.media_files = [] # (filename type)
        self.selected_file = dict()

        # Set up folder section
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        self.browse_button = tk.Button(top_frame, text="Browse Folder", command=self.browse_directory)
        self.browse_button.pack(side=tk.LEFT, padx=5)

        self.default_button = tk.Button(top_frame, text="Set Default", command=self.set_default_directory)
        self.default_button.pack(side=tk.LEFT, padx=5)

        self.folder_label = tk.Label(top_frame, text=self.current_directory if self.current_directory else "No folder selected")
        self.folder_label.pack(side=tk.LEFT)

        # Set up file list
        self.listbox = tk.Listbox(self.root, width=100, height=15)
        self.listbox.pack(padx=10)

        # Set up Classification buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.movie_button = tk.Button(button_frame, text="Mark as Movie", command=self.mark_as_movie)
        self.movie_button.pack(side=tk.LEFT, padx=5)

        self.tv_button = tk.Button(button_frame, text="Mark as TV Episode", command=self.mark_as_tv)
        self.tv_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(button_frame, text="Play", command=self.play_selected)
        self.play_button.pack(side=tk.LEFT, padx=5)

        ### Data entry fields ###

        # Movie fields
        self.movie_frame = tk.LabelFrame(self.root, text="Movie Info", padx=10, pady=10)

        tk.Label(self.movie_frame, text="Title:").grid(row=0, column=0)
        self.movie_title_entry = tk.Entry(self.movie_frame, width=25)
        self.movie_title_entry.grid(row=0, column=1)

        tk.Label(self.movie_frame, text="Year:").grid(row=0, column=2)
        self.movie_year_entry = tk.Entry(self.movie_frame, width=10)
        self.movie_year_entry.grid(row=0, column=3)

        # TV Fields
        self.tv_frame = tk.LabelFrame(self.root, text="TV Episode Info", padx=10, pady=10)

        tk.Label(self.tv_frame, text="Show Name:").grid(row=0, column=0)
        self.show_name_entry = tk.Entry(self.tv_frame, width=25)
        self.show_name_entry.grid(row=0, column=1)

        tk.Label(self.tv_frame, text="Year").grid(row=0, column=2)
        self.show_year_entry = tk.Entry(self.tv_frame, width=5)
        self.show_year_entry.grid(row=0, column=3)

        tk.Label(self.tv_frame, text="Season:").grid(row=0,column=4)
        self.show_season_entry = tk.Entry(self.tv_frame, width=5)
        self.show_season_entry.grid(row=0, column=5)

        tk.Label(self.tv_frame, text="Episode:").grid(row=0, column=6)
        self.show_episode_entry = tk.Entry(self.tv_frame, width=5)
        self.show_episode_entry.grid(row=0, column=7)

        # Organize Button
        self.organize_button = tk.Button(root, text="Organize files", bg="lightgreen", command=self.organize_files)

    # Enable/disable movie and tv info
    def enable_movie_info(self):
        # Enable the Movie Frame and disable the TV Frame
        self.tv_frame.pack_forget()
        self.movie_frame.pack(pady=5)

        # Reset the organize button
        self.organize_button.pack_forget()
        self.organize_button.pack(pady=10)

    def enable_tv_info(self):
        # Enable the TV Frame and disable the Movie Frame
        self.movie_frame.pack_forget()
        self.tv_frame.pack(pady=5)

        # Reset the organize button
        self.organize_button.pack_forget()
        self.organize_button.pack(pady=10)

    # Clear all entry fields
    def clear_entries(self):
        self.movie_title_entry.delete(0, tk.END)
        self.movie_year_entry.delete(0, tk.END)
        self.show_episode_entry.delete(0, tk.END)

    # Update media to new type
    def update_media_type(self, new_type):
        try:
            # Make sure only one file is assigned at a time
            for file in self.media_files:
                file["type"] = "Unassigned"
            index = self.listbox.curselection()[0]
            self.media_files[index]["type"] = new_type
            self.selected_file = self.media_files[index]
            self.refresh_list()
            self.listbox.selection_set(index)
        except:
            messagebox.showwarning("Warning", "Select a file first")

    # Refresh the list with updated media files
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for m in self.media_files:
            self.listbox.insert(tk.END, f"[{m['type']}] {m['name']}")

    ### Button Commands ###

    # Browse for current directory
    def browse_directory(self):
        self.current_directory = filedialog.askdirectory()
        self.load_media_files()

    def load_media_files(self):
        # If a directory is chosen
        if self.current_directory:
            # Update the label to the currently selected directory
            self.folder_label.config(text=f"Folder: {self.current_directory}")

            # Reset media files
            self.media_files = []

            # Delete any current media files in listbox
            self.listbox.delete(0, tk.END)

            # Retrieve files and populate listbox
            self.media_files = logic.retrieve_files(self.current_directory)

            # Populate the listbox
            for file in self.media_files:
                file_type = file["type"]
                file_name = file["name"]
                self.listbox.insert(tk.END, f"[{file_type}] {file_name}")

    # Play the selected file
    def play_selected(self):
        try:
            index = self.listbox.curselection()[0]
            file = self.media_files[index]["name"]
            filepath = os.path.join(self.current_directory, file)
            # Determine OS, nt for windows, posix for mac/linux
            if os.name == "nt":
                os.startfile(filepath)
            elif os.name == "posix":
                subprocess.call(["xdg-open", filepath])
        except:
            messagebox.showwarning("Warning", "Please select a file to play")

    # Mark as a movie or tv show
    def mark_as_movie(self):
        self.update_media_type("Movie")
        self.enable_movie_info()

    def mark_as_tv(self):
        self.update_media_type("TV")
        self.enable_tv_info()

    # Rename and move files
    def organize_files(self):
        # Make sure folder has been selected
        if not self.current_directory:
            messagebox.showwarning("Warning", "Select a folder first")
            return
        
        # Get currently selected file and organize
        try:
            file = self.selected_file

            if file["type"] == "Movie":
                title = self.movie_title_entry.get().strip() or os.path.splitext(file["name"])[0]
                year = self.movie_year_entry.get().strip()
                logic.organize_movie(self.current_directory, file, title, year)

                messagebox.showinfo("Done", "Files have been organized into plex folders")
                self.clear_entries()
                self.load_media_files() #refresh
            elif file["type"] == "TV":
                show = self.show_name_entry.get().strip() or "Unknown Show"
                year = self.show_year_entry.get().strip() or ""
                season = self.show_season_entry.get().strip() or "1"
                episode = self.show_episode_entry.get().strip() or "1"

                logic.orgainze_tv(self.current_directory, file, show, year, season, episode)
                messagebox.showinfo("Done", "Files have been organized into plex folders")
                self.clear_entries()
                self.load_media_files() #refresh
            else:
                messagebox.showwarning("Warning", "Assign media type first")

        except:
            messagebox.showwarning("Warning", "Select a file first")

    def set_default_directory(self):
        logic.set_default_directory(self.current_directory)
        messagebox.showinfo("Done", f"Default directory set to {self.current_directory}")