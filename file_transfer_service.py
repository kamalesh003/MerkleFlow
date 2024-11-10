class FileTransferService:
    def __init__(self, layer1_manager, layer2_manager, merkle_tree_layer1, merkle_tree_layer2, transition_manager):
        """Initialize the FileTransferService with the provided managers and transition manager."""
        self.layer1_manager = layer1_manager
        self.layer2_manager = layer2_manager
        self.merkle_tree_layer1 = merkle_tree_layer1
        self.merkle_tree_layer2 = merkle_tree_layer2
        self.transition_manager = transition_manager  # Added transition_manager

    def move_file(self, file_metadata, from_layer, to_layer):
        """General method to move a file between layers and record the transition."""
        if from_layer == 'Layer 1' and not self.layer1_manager.file_exists(file_metadata):
            print(f"File {file_metadata} not found in Layer 1.")
            return
        if from_layer == 'Layer 2' and not self.layer2_manager.file_exists(file_metadata):
            print(f"File {file_metadata} not found in Layer 2.")
            return

        # Remove file from the source layer
        if from_layer == 'Layer 1':
            self.layer1_manager.remove_file(file_metadata)
            print(f"File {file_metadata} removed from Layer 1.")
        elif from_layer == 'Layer 2':
            self.layer2_manager.remove_file(file_metadata)
            print(f"File {file_metadata} removed from Layer 2.")
        
        # Add file to the destination layer
        if to_layer == 'Layer 1':
            self.layer1_manager.add_file(file_metadata)
            print(f"File {file_metadata} added to Layer 1.")
        elif to_layer == 'Layer 2':
            self.layer2_manager.add_file(file_metadata)
            print(f"File {file_metadata} added to Layer 2.")

        # Record the transition using the TransitionManager
        self.transition_manager.store_transition(file_metadata, from_layer, to_layer)

        # Rebuild Merkle Trees for both layers
        self.update_merkle_trees()

    def move_file_to_layer2(self, file_metadata):
        """Move a file from Layer 1 (Redis) to Layer 2 (File System)."""
        self.move_file(file_metadata, from_layer='Layer 1', to_layer='Layer 2')

    def move_file_to_layer1(self, file_metadata):
        """Move a file from Layer 2 (File System) to Layer 1 (Redis)."""
        self.move_file(file_metadata, from_layer='Layer 2', to_layer='Layer 1')

    def update_merkle_trees(self):
        """Update Merkle Trees for both layers."""
        try:
            self.merkle_tree_layer1.update_tree()
            self.merkle_tree_layer2.update_tree()
            print("Merkle trees updated for Layer 1 and Layer 2.")
        except Exception as e:
            print(f"Error updating Merkle trees: {e}")
