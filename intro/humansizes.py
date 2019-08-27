sum = 2 + 2
print(sum)
#List
my_list = ["renee", "leo", "clive", False, 41]
my_list.count("renee")
my_list.count(41)
my_list.append("tucker")
print(my_list)
my_list.count(41)
my_list.pop(2)
my_list.reverse()
print(my_list)
my_list.insert(1, 58)
print(my_list)
print(my_list)
my_list.insert(2, 58)
print(my_list)
my_new_list = list(["what"])
my_new_list = list("what")
print(my_list)

# Dictionary

my_pairs = {
    "name": "Fred",
    "age": 46
}
print(my_pairs)

name = my_pairs["name"]
print(name)

my_pairs["last"] = "Jones"
print(my_pairs)
my_pairs["address"] = {"street": "123 Sesame Street", "zip": 40503}
print(my_pairs)
print(my_pairs["address"]["zip"])
print("items", my_pairs.items())
print("values", my_pairs.values())

for foo in my_pairs.values():
    print(foo)

for foo in my_pairs.items():
    print(foo)

for key,value in my_pairs.items():
    print(f"This came from my_pairs: {value}")

print(f'Hello, my name is {my_pairs["name"]}')

# Sets

my_set = {"fred", 3, 12, True, "Jones", 3}
print("set", my_set)

my_dupes = [1,2,3,4,5,1]
my_dupes = set(my_dupes)
print(list(my_dupes))

my_set.add("hello C33")
print(my_set)
print(set(my_pairs))

# Tuples

my_tup = ("1", 1, 3, "hello", True, 3)
print(my_tup)
my_tup.count(3)
print(my_tup.count(3))
print(my_tup.index("hello"))

# Conditionals

name = "Steve"
if name == "Steve":
    print("I feel good")
elif name == "Joe":
    print("Joe is the king of the world")
else:
    print("I have a cold")


SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    # '''Convert a file size to human-readable form.

    # (this is a docstring)

    # Keyword arguments:
    # size -- file size in bytes
    # a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
    #                             if False, use multiples of 1000

    # Returns: string

    # '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=False))
    print(approximate_size(-16384))














