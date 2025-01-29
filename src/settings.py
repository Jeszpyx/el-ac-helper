from typing import TypedDict, Literal
import os
import json
from enum import Enum

class BackgroundColor(Enum):
    WHITE = "white"
    BLACK = "black"
    CUSTOM = "custom"


class Settings(TypedDict):
    is_default_path: bool
    config_ini_custom_path: None | str
    background: BackgroundColor


KeyType = Literal["is_default_path", "config_ini_custom_path", "background"]

settings_file = "settings.json"

default_settings: Settings = {
    "is_default_path": True,
    "config_ini_custom_path": None,
    "background": BackgroundColor.WHITE.value,
}


def save_settings(settings: Settings):
    with open(settings_file, "w") as file:
        json.dump(settings, file, indent=4)


def update_settings(key: KeyType, value):
    with open(settings_file, "r") as file:
        data = json.load(file)
    file.close()

    data[key] = value

    with open(settings_file, "w") as file:
        json.dump(data, file, indent=4)
    file.close()


def load_settings():
    try:
        with open(settings_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_settings


if not os.path.exists(settings_file):
    print(default_settings)
    with open(settings_file, "w") as file:
        json.dump(default_settings, file, indent=4)
    file.close()
    settings = load_settings()
else:
    settings = load_settings()