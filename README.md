# consistent_hashing
Implementation of consistent hashing

## Overview of Consistent Hashing
Why Use Consistent Hashing?

To distribute data across multiple nodes in a balanced way.
It minimizes the movement of keys when nodes are added or removed.

## How It Works:

Use a hash function to map nodes and keys onto a circular hash space.
Each node is responsible for the keys between itself and the previous node on the ring.
Components:

A hash function (e.g., MD5 or SHA1).
A ring to simulate the circular space.
Nodes and keys that are hashed into this space.
