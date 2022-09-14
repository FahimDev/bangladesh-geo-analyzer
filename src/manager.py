from .constants import Constants
from .data_query import DataQuery
from .map_marker import MapMarker


class Manager:
    
    def menu(self):
        abs_directory_path = Constants.APP_DATA_DIRECTORY
        geo_hierarchy_sequence = Constants.GEO_HIERARCHY
        obj_map = MapMarker()
        obj = DataQuery()
        geojson_data = obj.get_geojson(abs_directory_path, "bangladesh.geojson")
        payload: dict = {
            'name': 'Bangladesh',
            'latitude': 23.6850,
            'longitude': 90.3563
        }
        obj_map.create_map(geojson_data, payload)
        print("Done")
        #obj.collect_all_json_data(abs_directory_path, geo_hierarchy_sequence)