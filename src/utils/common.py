import yaml
import json
import time

from src import logger
from pathlib import Path
from datetime import datetime


def read_yaml(path_to_yaml: Path):
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
        return content
    except Exception as exp:
        raise RuntimeError("unable to read the yaml")