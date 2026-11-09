class HashTable:
    def __init__(self, capacity=10):
        self.buckets = [[] for _ in range(capacity)]
        self.count = 0

    def _index(self, key):
        return hash_key(key) % len(self.buckets)

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value                   # existing key: overwrite
                return
        bucket.append([key, value])
        self.count += 1
        if self.count / len(self.buckets) > 0.7:
            self._resize()

    def get(self, key):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return None

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def __len__(self):
        return self.count

    def _resize(self):
        old = self.buckets
        self.buckets = [[] for _ in range(2 * len(old))]
        for bucket in old:                        # rehash: the cell depends on the size
            for pair in bucket:
                self.buckets[self._index(pair[0])].append(pair)
