import logging
import json
import requests
import subprocess
from google.cloud import compute_v1


class InstanceMetadata:
    """
    InstanceMetadata packages functions to manage and query metadata of the GCP Virtual Machines
    """

    def __init__(self, project, zone, instance):
        """
        Initialize Project, Zone and Name of the GCP instance
        :param project: Project Id
        :param zone: Zone
        :param instance: Instance Name
        """
        self.project = project
        self.zone = zone
        self.instance = instance
        self.instance_client = compute_v1.InstancesClient()
        self.endpoint = "https://compute.googleapis.com/compute/v1/projects/{}/zones/{}/instances/{}"\
            .format(self.project, self.zone, self.instance)
        self.__auth_token__ = self.generate_auth_token()

    def generate_auth_token(self):
        """
        Generate API Access Token for REST API calls
        :return: Access token
        """
        p = subprocess.run("gcloud auth print-access-token", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.stdout.decode('utf-8').strip()

    def get_all_instance_metadata(self):
        """
        Retrieve all metadata for the GCP instance using Google Cloud Compute client library
        :return: Dict of instance metadata
        """
        try:
            logging.info("Retrieving metadata for instance - {} of project - {} in zone - {}"
                         .format(self.instance, self.project, self.zone))

            data = self.instance_client.get(project=self.project,
                                            zone=self.zone,
                                            instance=self.instance)

            return data if data else None
        except Exception as e:
            logging.error("Exception Occurred - {}".format(str(e)))

    def get_instance_metadata_key(self, key):
        """
        Retrieve a specific metadata key for the GCP instance using Google Cloud Compute client library
        :return: Dict containing Metadata param
        """
        try:
            data = self.get_all_instance_metadata()
            return data[key] if data and key in data.keys() else ""

        except Exception as e:
            logging.error("Exception Occurred - {}".format(str(e)))

    def request_all_instance_metadata(self):
        """
        Retrieve all metadata for the GCP instance using Google Cloud Compute REST APIs
        :return: Dict of instance metadata
        """
        try:
            logging.info("Retrieving metadata for instance - {} of project - {} in zone - {}"
                         .format(self.instance, self.project, self.zone))

            headers = {'Metadata-Flavor': 'Google',
                       'Authorization': 'Bearer {}'.format(self.__auth_token__),
                       'Content-Type': 'application/json; charset=utf-8'}
            response = requests.get(url=self.endpoint, headers=headers)

            if response.status_code == 200:
                return json.loads(response.text)
            else:
                logging.error("Failed to retrieve instance metadata. Response:: code - {}, message"
                              .format(response.status_code, response.text))
                return None

        except Exception as e:
            logging.error("Exception Occurred - {}".format(str(e)))

    def request_instance_metadata_key(self, key):
        """
        Retrieve all metadata for the GCP instance using Google Cloud Compute REST APIs
        :return: Dict of instance metadata
        """
        try:
            data = self.request_all_instance_metadata()
            if key in data.keys():
                return {key: data[key]}
            else:
                logging.error("Key '{}' not found in the instance metadata!".format(key))

        except Exception as e:
            logging.error("Exception Occurred - {}".format(str(e)))
