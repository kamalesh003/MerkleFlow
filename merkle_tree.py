import logging
import hashlib
import json
class MerkleTree:
    def __init__(self, name, storage_manager):
        self.name = name
        self.storage_manager = storage_manager
        self.tree = []
        self.root_hash = None
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def build_tree(self, files):
        """Build Merkle tree from file hashes."""
        self.tree = [self.calculate_hash(file) for file in files]
        self.logger.info(f"Building Merkle tree with {len(self.tree)} leaf nodes.")
        while len(self.tree) > 1:
            self.tree = [self.calculate_hash(self.tree[i] + self.tree[i+1] if i+1 < len(self.tree) else self.tree[i])
                         for i in range(0, len(self.tree), 2)]
        self.root_hash = self.tree[0] if self.tree else None
        self.logger.info(f"Merkle tree root hash: {self.root_hash}")

    def calculate_hash(self, data):
        """Generate SHA-256 hash of the data."""
        # Ensure data is in bytes for hashing
        if isinstance(data, str):
            data = data.encode('utf-8')  # Only encode if it's a string
        elif not isinstance(data, bytes):
            raise ValueError("Data must be a string or bytes object.")
        
        return hashlib.sha256(data).hexdigest()

    def update_tree(self):
        """Rebuild the Merkle tree after changes."""
        files = self.storage_manager.get_all_files()
        self.build_tree(files)

    def verify_file(self, file_metadata):
        """Verify if a file exists in the tree and matches the root hash."""
        file_hash = self.calculate_hash(file_metadata)
        return file_hash in self.tree

    def get_root_hash(self):
        """Return the root hash of the Merkle tree."""
        return self.root_hash

    def get_tree_structure(self):
        """Return the structure of the Merkle tree (root hash and tree list)."""
        return {
            'root_hash': self.root_hash,
            'tree': self.tree
        }

    def print_tree(self):
        """Print the Merkle tree details."""
        print(f"{self.name} Merkle Tree:")
        print(f"Root Hash: {self.root_hash}")
        print(f"Tree Structure: {json.dumps(self.tree, indent=4)}")
