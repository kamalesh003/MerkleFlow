from layer1_manager import Layer1Manager
from layer2_manager import Layer2Manager
from merkle_tree import MerkleTree
from file_transfer_service import FileTransferService
from transition_manager import TransitionManager  # Assuming transition manager class exists
from lru_cache import LRUFileCache
from layer1_manager import Layer1Manager
from layer2_manager import Layer2Manager
from merkle_tree import MerkleTree
from file_transfer_service import FileTransferService
from transition_manager import TransitionManager  # Assuming transition manager class exists
from lru_cache import LRUFileCache
import json

def main():
    # Setup the managers and trees
    layer1_manager = Layer1Manager()
    layer2_manager = Layer2Manager()
    
    # Setup LRU File Cache (Assuming it's used for caching file metadata)
    lru_cache = LRUFileCache(max_size=100)  # Use max_size instead of cache_size

    # Setup Merkle trees for Layer 1 and Layer 2
    merkle_tree_layer1 = MerkleTree("Layer 1", layer1_manager)
    merkle_tree_layer2 = MerkleTree("Layer 2", layer2_manager)

    # Initialize the TransitionManager to log file movements
    transition_manager = TransitionManager()

    # Setup the file transfer service with all necessary components
    transfer_service = FileTransferService(
        layer1_manager, 
        layer2_manager, 
        merkle_tree_layer1, 
        merkle_tree_layer2, 
        transition_manager
    )

    # Example file metadata
    file_metadata = "sample_file_metadata"
    updated_file_metadata = "updated_file_metadata"  # New metadata for the update

    try:
        # Add file to Layer 1 and cache it
        print(f"Adding file to Layer 1: {file_metadata}")
        file_hash = layer1_manager.add_file(file_metadata)
        lru_cache.add(file_metadata, file_metadata)  # Cache file metadata in Layer 1

        # Check if the file is in cache (for debugging/logging purposes)
        if lru_cache.get(file_metadata):
            print(f"File {file_metadata} found in cache.")
        else:
            print(f"File {file_metadata} not found in cache.")

        # Update and store the file in Layer 1 with updated metadata
        print(f"Updating file in Layer 1: {updated_file_metadata}")
        layer1_manager.update_file(file_metadata, updated_file_metadata)  # Assuming the update method exists
        lru_cache.add(updated_file_metadata, updated_file_metadata)  # Update the cache with new metadata

        # Check if the updated file is in cache (for debugging/logging purposes)
        if lru_cache.get(updated_file_metadata):
            print(f"Updated file {updated_file_metadata} found in cache.")
        else:
            print(f"Updated file {updated_file_metadata} not found in cache.")

        # Move file to Layer 2 and track the transition
        print(f"Moving file to Layer 2: {updated_file_metadata}")
        if layer1_manager.file_exists(updated_file_metadata):  # Ensure the file exists in Layer 1
            transfer_service.move_file_to_layer2(updated_file_metadata)

            # Log the transition
            transition_manager.store_transition(  # Use store_transition instead of log_transition
                updated_file_metadata,  # Metadata of the updated file
                "Layer 1",  # From Layer 1
                "Layer 2"   # To Layer 2
            )
        else:
            print(f"File {updated_file_metadata} not found in Layer 1.")

        # New example: Move the file back from Layer 2 to Layer 1
        print(f"Moving file back to Layer 1: {updated_file_metadata}")
        if layer2_manager.file_exists(updated_file_metadata):  # Ensure the file exists in Layer 2
            transfer_service.move_file_to_layer1(updated_file_metadata)

            # Log the transition back to Layer 1
            transition_manager.store_transition(
                updated_file_metadata,  # Metadata of the updated file
                "Layer 2",  # From Layer 2
                "Layer 1"   # To Layer 1
            )
        else:
            print(f"File {updated_file_metadata} not found in Layer 2.")

        # Print Merkle tree information for both layers
        print("\nMerkle Tree Layer 1:")
        merkle_tree_layer1.print_tree()

        print("\nMerkle Tree Layer 2:")
        merkle_tree_layer2.print_tree()

        # Print transition log (to verify the move)
        print("\nTransition Log:")
        transition_manager.print_all_transitions()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Additional logging can be done here if needed
        layer1_manager.logger.error(f"Error in file management process: {e}")
    print(f"Current cache content: {lru_cache.cache}")



if __name__ == "__main__":
    main()

def main():
    # Setup the managers and trees
    layer1_manager = Layer1Manager()
    layer2_manager = Layer2Manager()
    
    # Setup LRU File Cache (Assuming it's used for caching file metadata)
    lru_cache = LRUFileCache(max_size=100)  # Use max_size instead of cache_size

    # Setup Merkle trees for Layer 1 and Layer 2
    merkle_tree_layer1 = MerkleTree("Layer 1", layer1_manager)
    merkle_tree_layer2 = MerkleTree("Layer 2", layer2_manager)

    # Initialize the TransitionManager to log file movements
    transition_manager = TransitionManager()

    # Setup the file transfer service with all necessary components
    transfer_service = FileTransferService(
        layer1_manager, 
        layer2_manager, 
        merkle_tree_layer1, 
        merkle_tree_layer2, 
        transition_manager
    )

    # Example file metadata
    file_metadata = "sample_file_metadata"
    updated_file_metadata = "updated_file_metadata"  # New metadata for the update

    try:
        # Add file to Layer 1 and cache it
        print(f"Adding file to Layer 1: {file_metadata}")
        file_hash = layer1_manager.add_file(file_metadata)
        lru_cache.add(file_metadata, file_metadata)  # Cache file metadata in Layer 1

        # Check if the file is in cache (for debugging/logging purposes)
        if lru_cache.get(file_metadata):
            print(f"File {file_metadata} found in cache.")
        else:
            print(f"File {file_metadata} not found in cache.")

        # Update and store the file in Layer 1 with updated metadata
        print(f"Updating file in Layer 1: {updated_file_metadata}")
        layer1_manager.update_file(file_metadata, updated_file_metadata)  # Assuming the update method exists
        lru_cache.add(updated_file_metadata, updated_file_metadata)  # Update the cache with new metadata

        # Check if the updated file is in cache (for debugging/logging purposes)
        if lru_cache.get(updated_file_metadata):
            print(f"Updated file {updated_file_metadata} found in cache.")
        else:
            print(f"Updated file {updated_file_metadata} not found in cache.")

        # Move file to Layer 2 and track the transition
        print(f"Moving file to Layer 2: {updated_file_metadata}")
        if layer1_manager.file_exists(updated_file_metadata):  # Ensure the file exists in Layer 1
            transfer_service.move_file_to_layer2(updated_file_metadata)

            # Log the transition
            transition_manager.store_transition(  # Use store_transition instead of log_transition
                updated_file_metadata,  # Metadata of the updated file
                "Layer 1",  # From Layer 1
                "Layer 2"   # To Layer 2
            )
        else:
            print(f"File {updated_file_metadata} not found in Layer 1.")

        # New example: Move the file back from Layer 2 to Layer 1
        print(f"Moving file back to Layer 1: {updated_file_metadata}")
        if layer2_manager.file_exists(updated_file_metadata):  # Ensure the file exists in Layer 2
            transfer_service.move_file_to_layer1(updated_file_metadata)

            # Log the transition back to Layer 1
            transition_manager.store_transition(
                updated_file_metadata,  # Metadata of the updated file
                "Layer 2",  # From Layer 2
                "Layer 1"   # To Layer 1
            )
        else:
            print(f"File {updated_file_metadata} not found in Layer 2.")

        # Print Merkle tree information for both layers
        print("\nMerkle Tree Layer 1:")
        merkle_tree_layer1.print_tree()

        print("\nMerkle Tree Layer 2:")
        merkle_tree_layer2.print_tree()

        # Print transition log (to verify the move)
        print("\nTransition Log:")
        transition_manager.print_all_transitions()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Additional logging can be done here if needed
        layer1_manager.logger.error(f"Error in file management process: {e}")
    print(f"Current cache content: {lru_cache.cache}")



if __name__ == "__main__":
    main()
