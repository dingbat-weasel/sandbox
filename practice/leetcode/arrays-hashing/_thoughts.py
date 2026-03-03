"""
For hash maps python has dictionaries: with keys, and sets: without keys

General pattern for checking the presence of a value:

- initialize an empty hash map 'seen'
- iterate over array
- check if input val is in hash
- add input val to hash
"""


def check_match(input: list[int]):
    seen = set()
    for val in input:
        if val in seen:
            return True
        seen.add(val)
    return False


"""
When using a dictionary, can use .get(val, default) to ensure a value is added to the key during lookup if the lookup returns false

Often it saves memory to increment/add to a hash in one loop
and then decrement from it in another,
rather than using two hash maps to check presence of values
"""
