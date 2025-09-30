
# dictionary in python means key : value pair, key and value should cotted with single/double qoutes, inside the curly braces.

a = {
    "name" : "Ahmed", # key : value pair 
    "rollnumber": 12
}

print(a["name"]) # give value of given key from the disc
print(a.keys()) # give all only keys inside the disc
print(a.values()) # give all only values inside the disc 
print(a.get("name")) # gives direct value of given key