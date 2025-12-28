from CodingPractice.OOP.s3_mock_implementation.s3 import S3
from CodingPractice.OOP.s3_mock_implementation import variables


class Client(S3):
    S3_TYPE = "Client"

    def __init__(self):
        self.access_key_id = variables.AWS_ACCESS_KEY_ID
        self.secret_access_key = variables.AWS_SECRET_ACCESS_KEY

    def setup(self):
        return f"Setting up with {self.access_key_id} and {self.secret_access_key}"

    @property
    def storage_type(self):
        return f"This is an S3 implementation of type {Client.S3_TYPE}"

    def bucket_creation(self, bucket_name: str):
        return f"Create {bucket_name} bucket"

    def object_creation(self, bucket_name: str, object_name: str):
        return f"Create object {object_name} in {bucket_name} bucket"

    def list_objects(self):
        return "list of objs"

    def list_buckets(self):
        return "list of buckets"

    def read_object(self, bucket_name: str, object_name: str):
        return f"Reading object {object_name} in {bucket_name} bucket"
