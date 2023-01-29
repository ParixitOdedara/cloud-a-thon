import json
import logging


class Utilities:
    """
    Common library functions for cloud-a-thon project
    """
    def __init__(self, project_config=""):
        self.config_file = project_config

    def load_project_config(self):
        """
        Load Project JSON Config file and return it as dictionary
        :return: Project config dictionary
        """
        with open(self.config_file, 'r') as f:
            conf_data = json.load(f)
        return conf_data

    def fetch_value_from_nested_obj(self, obj, key):
        """
        Fetch value of the input key in the nested object
        :param obj: Input JSON / Dict
        :param key: Key to be searched
        :return: Value for the input key
        """
        keys_list = key.split('/')
        for key in keys_list:
            logging.debug("key - {}, obj - {}".format(key, obj))
            obj = obj[key] if type(obj) == dict and key in obj.keys() else ""

        logging.debug("Extracted value - {}".format(obj))
        return obj
