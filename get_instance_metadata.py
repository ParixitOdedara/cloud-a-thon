import logging
import sys
import os
import json
from gcp.instance_metadata import InstanceMetadata
from common.utilities import Utilities

logging.basicConfig(level=logging.INFO)


def get_metadata(instance_name, metadata_key=""):
    """
    Initialize the InstanceMetadata class and fetch GCP instance metadata using GCP REST API.
    Pass metadata key to fetch a specific key of the instance metadata. If not passed, all metadata attributes will be
    fetched and returned.

    :param instance_name: Instance Name
    :param metadata_key: Metadata Key
    :return: Metadata in JSON format
    """
    try:
        project_conf_f = os.path.join(os.path.dirname(sys.argv[0]), 'cloud-a-thon.json')
        utils = Utilities(project_config=project_conf_f)
        conf = utils.load_project_config()

        inst_m = InstanceMetadata(project=conf['gcp']['project_id'],
                                  zone=conf['gcp']['zone'],
                                  instance=instance_name)

        if metadata_key:
            metadata = inst_m.request_instance_metadata_key(metadata_key)
        else:
            metadata = inst_m.request_all_instance_metadata()

        return metadata

    except Exception as e:
        logging.error("Exception Occurred - {}".format(str(e)))


if __name__ == "__main__":
    """
    get-instance-metadata is used to query VM metadata of an instance running on public clouds like GCP, AWS or Azure.
    """

    logging.info("Script started.")

    if len(sys.argv) not in [2, 3]:
        logging.error("Invalid script usage! >> python {} <mandatory: intance_name> <optional: metadata_key>")

    inst_nm = sys.argv[1] if len(sys.argv) >= 2 else ""
    meta_key = sys.argv[2] if len(sys.argv) == 3 else ""

    meta = get_metadata(inst_nm, meta_key)
    logging.info(100*"*")
    logging.info("\n {}".format(json.dumps(meta, indent=4)))
    logging.info(100*"*")

    logging.info("Script Completed! Exiting!")
