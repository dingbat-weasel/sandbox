
class HashTable:
    def __init__(self, size = 7):
        # initialize the table to length = size (default 7)
        self.data_map: list[list[list[str | int]] | None] = [None] * size

    def _hash(self, key):
        # BigO: O(1)

        # initialize hash
        my_hash = 0
        for letter in key:
            # convert each letter to an int, multiply by prime for less collisions, divide by length of table and take remainder
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        # BigO: O(1)

        # create the address
        index = self._hash(key)

        # store in variable to satisfy type checker
        bucket = self.data_map[index]

        # initialize an empty list at the address
        if bucket == None:
            bucket = []

        # set key, value
        bucket.append([key, value])


    def get_item(self, key):
        # BigO: O(1) to get address, O(n) to iterate in absolute worst case
            # - however the assumption is that the distribution of hashed keys is very good, esp w/ python dicts, and so bigO is considered O(1)

        # find the index of the item
        index = self._hash(key)

        # store in variable to satisfy type checker
        bucket = self.data_map[index]

        # as long as that index is not empty
        if bucket is not None:
            # check each member of the list present at that index
            for i in range(len(bucket)):
                # check the key of each member to the key we are getting
                if bucket[i][0] == key:
                    # if it matches, return the value
                    return bucket[i][1]

        # if index is empty or does not contain key 
        return None


    def keys(self):
        # initialize list of keys
        all_keys = []

        # for each index in the table
        for i in range(len(self.data_map)):
            # initialize as variable to satisfy type checker
            bucket = self.data_map[i]

            # if the bucket is not empty
            if bucket is not None:
                # check each member of the bucket arr
                for j in range(len(bucket)):
                    # add the key to the list of keys
                    all_keys.append(bucket[j][0])

        return all_keys
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")

my_hash_table = HashTable()



my_hash_table.set_item('abc', 123)
my_hash_table.set_item('washers', 1200)
my_hash_table.set_item('bolts', 50)
my_hash_table.set_item('books', 35)

print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('books'))
print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('suspenders'))



my_hash_table.print_table()

print(my_hash_table.keys())