a = {
    "name": "Akbar",
    "rollNumber": 12,
    "student": "yes",
    "marks": 90
}

# print(a, type(a))
print(a.items(), type(a)) # it shows the direct value of given key
print(a.keys()) # it shows the all keys of called disc
print(a.values()) # it shows the all values of called disc
print(a.get("rollNumber")) # it shows the direct value of given key
print(a.update({"name": "Amjad"})) # it update the existing value in dic and add which is not already present in disc
print(a)
print(a.pop("marks")) # it removes the given key's 'key-value' pair 
print(a)
b = a.popitem() # it removes and returns the last inserted key-value pair
print(b)