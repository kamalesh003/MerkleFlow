import os
import hashlib
from datetime import datetime
import json
import logging

class TransitionManager:
    def __init__(self, log_file='layer_transition_log.json'):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

        # Ensure the directory for the log file exists
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Initialize log file if not exists
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)
            self.logger.info(f"Log file {self.log_file} created.")

    def store_transition(self, file_metadata, from_layer, to_layer):
        """Store a transition from one layer to another with relevant metadata."""
        file_hash = self.calculate_hash(file_metadata)
        timestamp = datetime.now().isoformat()

        transition_data = {
            'file_hash': file_hash,
            'file_metadata': file_metadata,
            'from_layer': from_layer,
            'to_layer': to_layer,
            'timestamp': timestamp
        }

        self._append_to_log(transition_data)

    def _append_to_log(self, transition_data):
        """Append transition data to the log file."""
        try:
            # Open log file and read existing data
            with open(self.log_file, 'r') as f:
                logs = json.load(f)

            # Append the new transition data
            logs.append(transition_data)

            # Write back the updated log data
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=4)
            
            self.logger.info(f"Transition recorded: {transition_data}")
        except Exception as e:
            self.logger.error(f"Failed to log transition: {e}")

    @staticmethod
    def calculate_hash(data):
        """Generate SHA-256 hash for the given data."""
        if isinstance(data, str):
            data = data.encode('utf-8')  # Convert string to bytes
        elif not isinstance(data, bytes):
            raise TypeError("Input must be a string or bytes")
    
        return hashlib.sha256(data).hexdigest()

    def get_all_transitions(self):
        """Return all recorded transitions."""
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to read transitions: {e}")
            return []

    def print_all_transitions(self):
        """Print all recorded transitions."""
        transitions = self.get_all_transitions()
        for transition in transitions:
            print(json.dumps(transition, indent=4))
