class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Stores {key: value}
        self.keys = []   # Stores [key1, key2...] to track order

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # We used it, so move it to the back (Most Recent)
        # This is the "expensive" O(N) unoptimized part
        self.keys.remove(key) 
        self.keys.append(key)
        
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to back
            self.keys.remove(key)
            self.keys.append(key)
            self.cache[key] = value
        else:
            # Add new key
            self.keys.append(key)
            self.cache[key] = value
            
            # Check if we are full
            if len(self.keys) > self.capacity:
                # The "Least Recently Used" is at the front (index 0)
                lru_key = self.keys.pop(0) 
                del self.cache[lru_key]