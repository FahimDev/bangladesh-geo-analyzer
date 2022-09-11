import os
import json
import math
#from dateutil import parser
from .abstract.i_data_query import IDataQuery


class DataQuery(IDataQuery):
    """
    This class is responsible for collecting, stocking and arranging data and serving basic query operations.
    """

    def collect_all_json_data(self, directory_path: str) -> dict:
        file_names: list = self.find_files(directory_path) 
               
        
    def _find_files(self, directory_path: str) -> list:
        file_names: list = os.listdir(directory_path)
        return file_names
