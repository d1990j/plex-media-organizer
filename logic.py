import os
import subprocess
from tkinter import messagebox
import shutil

def retrieve_files(directory):
    media_files = []

    for file in os.listdir(directory):
        if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".mp3", ".flac", ".txt")):
                media_files.append({"name": file, "type": "Unassigned"})

    return media_files

def organize_movie(current_directory: str, file: dict, title: str, year: str):
    # create the organized folder if not existing
    base_dir = os.path.join(current_directory, "Organized")
    os.makedirs(base_dir, exist_ok=True)

    # Record the old path to the file
    old_path = os.path.join(current_directory, file["name"])

    # Create the new folder structure and make the directory
    folder_name = f"{title} ({year})" if year else title
    dest_dir = os.path.join(base_dir, "Movies", folder_name)
    os.makedirs(dest_dir, exist_ok=True)

    # Move the file
    ext = os.path.splitext(file["name"])[1]
    new_path = os.path.join(dest_dir, f"{folder_name}{ext}")
    shutil.move(old_path, new_path)

def orgainze_tv(current_directory: str, file: dict, show: str, year: str, season: str, episode: str):
     # create the organized folder if not existing
    base_dir = os.path.join(current_directory, "Organized")
    os.makedirs(base_dir, exist_ok=True)

    # Record the old path to the file
    old_path = os.path.join(current_directory, file["name"])

    # Create the new folder structure and make the directory
    dest_dir = os.path.join(base_dir, "TV Shows", f"{show} ({year})", f"Season {season.zfill(2)}")
    os.makedirs(dest_dir, exist_ok=True)

    # Move the file
    ext = os.path.splitext(file["name"])[1]
    new_name = f"{show} ({year}) - S{season.zfill(2)}E{episode.zfill(2)}{ext}"
    new_path = os.path.join(dest_dir, new_name)
    shutil.move(old_path, new_path)
     