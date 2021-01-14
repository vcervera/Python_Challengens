# Write a function that builds a pyramid based on a number given 
"""
if 3 is given it would be
​
*
**
***
"""
​
​
def build_pyramid(x):
    counter = 1
    while counter < x:
        print(counter * "*")
        counter += 1
​
​
# build_pyramid(9)
​
​
def build_pyramid2(x):
    for i in range(x):
        print(i * "*")
​
​
# build_pyramid2(9)
​
​
# Write a function that takes a list of strings an prints them,
# one per line, in a rectangular frame. For example the list 
# ["Hello", "World", "in", "a", "frame"] gets printed as:
"""
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
"""
​
​
def hello_frame(ls):
    row_len = 0
    for i in ls:
        if len(i) > row_len:
            row_len = len(i)
    row_len = row_len + 4
​
    ends = row_len * "*"
    print(ends)
    for i in ls:
        space = (row_len - 4) - len(i)
        space_str = space * " "
        print("* " + i + space_str + " *")
    print(ends)
​
​
hello_frame(["Hello", "World", "in", "a", "frame"])
​
ret = "".join([str(x) for x in [1, 2, 3]])
​
print(ret)
​
​
# Write a function that rotates a list by k elements.
# For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
# Try solving this without creating a copy of the list.
# How many swap or move operations do you need?
​
​
def rotate_list(ls, offs):
    ofs = offs % len(ls)
    return ls[ofs:] + ls[:ofs]
​
​
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 8))


"""
write the following loop as a list comprension
tmp = []
for i in range(100):
    tmp.append(i)
"""

tmp =[]
for i in range(100):
    tmp.append(i)

hundred = [i for i in range(100) ]



"""
write the following function as a lambda
def square(x):
    return x * x
"""
def square(x):
    return x * x

square = lambda x: x*X




"""
create a class object "Book"
whose constructor // __init__
function takes in a title and author
and sets them as instance properties
Bonus:
add a method to the class called read that prints
the books title and says you are reading X
"""
class Book: 
    def__init__(self,title,author):
       self.title = title
       self.author = author
       
    def read(self):
        print(f"You are reading {self.title}")




lotr = Book("Tale of two Citties", "Dickiens")
lotr.read


"""
try creating a project folder and setting it up
with github,
push all your warmups to that repo
Bonus:
Adding a readme
"""