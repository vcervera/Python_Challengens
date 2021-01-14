import pprint
​

with open('fruit.txt', 'r') as f:
    fruit_data = f.read().split('\n')
    print(fruit_data)
​
fruit_dict = {}
for fruit in fruit_data:
    if fruit_dict.get(fruit[0]):
        fruit_dict[fruit[0]].append(fruit)
    else:
        fruit_dict[fruit[0]] = [fruit]
​
pprint.pprint(fruit_dict)
​
fruit_dict2 = {}
for fruit in fruit_data:
    if found := fruit_dict.get(fruit[0]):
        found.append(fruit)
    else:
        fruit_dict[fruit[0]] = [fruit]
​

# Write a function that takes in a list
# and returns items that are unique only
# f([1, 2, 3, 2, 5]) -> [1, 3, 5]
​
​
​
​
# Write a program that takes in a fruit list as
# txt and creates a dict that the:
# Key is the first letter &
# The value is a list of all that begin with that
# letter


