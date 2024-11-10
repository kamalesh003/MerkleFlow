C:\Users\Dell\Downloads\New folder (2)\RedisMerkleTreeProject>python main.py
Adding file to Layer 1: sample_file_metadata
DEBUG:layer1_manager:Attempting to add file: sample_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File added to Layer 1 with hash ce75bfdfe61a4ef60d95ccb5b6783a425cbd712772d4c71fda7b1f678f1dafcd
INFO:lru_cache:File with hash sample_file_metadata added to LRU cache.
INFO:lru_cache:File with hash sample_file_metadata retrieved from LRU cache.
File sample_file_metadata found in cache.
Updating file in Layer 1: updated_file_metadata
DEBUG:layer1_manager:Updating file: old=sample_file_metadata (type: <class 'str'>), new=updated_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:Checking existence of file: sample_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:File found in cache with hash ce75bfdfe61a4ef60d95ccb5b6783a425cbd712772d4c71fda7b1f678f1dafcd
DEBUG:layer1_manager:Attempting to remove file: sample_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File removed from Layer 1 with hash ce75bfdfe61a4ef60d95ccb5b6783a425cbd712772d4c71fda7b1f678f1dafcd
DEBUG:layer1_manager:Attempting to add file: updated_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File added to Layer 1 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
INFO:layer1_manager:File updated in Layer 1: sample_file_metadata -> updated_file_metadata
INFO:lru_cache:File with hash updated_file_metadata added to LRU cache.
INFO:lru_cache:File with hash updated_file_metadata retrieved from LRU cache.
Updated file updated_file_metadata found in cache.
Moving file to Layer 2: updated_file_metadata
DEBUG:layer1_manager:Checking existence of file: updated_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:File found in cache with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
DEBUG:layer1_manager:Checking existence of file: updated_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:File found in cache with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
DEBUG:layer1_manager:Attempting to remove file: updated_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File removed from Layer 1 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata removed from Layer 1.
INFO:layer2_manager:File added to Layer 2 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata added to Layer 2.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 1', 'to_layer': 'Layer 2', 'timestamp': '2024-11-10T18:45:44.689405'}
INFO:merkle_tree:Building Merkle tree with 0 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: None
INFO:merkle_tree:Building Merkle tree with 1 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: 3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893
Merkle trees updated for Layer 1 and Layer 2.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 1', 'to_layer': 'Layer 2', 'timestamp': '2024-11-10T18:45:44.720599'}
Moving file back to Layer 1: updated_file_metadata
INFO:layer2_manager:File removed from Layer 2 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata removed from Layer 2.
DEBUG:layer1_manager:Attempting to add file: updated_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File added to Layer 1 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata added to Layer 1.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 2', 'to_layer': 'Layer 1', 'timestamp': '2024-11-10T18:45:44.751841'}
INFO:merkle_tree:Building Merkle tree with 1 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: 3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893
INFO:merkle_tree:Building Merkle tree with 0 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: None
Merkle trees updated for Layer 1 and Layer 2.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 2', 'to_layer': 'Layer 1', 'timestamp': '2024-11-10T18:45:44.767461'}

Merkle Tree Layer 1:
Layer 1 Merkle Tree:
Root Hash: 3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893
Tree Structure: [
    "3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893"
]

Merkle Tree Layer 2:
Layer 2 Merkle Tree:
Root Hash: None
Tree Structure: []

Transition Log:
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:08:59.436802"
}
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:08:59.436802"
}
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:08:59.468011"
}
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:08:59.483631"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.796950"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.796950"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.828190"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.843810"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.937538"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.937538"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.968782"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.984409"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.192067"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.192067"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.224730"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.240396"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.365342"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.380949"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.412192"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.427814"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.042365"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.057985"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.089228"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.104849"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.214199"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.229819"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.245450"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.261062"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:09.959713"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:09.975329"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:09.990988"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:10.006578"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:10.147165"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:10.162795"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:10.178409"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:10.194027"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:44.689405"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:44.720599"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:44.751841"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:44.767461"
}
Current cache content: LRUCache([('sample_file_metadata', 'sample_file_metadata'), ('updated_file_metadata', 'updated_file_metadata')], maxsize=100, currsize=2)
Adding file to Layer 1: sample_file_metadata
DEBUG:layer1_manager:Attempting to add file: sample_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File added to Layer 1 with hash ce75bfdfe61a4ef60d95ccb5b6783a425cbd712772d4c71fda7b1f678f1dafcd
INFO:lru_cache:File with hash sample_file_metadata added to LRU cache.
INFO:lru_cache:File with hash sample_file_metadata retrieved from LRU cache.
File sample_file_metadata found in cache.
Updating file in Layer 1: updated_file_metadata
DEBUG:layer1_manager:Updating file: old=sample_file_metadata (type: <class 'str'>), new=updated_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:Checking existence of file: sample_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:File found in cache with hash ce75bfdfe61a4ef60d95ccb5b6783a425cbd712772d4c71fda7b1f678f1dafcd
DEBUG:layer1_manager:Attempting to remove file: sample_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File removed from Layer 1 with hash ce75bfdfe61a4ef60d95ccb5b6783a425cbd712772d4c71fda7b1f678f1dafcd
DEBUG:layer1_manager:Attempting to add file: updated_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File added to Layer 1 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
INFO:layer1_manager:File updated in Layer 1: sample_file_metadata -> updated_file_metadata
INFO:lru_cache:File with hash updated_file_metadata added to LRU cache.
INFO:lru_cache:File with hash updated_file_metadata retrieved from LRU cache.
Updated file updated_file_metadata found in cache.
Moving file to Layer 2: updated_file_metadata
DEBUG:layer1_manager:Checking existence of file: updated_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:File found in cache with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
DEBUG:layer1_manager:Checking existence of file: updated_file_metadata (type: <class 'str'>)
DEBUG:layer1_manager:File found in cache with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
DEBUG:layer1_manager:Attempting to remove file: updated_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File removed from Layer 1 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata removed from Layer 1.
INFO:layer2_manager:File added to Layer 2 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata added to Layer 2.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 1', 'to_layer': 'Layer 2', 'timestamp': '2024-11-10T18:45:45.048647'}
INFO:merkle_tree:Building Merkle tree with 0 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: None
INFO:merkle_tree:Building Merkle tree with 1 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: 3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893
Merkle trees updated for Layer 1 and Layer 2.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 1', 'to_layer': 'Layer 2', 'timestamp': '2024-11-10T18:45:45.048647'}
Moving file back to Layer 1: updated_file_metadata
INFO:layer2_manager:File removed from Layer 2 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata removed from Layer 2.
DEBUG:layer1_manager:Attempting to add file: updated_file_metadata (type: <class 'str'>)
INFO:layer1_manager:File added to Layer 1 with hash d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa
File updated_file_metadata added to Layer 1.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 2', 'to_layer': 'Layer 1', 'timestamp': '2024-11-10T18:45:45.111135'}
INFO:merkle_tree:Building Merkle tree with 1 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: 3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893
INFO:merkle_tree:Building Merkle tree with 0 leaf nodes.
INFO:merkle_tree:Merkle tree root hash: None
Merkle trees updated for Layer 1 and Layer 2.
INFO:transition_manager:Transition recorded: {'file_hash': 'd12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa', 'file_metadata': 'updated_file_metadata', 'from_layer': 'Layer 2', 'to_layer': 'Layer 1', 'timestamp': '2024-11-10T18:45:45.126753'}

Merkle Tree Layer 1:
Layer 1 Merkle Tree:
Root Hash: 3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893
Tree Structure: [
    "3b6e58b40908e56f437ca317209f70a3db2e8f75af2a209a41181cdeaf5cd893"
]

Merkle Tree Layer 2:
Layer 2 Merkle Tree:
Root Hash: None
Tree Structure: []

Transition Log:
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:08:59.436802"
}
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:08:59.436802"
}
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:08:59.468011"
}
{
    "file_hash": "b4ca76a5440bfe108d137e86c48f16352eaba1d67d45064d3250aca61035a805",
    "file_metadata": "retail_future",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:08:59.483631"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.796950"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.796950"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.828190"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.843810"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.937538"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T17:26:01.937538"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.968782"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T17:26:01.984409"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.192067"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.192067"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.224730"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.240396"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.365342"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:03:21.380949"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.412192"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:03:21.427814"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.042365"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.057985"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.089228"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.104849"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.214199"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:08:43.229819"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.245450"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:08:43.261062"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:09.959713"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:09.975329"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:09.990988"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:10.006578"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:10.147165"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:10.162795"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:10.178409"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:10.194027"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:44.689405"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:44.720599"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:44.751841"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:44.767461"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:45.048647"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 1",
    "to_layer": "Layer 2",
    "timestamp": "2024-11-10T18:45:45.048647"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:45.111135"
}
{
    "file_hash": "d12ed4aacc2b6db991e868ca5c34ee457e70b68d9d361d189d33b877f467bdaa",
    "file_metadata": "updated_file_metadata",
    "from_layer": "Layer 2",
    "to_layer": "Layer 1",
    "timestamp": "2024-11-10T18:45:45.126753"
}
Current cache content: LRUCache([('sample_file_metadata', 'sample_file_metadata'), ('updated_file_metadata', 'updated_file_metadata')], maxsize=100, currsize=2)

C:\Users\Dell\Downloads\New folder (2)\RedisMerkleTreeProject>
