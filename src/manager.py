from .constants import Constants
from .data_query import DataQuery


class Manager:
    
    def menu(self):
        abs_directory_path = Constants.APP_DATA_DIRECTORY
        geo_hierarchy_sequence = Constants.GEO_HIERARCHY
        obj = DataQuery()
        obj.collect_all_json_data(abs_directory_path, geo_hierarchy_sequence)