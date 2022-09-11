import os
from abc import ABC


class Constants(ABC):

    # List of ignorable file names at '/data' folder (keep file extension)
    IGNORE_FILES = ['README']
    APP_ROOT_DIRECTORY: str = str(os.path.realpath('.'))
    APP_DATA_DIRECTORY: str = str(os.path.join(APP_ROOT_DIRECTORY, "data"))
    # Geographical Hierarchy Order
    GEO_HIERARCHY: set = {'continents', 'countries', 'regions',
                          'divisions', 'cities', 'districts', 'postcodes', 'upazilas'}
