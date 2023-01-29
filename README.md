# cloud-a-thon
cloud-a-thon hosts utility scripts to connect and query cloud resources and cloud deployment templates.

## Project Config
`cloud-a-thon.json` file is the master config file of the project. After checking out this repository, update the master config file as needed.

## get_instance_metadata
`get_instance_metadata.py` Python script can be used to retrieve VM instance metadata of a public cloud platforms like,
  - Google Cloud Platform
  - Amazon Web Services
  - Azure Cloud Platform

In the first cut, the script supports querying metadata of a GCP VM instance only but it can be easily extended to support other cloud platforms. Script uses Google REST APIs and Google Client libraries to fetch the metadata. Script prints the output on the console in a JSON format.

### Script Usage

```bash
python get_instance_metadata.py <instance_name> [metadata_key]`

# Example - Fetch all metadata
python get_instance_metadata.py instance-1

# Example - Fetch specific metadata key. For ex. 'zone'
python get_instance_metadata.py instance-1 zone
```
