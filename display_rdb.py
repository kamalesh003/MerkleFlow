import sys
from rdbtools import RdbParser, MemoryCallback

# Custom Stream class to handle the next_record method
class CustomStream:
    def __init__(self, stream=sys.stdout):
        self.stream = stream

    def next_record(self, record):
        # Redirects each record to stdout or any specified stream
        self.stream.write(str(record) + "\n")

    def write(self, data):
        # Ensures compatibility with standard write calls
        self.stream.write(data)

    def flush(self):
        # Ensures data is flushed to the stream
        self.stream.flush()

# Function to read and display the RDB file
def display_rdb(file_path):
    # Redirect the output to the custom stream
    callback = MemoryCallback(CustomStream(), architecture=64)  # Adjust architecture if needed

    # Initialize the RDB parser
    parser = RdbParser(callback)

    # Parse the RDB file by passing the file path
    parser.parse(file_path)

if __name__ == "__main__":
    # Get the file path from the command line arguments
    if len(sys.argv) != 2:
        print("Usage: python display_rdb.py <path_to_rdb_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Call the display function
    display_rdb(file_path)
