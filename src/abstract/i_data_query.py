from abc import ABC, abstractmethod


class IDataQuery(ABC):
    """
    This abstract class is the template which holds the standard operational 
    structure for collecting, stocking and arranging all geo location data 
    from the json files and serving different basic query requests. 
    Design and Development: Md. Ariful Islam || fahim.arif0373@outlook.com
    """

    @abstractmethod
    def get_geojson(self, data_directory_path: str, file_name: str) -> dict:
        """
        This method takes directory file location and file name as parameter then 
        finds and read the file data and return the Geo-JSON data.
        """

    @abstractmethod
    def collect_all_json_data(self, directory_path: str, geo_hierarchy_sequence: set) -> dict:
        """
        Collects all the data from the different chunks of json files
        and arrange those according to their hierarchy and relationship.
        Then return the whole data set as Py Dictionary.
        """

    @abstractmethod
    def geo_hierarchy_manager(self, directory_path: str, file_names: list, geo_hierarchy_sequence: set) -> dict:
        """
        This method will take folder location (absulate path) as String and Targeted 
        file names (JSON file) as List and geographical hierarchy sequence and Py Set. 
        Arrange those data according to their Geographical
        Hierarchy and return the data set as Py Dictionary.
        """

    @abstractmethod
    def _find_files(self, directory_path: str) -> list:
        """
        This method is responsible for finding all the file names of a
        specific directory and return those file names as a list format.
        """
