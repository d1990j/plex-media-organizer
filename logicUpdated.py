# IMPORTS
import os
import json
from pathlib import Path
import shutil
from tkinter import filedialog, messagebox

DEFAULT_CONFIG = {
    "default_directory": ""
}

CONFIG_FILENAME = "config.json"

class persistantLogic:
    def __init__(self):
        self.current_directory = self.get_default_directory()
        self.media_files = [] # (filename type)
        self.selected_file = dict()
        self.destination_directory = ""

    def get_default_directory(self):
        """Return the absolute path to the default directory."""
        config = self.load_config()
        return config["default_directory"]
    
    def get_config_path(self) -> Path:
        """Return the absolute path to the config file."""
        return Path(__file__).with_name(CONFIG_FILENAME)
    
    def load_config(self) -> dict:
        """Load the config from disk, falling back to defaults if missing or corrupt."""
        config_path = self.get_config_path()

        if not config_path.is_file():
            # No file yet, write default and return
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with config_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            # Corrupted file - reset to defaults
            print("Warning: config file unreadable - resetting to defaults")
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        # Merge defaults with loaded values so new keys get added automatically
        merged = DEFAULT_CONFIG.copy()
        merged.update(data)
        return merged
    
    def save_config(self, config: dict) -> None:
        """Write the given config dictionary to disk."""
        config_path = self.get_config_path()
        try:
            with config_path.open("w", encoding="utf-8") as f:
                json.dump(config, f, indent=4, sort_keys=True)
        except OSError as exc:
            print(f"Failed to write config file: {exc}")

    def browse_directory(self):
        """Open a dialog to select a directory and then refresh the list."""
        self.current_directory = filedialog.askdirectory(initialdir=self.current_directory if self.current_directory else os.getcwd())
        #self.load_media_files()

    def set_default_directory(self):
        """Set the default directory to use on startup."""
        config = self.load_config()
        config["default_directory"] = self.current_directory
        self.save_config(config)

        messagebox.showinfo("Done", f"Default directory set to {self.current_directory}")
