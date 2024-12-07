# Example Usage

from consistent_hasher import ConsistentHashing

if __name__ == "__main__":
    hasher = ConsistentHashing(num_replicas=5)
    
    # Add nodes
    hasher.add_node("Server1")
    hasher.add_node("Server2")
    hasher.add_node("Server3")
    hasher.add_node("Server4")
    hasher.add_node("Server5")

    # Get nodes for keys
    print(f"Key 'server 1' maps to: {hasher.get_node('Server1')}")
    print(f"Key 'server 2' maps to: {hasher.get_node('Server2')}")
    print(f"Key 'server 3' maps to: {hasher.get_node('Server3')}")
    print(f"Key 'server 4' maps to: {hasher.get_node('Server4')}")
    print(f"Key 'server 5' maps to: {hasher.get_node('Server5')}")

    # Remove a node and recheck mappings
    hasher.remove_node("Server3")
    
    print("\nAfter removing Server3:")
    print(f"Key 'Server1' maps to: {hasher.get_node('Server1')}")
    print(f"Key 'Server2' maps to: {hasher.get_node('Server2')}")
    print(f"Key 'Server4' maps to: {hasher.get_node('Server4')}")
    print(f"Key 'Server5' maps to: {hasher.get_node('Server5')}")