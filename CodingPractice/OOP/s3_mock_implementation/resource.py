from CodingPractice.OOP.s3_mock_implementation.s3 import S3
from CodingPractice.OOP.s3_mock_implementation import variables


class Resource(S3):
    S3_TYPE = "Resource"

    def __init__(self):
        self.access_key_id = variables.AWS_ACCESS_KEY_ID
        self.secret_access_key = variables.AWS_SECRET_ACCESS_KEY

    def setup(self):
        return f"Setting up AWS S3 instance with {self.access_key_id} and with " \
               f"{self.secret_access_key}"

    @property
    def storage_type(self):
        return f"Using S3 storage type {Resource.S3_TYPE}"

    def bucket_creation(self, bucket_name: str):
        return f"creating bucket {bucket_name} of {Resource.S3_TYPE}"

    def object_creaton(self, bucket_name: str, object_name: str):
        return f"creating object {bucket_name} and {object_name} of {Resource.S3_TYPE}"

    def list_buckets(self):
        return f"listing bucket of {Resource.S3_TYPE}"

    def list_objects(self):
        return f"listing obj of {Resource.S3_TYPE}"

    def read_object(self, bucket_name: str, object_name: str):
        return f"Reading {bucket_name} bucket and {object_name} object"

    def write_object(self, bucket_name: str, object_name: str):
        return f"Writing {bucket_name} bucket and {object_name} object"



