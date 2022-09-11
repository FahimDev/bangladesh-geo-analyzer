import os
from abc import ABC


class Constants(ABC):

    # List of ignorable file names at '/data' folder (keep file extension)
    IGNORE_FILES = ['README']
    APP_ROOT_DIRECTORY: str = str(os.path.realpath('.'))
    APP_DATA_DIRECTORY: str = str(os.path.join(APP_ROOT_DIRECTORY, "data"))
    GEO_HIERARCHY: set = {'country', 'divisions', 'districts', 'postcodes', 'upazilas'}
