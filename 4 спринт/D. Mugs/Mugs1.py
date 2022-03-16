class HashTable(object):
    """Sample Python Hash Table."""

    def __init__(self, slots):
        """Init method for hash table."""
        self.slots = slots
        self._table = [[] for num in range(slots)]

    def _hash(self, key):
        """Render key string as integer with additive algorithm."""
        if not isinstance(key, str):
            raise TypeError('please give us a string')
        hashnum = sum(ord(char) for char in key)
        return hashnum % self.slots

    def set(self, key, value):
        """Store given value in table using given key."""
        hashed_key = self._hash(key)
        self._table[hashed_key].append((key, value))

    def get(self, key):
        """Retrieve value from table given key."""
        hashed_key = self._hash(key)
        for tag, value in self._table[hashed_key]:
            if key == tag:
                return value
        return None


if __name__ == '__main__':
    size = int(input())
    hashtable = HashTable(size)
    parameters = input().split()
    for value in parameters:
        element = hashtable._hash(value)
        for element in parameters:
            hashtable.set(element, value)        
    result = hashtable.get(element for element in parameters)
    print(result)
