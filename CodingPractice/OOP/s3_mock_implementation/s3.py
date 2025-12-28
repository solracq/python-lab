from abc import ABC, abstractmethod

class S3:
    def description(self):
        return "S3 implementation"

    @abstractmethod
    def setup(self):
        pass

    @property
    @abstractmethod
    def storage_type(self):
        pass

    @abstractmethod
    def bucket_creation(self, bucket_name: str):
        pass

    @abstractmethod
    def object_creaton(self, bucket_name: str, object_name: str):
        pass

    @abstractmethod
    def list_buckets(self):
        pass

    @abstractmethod
    def list_objects(self):
        pass

    @abstractmethod
    def read_object(self, bucket_name: str, object_name: str):
        pass

    @abstractmethod
    def write_object(self, bucket_name: str, object_name: str):
        pass

