# Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].

def digits(s):
    digit_list = [int(i) for i in str(s)]
    return digit_list

print(digits(1234))



# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.

def sort_two(a,b):
    return sorted(a + b)

print(sort_two([1, 2, 4, 5], [3, 6, 7, 8]))



# Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].