.# [Lists, Strings] Challenges
# Write a function that returns the largest element in a list

# def get_largest(col):
#     if col:
#         tmp = col[0]
#         for i in col:
#             if tmp < i:
#                 tmp = i
#         return tmp
#     return None
# print(get_largest([1, 2, 3, 4]))

# def largest(list):
#     max = list [0]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(largest([1, 2, 3, 4]))


# Write a function that checks whether an element occurs in a list

# def is_in(ls, elm):
#     #return elm in ls
#     for item in ls:
#         if item == elm:
#             return True
#     return False

# print(is_in(x, 8))
# print(8 in x)

# Write a function that returns the element s on odd positions in a list
# def odd_pos(ls):
#     # return ls[1::2]
#     tmp = []
#     for i, v in enumerate(ls):
#         if i % 2 != 0:
#             tmp.append(v)
#         return tmp

# print(odd_pos(["Justine", "Ada","Paulina","Amy"]))

# print(odd_pos(x))
# Write a function that computes the running total of a list

# def total_up_list(ls):
#     total = 0
#     for i in ls:
#         total += i
#     return total

# print(total_up_list([1, 2, 3, 4, 5, 6]))
# Write a function that tests whether a string is a palindrome

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

check_this = "racecar"
print(is_palindrome(check_this))



# [BONUS SPICY CHALLENGE]
# Write a function that reverses a list, if you can do it in place

def rev_inplace(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

y = [1, 2, 3, 4, 5, 6, 7]
print (y)
rev_inplace(y)
print(y)

start, stop = 0, 9
start, stop = stop, start 
print (start, stop)




# test_list = [1, 6, 3, 5, 3, 4]
# for i in test_list: 
#     if(i == 8) : 
#         print ("Element Exists") 
#     else:
#         print ("Element not found")

# L = [1, 2, 3, 4, 5, 6, 7]
# li = []
# count = 0
# for i in L:
#     if count % 2 == 1:
#         li.append(i)
#     count += 1
# print(li)




