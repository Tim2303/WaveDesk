from pathlib import Path
import json

class ConfigManager:
    """
    Class for managing config.json file
    Automatically creates config file with default values
    """

    def __init__(self, file_name="config.json"):
        self.file_path = Path(file_name)
        self.data = {}
        self._ensure_config_exists()
        self.load_data()

    def _default_init(self):
        """Creates JSON-file with default values."""
        default_data = {
            'dirs_array': ["audio"],
            'volume': 80,
            'output_device': 'default'
        }

        with self.file_path.open('w', encoding='utf-8') as f:
            json.dump(default_data, f, indent=4)
        return default_data

    def _ensure_config_exists(self):
        """Check if config file exists and creates if needed."""
        if not self.file_path.exists():
            print(f"File '{self.file_path}' not found. Creating default config...")
            self._default_init()

    def load_data(self):
        """Load data from config file."""
        try:
            with self.file_path.open('r', encoding='utf-8') as f:
                self.data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Failed to read config file: {e}. Create default config.")
            self.data = self._default_init()

    def save_data(self):
        """Save current data to config file."""
        with self.file_path.open('w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)

    def get(self, key, default=None):
        """Get value from config file by key."""
        return self.data.get(key, default)

    def set(self, key, value):
        """Set value by key and save current data."""
        self.data[key] = value
        self.save_data()