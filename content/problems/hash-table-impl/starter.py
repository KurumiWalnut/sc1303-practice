# hash_key(key) is already loaded for you.


class HashTable:
    def __init__(self, capacity=10):
        self.buckets = [[] for _ in range(capacity)]
        self.count = 0

    def _index(self, key):
        return hash_key(key) % len(self.buckets)

    def put(self, key, value):
        # TODO
        pass

    def get(self, key):
        # TODO
        pass

    def remove(self, key):
        # TODO
        pass

    def __len__(self):
        # TODO
        pass

    def _resize(self):
        # TODO: twice as many cells, then put every pair back
        pass
