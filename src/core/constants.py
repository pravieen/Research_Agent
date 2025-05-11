import os
from pathlib import Path
from src.utils.common import read_yaml

CONFIG_FILE_PATH = Path("./configs/secrets.yml")
CONFIGURATION = read_yaml(CONFIG_FILE_PATH)