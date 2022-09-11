import json
from abc import ABC, abstractmethod


class IDataQuery(ABC):
    """
    This abstract class is the template which holds the standard operational 
    structure for collecting, stocking and arranging all geo location data 
    from the json files and serving different basic query requests. 
    Design and Development: Md. Ariful Islam || fahim.arif0373@outlook.com
    """
        
    @abstractmethod
    def collect_all_json_data(self, file_path: str) -> dict:
        """
        Collects all the data from the different chunks of json files
        and arrange those according to their hierarchy and relationship.
        Then return the whole data set as Py Dictionary.
        """