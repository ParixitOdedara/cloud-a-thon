import json


class Utilities:
    """
    Common library functions for cloud-a-thon project
    """
    def __init__(self, project_config):
        self.config_file = project_config

    def load_project_config(self):
        """
        Load Project JSON Config file and return it as dictionary
        :return: Project config dictionary
        """
        with open(self.config_file, 'r') as f:
            conf_data = json.load(f)
        return conf_data
