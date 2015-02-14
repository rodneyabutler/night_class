#dictionary = {'Bob'{'name': 'Bob', 'age': 22}, 'Carol'{'name': 'Carol', 'age': 47}, 'Justin'{'name': 'Justin', 'age': 14}}
#d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}
#print (dictionary)

people = {
    "bob" : { "age":22},
    "carol" : {"age": 47},
    "justin" : { "age": 14}
}

for index, person in people.items():
    print index, person["age"]

people = {
    "bob" : { "age":22},
    "carol" : {"age": 47},
    "justin" : { "age": 14}
}
for person in people:
    print person["name"], person["age"]