import os
import json
from pathlib import Path
import shutil

DEFAULT_CONFIG = {
    "default_directory": ""
}

CONFIG_FILENAME = "config.json"

def retrieve_files(directory):
    """Retrieve an array of all media files in the directory."""
    media_files = []

    for file in os.listdir(directory):
        if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".mp3", ".flac", ".txt")):
                media_files.append({"name": file, "type": "Unassigned"})

    return media_files

def organize_movie(current_directory: str, file: dict, title: str, year: str):
    """Organize the movie into the appropriate format of folders and titles."""
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
    """Organize the tv episode into the appropriate format of folders and titles."""
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

def get_default_directory():
    """Return the absolute path to the default directory."""
    config = load_config()
    return config["default_directory"]

def set_default_directory(directory: str):
    """Set the default directory to use on startup."""
    config = load_config()
    config["default_directory"] = directory
    save_config(config)

def get_config_path() -> Path:
    """Return the absolute path to the config file."""
    return Path(__file__).with_name(CONFIG_FILENAME)

def load_config() -> dict:
    """Load the config from disk, falling back to defaults if missing or corrupt."""
    config_path = get_config_path()

    if not config_path.is_file():
        # No file yet, write default and return
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

    try:
        with config_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        # Corrupted file - reset to defaults
        print("Warning: config file unreadable - resetting to defaults")
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

    # Merge defaults with loaded values so new keys get added automatically
    merged = DEFAULT_CONFIG.copy()
    merged.update(data)
    return merged

def save_config(config: dict) -> None:
    """Write the given config dictionary to disk."""
    config_path = get_config_path()
    try:
        with config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, sort_keys=True)
    except OSError as exc:
        print(f"Failed to write config file: {exc}")