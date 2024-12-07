import hashlib
import bisect


class ConsistentHashing:
    def __init__(self, num_replicas=5):
        """
        Initialize consistent hashing.
        :param num_replicas: Number of replicas for each node (virtual nodes).
        """
        self.num_replicas = num_replicas
        self.ring = {}  # Stores hash -> node mapping
        self.sorted_hashes = []  # Sorted list of hashes for efficient searching
        self.nodes = set()

    def _generate_hash_key(self, key: str) -> int: 
        """
        Hashes the given key using SHA1.
        :param key: Key to hash.
        :return: Hash value as an integer.
        """

        return int(hashlib.sha1(key.encode('utf-8')).hexdigest(), 16)

    
    def add_node(self, node: str) -> None:
        """
        Add a node to the hash ring.
        :param node: The node to add.
        """

        self.nodes.add(node)
        for i in range(self.num_replicas):
            replica_key = f"{node}#{i}"
            node_hash = self._generate_hash_key(replica_key)
            self.ring[node_hash] = node
            bisect.insort(self.sorted_hashes, node_hash)        

    def remove_node(self, node: str) -> None:
        """
        Remove a node from the hash ring.
        :param node: The node to remove.
        """

        if node not in self.nodes:
            return

        self.nodes.remove(node)

        for i in range(self.num_replicas):
            replica_key = f"{node}#{i}"
            node_hash = self._generate_hash_key(replica_key)            

            if node_hash in self.ring:
                del self.ring[node_hash]
                self.sorted_hashes.remove(node_hash)
            
    def get_node(self, key) -> str:
        """
        Get the node responsible for a given key.
        :param key: The key to map.
        :return: The node that maps to the given key.
        """

        key_hash = self._generate_hash_key(key)
        idx = bisect.bisect(self.sorted_hashes, key_hash)
        if idx == len(self.sorted_hashes):
            idx = 0

        node_hash = self.sorted_hashes[idx]        
        return self.ring[node_hash]
