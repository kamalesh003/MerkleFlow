import redis
import hashlib
import logging
from cachetools import LRUCache

class Layer1Manager:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0, cache_size=1000):
        """Initialize the Layer1Manager with Redis client and in-memory cache."""
        self.client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
        self.layer1_key = 'layer1_hashes'
        self.cache = LRUCache(maxsize=cache_size)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)  # Set logging to DEBUG for more detailed logs

    def add_file(self, file_metadata):
        """Add a file's hash to Layer 1 Redis and cache it."""
        # Debugging the file type
        self.logger.debug(f"Attempting to add file: {file_metadata} (type: {type(file_metadata)})")

        # Ensure that file_metadata is in the correct format
        if isinstance(file_metadata, bytes):
            file_metadata = file_metadata.decode('utf-8')  # Decode bytes to string
        elif not isinstance(file_metadata, str):
            raise ValueError(f"Unsupported file_metadata type: {type(file_metadata)}")

        file_hash = self.calculate_hash(file_metadata)

        try:
            # Store in Redis
            self.client.sadd(self.layer1_key, file_hash)
            # Store in Cache
            self.cache[file_hash] = file_metadata
            self.logger.info(f"File added to Layer 1 with hash {file_hash}")
        except redis.RedisError as e:
            self.logger.error(f"Failed to add file to Redis: {e}")
            raise Exception(f"Failed to add file to Redis: {e}")  # Custom exception for better clarity
        return file_hash

    def remove_file(self, file_metadata):
        """Remove a file's hash from Layer 1 Redis and cache."""
        # Debugging the file type
        self.logger.debug(f"Attempting to remove file: {file_metadata} (type: {type(file_metadata)})")

        # Ensure file_metadata is in the correct format
        if isinstance(file_metadata, bytes):
            file_metadata = file_metadata.decode('utf-8')  # Decode bytes to string
        elif not isinstance(file_metadata, str):
            raise ValueError(f"Unsupported file_metadata type: {type(file_metadata)}")

        file_hash = self.calculate_hash(file_metadata)

        try:
            # Remove from Redis
            self.client.srem(self.layer1_key, file_hash)
            # Remove from Cache
            if file_hash in self.cache:
                del self.cache[file_hash]
            self.logger.info(f"File removed from Layer 1 with hash {file_hash}")
        except redis.RedisError as e:
            self.logger.error(f"Failed to remove file from Redis: {e}")
            raise Exception(f"Failed to remove file from Redis: {e}")  # Custom exception for better clarity

    def file_exists(self, file_metadata):
        """Check if a file's hash exists in Layer 1 Redis or Cache."""
        # Debugging the file type
        self.logger.debug(f"Checking existence of file: {file_metadata} (type: {type(file_metadata)})")

        # Ensure file_metadata is in the correct format
        if isinstance(file_metadata, bytes):
            file_metadata = file_metadata.decode('utf-8')  # Decode bytes to string
        elif not isinstance(file_metadata, str):
            raise ValueError(f"Unsupported file_metadata type: {type(file_metadata)}")

        file_hash = self.calculate_hash(file_metadata)

        # Check Cache first
        if file_hash in self.cache:
            self.logger.debug(f"File found in cache with hash {file_hash}")
            return True

        # Check Redis if not in Cache
        try:
            exists = self.client.sismember(self.layer1_key, file_hash)
            if exists:
                self.cache[file_hash] = file_metadata  # Cache the file hash for quicker future lookups
            self.logger.debug(f"File exists in Redis: {exists}")
            return exists
        except redis.RedisError as e:
            self.logger.error(f"Failed to check file existence in Redis: {e}")
            raise Exception(f"Failed to check file existence in Redis: {e}")  # Custom exception for better clarity

    def update_file(self, old_metadata, new_metadata):
        """Update an existing file with new metadata."""
        # Debugging the file type
        self.logger.debug(f"Updating file: old={old_metadata} (type: {type(old_metadata)}), new={new_metadata} (type: {type(new_metadata)})")

        # Ensure both old and new metadata are properly decoded if necessary
        if isinstance(old_metadata, bytes):
            old_metadata = old_metadata.decode('utf-8')
        elif not isinstance(old_metadata, str):
            raise ValueError(f"Unsupported old_metadata type: {type(old_metadata)}")

        if isinstance(new_metadata, bytes):
            new_metadata = new_metadata.decode('utf-8')
        elif not isinstance(new_metadata, str):
            raise ValueError(f"Unsupported new_metadata type: {type(new_metadata)}")

        old_file_hash = self.calculate_hash(old_metadata)
        new_file_hash = self.calculate_hash(new_metadata)

        # Check if the old file exists in Redis and Cache
        if self.file_exists(old_metadata):
            # Remove the old file from Redis and Cache
            self.remove_file(old_metadata)
            # Add the new file with updated metadata
            self.add_file(new_metadata)
            self.logger.info(f"File updated in Layer 1: {old_metadata} -> {new_metadata}")
        else:
            self.logger.error(f"File with metadata {old_metadata} not found in Layer 1")

    @staticmethod
    def calculate_hash(data):
        """Generate SHA-256 hash of the data."""
        # Ensure that the data is in bytes
        if isinstance(data, str):
            data = data.encode('utf-8')  # Only encode if it's a string
        elif not isinstance(data, bytes):
            raise ValueError(f"Unsupported data type for hashing: {type(data)}")

        return hashlib.sha256(data).hexdigest()

    def get_all_files(self):
        """Return all files' hashes from Layer 1."""
        try:
            return list(self.client.smembers(self.layer1_key))  # Convert to list for easier handling
        except redis.RedisError as e:
            self.logger.error(f"Failed to retrieve files from Redis: {e}")
            raise Exception(f"Failed to retrieve files from Redis: {e}")  # Custom exception for better clarity
