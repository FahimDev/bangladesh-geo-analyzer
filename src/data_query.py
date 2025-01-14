import os
import json
import math
#from dateutil import parser
from .abstract.i_data_query import IDataQuery


class DataQuery(IDataQuery):
    """
    This class is responsible for collecting, stocking and arranging data and serving basic query operations.
    """
    
    def get_geojson(self, data_directory_path: str, file_name: str) -> dict:
        file_path_location:str = str(os.path.join(data_directory_path, file_name))
        # Opening JSON file
        json_file = open(file_path_location)
        # returns JSON object as a dictionary
        json_data = json.load(json_file)
        # Closing file
        json_file.close()
        return json_data
    
    def collect_all_json_data(self, directory_path: str, geo_hierarchy_sequence: set) -> dict:
        file_names: list = self.find_files(directory_path) 
        geo: dict = self.geo_hierarchy_manager(directory_path, file_names)
               
    def geo_hierarchy_manager(self, directory_path: str, file_names: list, geo_hierarchy_sequence: set) -> dict:
        geo_hierarchy_map: dict = {}
        return geo_hierarchy_map
        
    def _find_files(self, directory_path: str) -> list:
        file_names: list = os.listdir(directory_path)
        return file_names
    

