# HashTable class using chaining
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # Complexity: O(N)
    def __init__(self, initial_capacity=40):
        # Initializes the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # Complexity: O(N) (Best: O(1))
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value_)
            if kv[0] == key:
                kv[1] = item
                return True
        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Complexity: O(N) (Best: O(1))
    def search(self, key):
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                return key_value[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # Complexity: O(N) (Best: O(1))
    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Removes the item from the bucket list if it is present
        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
