import os
import hashlib
import logging

class Layer2Manager:
    def __init__(self, layer2_directory='layer2_files'):
        """Initialize Layer 2 Manager."""
        self.layer2_directory = layer2_directory
        # Ensure the directory exists
        os.makedirs(self.layer2_directory, exist_ok=True)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def add_file(self, file_metadata):
        """Store file metadata in Layer 2 directory, using hash as filename."""
        try:
            file_hash = self.calculate_hash(file_metadata)
            file_path = os.path.join(self.layer2_directory, file_hash)

            # Write metadata to the file
            with open(file_path, 'w') as f:
                f.write(file_metadata)
            
            self.logger.info(f"File added to Layer 2 with hash {file_hash}")
            return file_hash
        except Exception as e:
            self.logger.error(f"Failed to add file: {e}")
            raise

    def remove_file(self, file_metadata):
        """Remove file from Layer 2 directory using metadata hash."""
        try:
            file_hash = self.calculate_hash(file_metadata)
            file_path = os.path.join(self.layer2_directory, file_hash)

            # Check if file exists and remove it
            if os.path.exists(file_path):
                os.remove(file_path)
                self.logger.info(f"File removed from Layer 2 with hash {file_hash}")
            else:
                self.logger.error(f"File not found in Layer 2 with hash {file_hash}")
        except Exception as e:
            self.logger.error(f"Failed to remove file: {e}")
            raise

    def file_exists(self, file_metadata):
        """Check if a file exists in Layer 2 by hash."""
        try:
            file_hash = self.calculate_hash(file_metadata)
            file_path = os.path.join(self.layer2_directory, file_hash)
            return os.path.exists(file_path)
        except Exception as e:
            self.logger.error(f"Error checking file existence: {e}")
            raise

    @staticmethod
    def calculate_hash(data):
        """Generate SHA-256 hash of the data (used for unique file identification)."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def get_all_files(self):
        """Return all files in Layer 2 directory."""
        try:
            return os.listdir(self.layer2_directory)
        except Exception as e:
            self.logger.error(f"Failed to retrieve files from Layer 2: {e}")
            raise
