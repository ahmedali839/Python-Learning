lists = [
    1,
    4,
    5,
    6,
    33,
    5555,
    2,
]

# index = 0
# for item in lists:
#     print(f"The value {item} at index {index}")
#     index += 1

for index, item in enumerate(lists): # index gives index and item gives that index's value
    print(f"The value {item} at index {index}")
