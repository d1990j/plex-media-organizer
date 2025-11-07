# TODO
# >>Create new window for input when selecting the media type.
# >>Allow choosing a destination directory
# >>Organize code, maybe split into multiple files

# >>>>>>>New Features<<<<<<<<
# >>Allow editing file details, can select files in library and edit title, number, date, etc and necessary folder updates will be made
# >>Allow a default directory to be set

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

#Create the window
root = tk.Tk()
root.title("Plex Media Organizer")
root.geometry("850x600")

#Core variables and helper functions
#Store media items in a list and allow user to classify each one
current_directory = ""
media_files = [] # (filename type)
selected_file = ""

#Folder browsing and file loading
def browse_directory():
    global current_directory, media_files
    current_directory = filedialog.askdirectory()
    if current_directory:
        folder_label.config(text=f"Folder: {current_directory}")
        media_files = []
        listbox.delete(0, tk.END)
        for file in os.listdir(current_directory):
            if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".mp3", ".flac", ".txt")):
                media_files.append({"name": file, "type": "Unassigned"})
                listbox.insert(tk.END, f"[Unassigned] {file}")

# Selecting and playing files
def play_selected():
    try:
        index = listbox.curselection()[0]
        file = media_files[index]["name"]
        filepath = os.path.join(current_directory, file)
        if os.name == "nt":
            os.startfile(filepath)
        elif os.name == "posix":
            subprocess.call(["xdg-open", filepath])
    except:
        messagebox.showwarning("Warning", "Please select a file to play")

# Mark as movie or tv
def mark_as_movie():
    update_media_type("Movie")
    enable_movie_info()

def mark_as_tv():
    update_media_type("TV")
    enable_tv_info()

def update_media_type(new_type):
    try:
        # Make sure only one file is assigned at a time
        for file in media_files:
            file["type"] = "Unassigned"
        index = listbox.curselection()[0]
        media_files[index]["type"] = new_type
        refresh_list()
        listbox.selection_set(index)
    except:
        messagebox.showwarning("Warning", "Select a file first")

def refresh_list():
    listbox.delete(0, tk.END)
    for m in media_files:
        listbox.insert(tk.END, f"[{m['type']}] {m['name']}")

#Rename and move files
def organize_files():
    if not current_directory:
        messagebox.showwarning("Warning", "Select a folder first")
        return
    
    base_dir = os.path.join(current_directory, "Organized")
    os.makedirs(base_dir, exist_ok=True)

    for m in media_files:
        old_path = os.path.join(current_directory, m["name"])
        if m["type"] == "Movie":
            title = movie_title_entry.get().strip() or os.path.splitext(m["name"])[0]
            year = movie_year_entry.get().strip()
            folder_name = f"{title} ({year})" if year else title
            dest_dir = os.path.join(base_dir, "Movies", folder_name)
            os.makedirs(dest_dir, exist_ok=True)
            ext = os.path.splitext(m["name"])[1]
            new_path = os.path.join(dest_dir, f"{folder_name}{ext}")
            shutil.move(old_path, new_path)
        elif m["type"] == "TV":
            show = show_name_entry.get().strip() or "Unknown Show"
            year = show_year_entry.get().strip() or ""
            season = show_season_entry.get().strip() or "1"
            episode = show_episode_entry.get().strip() or "1"
            dest_dir = os.path.join(base_dir, "TV Shows", f"{show} ({year})", f"Season {season.zfill(2)}")
            os.makedirs(dest_dir, exist_ok=True)
            ext = os.path.splitext(m["name"])[1]
            new_name = f"{show} ({year}) - S{season.zfill(2)}E{episode.zfill(2)}{ext}"
            new_path = os.path.join(dest_dir, new_name)
            shutil.move(old_path, new_path)

    messagebox.showinfo("Done", "Files have been organized into plex folders")
    clear_entries()
    browse_directory() #refresh

def clear_entries():
    movie_title_entry.delete(0, tk.END)
    movie_year_entry.delete(0, tk.END)
    show_episode_entry.delete(0, tk.END)

def enable_movie_info():
    # Enable the Movie Frame and disable the TV Frame
    tv_frame.pack_forget()
    movie_frame.pack(pady=5)

    # Reset the organize button
    organize_button.pack_forget()
    organize_button.pack(pady=10)

def enable_tv_info():
    # Enable the TV Frame and disable the Movie Frame
    movie_frame.pack_forget()
    tv_frame.pack(pady=5)

    # Reset the organize button
    organize_button.pack_forget()
    organize_button.pack(pady=10)

# Build the interface

#Folder section
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

browse_button = tk.Button(top_frame, text="Browse Folder", command=browse_directory)
browse_button.pack(side=tk.LEFT, padx=5)

folder_label = tk.Label(top_frame, text="No folder selected")
folder_label.pack(side=tk.LEFT)

# File list
listbox = tk.Listbox(root, width=100, height=15)
listbox.pack(pady=10)

# Classification buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

movie_button = tk.Button(button_frame, text="Mark as Movie", command=mark_as_movie)
movie_button.pack(side=tk.LEFT, padx=5)

tv_button = tk.Button(button_frame, text="Mark as TV Episode", command=mark_as_tv)
tv_button.pack(side=tk.LEFT, padx=5)

play_button = tk.Button(button_frame, text="Play", command=play_selected)
play_button.pack(side=tk.LEFT, padx=5)

#Metadata entry fields

#Movie Fields
movie_frame = tk.LabelFrame(root, text="Movie Info", padx=10, pady=10)

tk.Label(movie_frame, text="Title:").grid(row=0, column=0)
movie_title_entry = tk.Entry(movie_frame, width=25)
movie_title_entry.grid(row=0, column=1)

tk.Label(movie_frame, text="Year:").grid(row=0, column=2)
movie_year_entry = tk.Entry(movie_frame, width=10)
movie_year_entry.grid(row=0, column=3)

# TV Fields
tv_frame = tk.LabelFrame(root, text="TV Episode Info", padx=10, pady=10)

tk.Label(tv_frame, text="Show Name:").grid(row=0, column=0)
show_name_entry = tk.Entry(tv_frame, width=25)
show_name_entry.grid(row=0, column=1)

tk.Label(tv_frame, text="Year").grid(row=0, column=2)
show_year_entry = tk.Entry(tv_frame, width=5)
show_year_entry.grid(row=0, column=3)

tk.Label(tv_frame, text="Season:").grid(row=0,column=4)
show_season_entry = tk.Entry(tv_frame, width=5)
show_season_entry.grid(row=0, column=5)

tk.Label(tv_frame, text="Episode:").grid(row=0, column=6)
show_episode_entry = tk.Entry(tv_frame, width=5)
show_episode_entry.grid(row=0, column=7)

#Organize button
organize_button = tk.Button(root, text="Organize files", command=organize_files, bg="lightgreen")


#Run 
root.mainloop()
