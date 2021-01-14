# Create a function that takes in a number and returns it's 
# length, you can't use the len() function 
# def string_length(my_string):
#     counter = 0
#     for char in my_string:
#         counter += 1
#     return counter

# # taking user input
# string_input = input("enter string :")
# length = string_length(string_input)

# print(length)

# def num_len(n):
#     s_num = str(n)
#     total_len = 0
#     for _ in s_num:
#         total_len += 1
#     return total_len

# print(num_len(147258))



# write a function that takes in two lists 
# and only returns elements that are found in both 
  
# def common_member(a, b): 
#     a_set = set(a) 
#     b_set = set(b) 
  
#     if (a_set & b_set): 
#         print(a_set & b_set) 
#     else: 
#         print("No common elements")  
           
   
# a = [1, 2, 3, 4] 
# b = [6, 7, 8, 9] 
# common_member(a, b) 

# def find_shared(x,y):
#     return set(x).intersection(set(y))

# print(find_shared([1,2,3],[3,4,5]))


# write a function that checks for the larges number 
# palindrome from 1*1 up to x*y 
# example 1*11 is a 11 a palindrome, the  
# function should take an x and a y and  
# only give you back the largest 

# def find_number_pal2(x, y):
#     tmp = []
#     for i in range(1, x+1):
#         for j in range(1, y+1):
#             s = str(i*j)
#             if s == s[::-1]:
#                 tmp.append(i*j)
#     return max(tmp)
# ​
# ​
# print(find_number_pal2(100, 300))


# given an list of numbers, return the one that 
# occurs an odd number of times. 
# your input list will only have one that qualifys  
# def getOddOccurrence(arr, arr_size): 
      
#     for i in range(0, arr_size): 
#         count = 0
#         for j in range(0, arr_size): 
#             if arr[i] == arr[j]: 
#                 count+= 1
              
#         if (count % 2 != 0): 
#             return arr[i] 
          
#     return -1

# arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ] 
# n = len(arr) 
# print(getOddOccurrence(arr, n))


def odd_occur(num_list):
    for n in num_list:
        if num_list.count(n) % 2 != 0:
            return n

print(odd_occur([1,2,3,4,5,6,1,2,3,4,6]))

# Write a function that generates the Fibonacci 
# sequence 
# 1, 2, 3, 5, 8, 13, 21, 34.... 
# who's total elements is equal to the number 
# the user passes into the function 




# Bonus: Return a tuple (x, y) 
# where x is the list of all generated elements 
# and y is the sum of those elements 


def gen_fibs(n):
    if n == 0:
        return
    if n == 1:
        return 1
​
    tmp = []
​
    x = 0
    y = 1
    count = 0
    while count < n:
        tmp.append(x)
        x, y = y, x+y
        count += 1
​
    return tmp
    # bonus
    # return (tmp, sum(tmp))
​
​
