from cachetools import LRUCache
import logging

class LRUFileCache:
    def __init__(self, max_size=1000):
        """
        Initializes the LRU cache with the specified max size and sets up logging.

        :param max_size: The maximum number of items the cache can hold.
        """
        self.cache = LRUCache(maxsize=max_size)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def add(self, file_hash, file_metadata):
        """
        Add a file's metadata to the cache.

        :param file_hash: The unique identifier (hash) for the file.
        :param file_metadata: The metadata associated with the file.
        """
        self.cache[file_hash] = file_metadata
        self.logger.info(f"File with hash {file_hash} added to LRU cache.")

    def get(self, file_hash):
        """
        Get file metadata from the cache.

        :param file_hash: The hash of the file whose metadata is to be fetched.
        :return: File metadata if found, None otherwise.
        """
        file_metadata = self.cache.get(file_hash)
        if file_metadata:
            self.logger.info(f"File with hash {file_hash} retrieved from LRU cache.")
        else:
            self.logger.warning(f"File with hash {file_hash} not found in LRU cache.")
        return file_metadata

    def remove(self, file_hash):
        """
        Remove file metadata from the cache.

        :param file_hash: The hash of the file to be removed.
        """
        if file_hash in self.cache:
            del self.cache[file_hash]
            self.logger.info(f"File with hash {file_hash} removed from LRU cache.")
        else:
            self.logger.warning(f"File with hash {file_hash} not found in LRU cache.")

    def clear(self):
        """Clears the entire cache."""
        self.cache.clear()
        self.logger.info("LRU cache cleared.")

    def cache_size(self):
        """Returns the current size of the cache."""
        return len(self.cache)

    def is_cache_full(self):
        """Returns whether the cache has reached its maximum size."""
        return len(self.cache) == self.cache.maxsize

    def to_serializable(self):
        """Convert the cache into a JSON serializable format."""
        return list(self.cache.items()) 
