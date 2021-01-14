# Fizzbuzz

"""
given a number n:
    for all numbers 1..n
    if the number divides evenly by 3 -> fizz
    if the number divides evenly by 5 -> buzz
    if the number divides evenly by 3 and 5 -> fizzbuzz
    otherwise -> n

"""

# up_till = int(input("Number?"))
# for n in range(1,up_till + 1): 
#     if n % 15 == 0:
#         print("FizzBuzz")
#     elif n % 3 ==0:
#         print ("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)


#  Write a program that prints number of primes 

# def find_primes(n):
#     primes = []
#     num_to_check = 2
#     while len(primes) < n:
#         found_match = False
#         for p in primes:
#             if num_to_check % p == 0:
#                 found_match = True
#                 break
#             if not found_match:
#                 primes.append(num_to_check)
#             num_to_check += 1
#     return primes
 

# result = find_primes(3)
# print(result)
    






# Write a program that is a higher lower guessing game
# try:
#     usr_input = int(input("> "))
# except ValueError as err:
#     pass

# print("Keep on swimming")
# def guessing_game(secret):
#     print("try to guess my number!")
#     while(True):
#         usr_input = None
#         try:
#             usr_input = int(input("> "))
#         except Exception:
#             pass

#         if usr_input:
#             if usr_input == secret:
#                 print("That was my number, good job!")
#                 return
#             elif usr_input > secret:
#                 print("Your number was to high")
#             elif usr_input < secret:
#                 print("Your number is to low")

# guessing_game(37)


#write a program that prints the next 20 leap years
def leap_years(starting_year):
    upcomming_years = []
    current_year = starting_year

    while len(upcomming_years) < 20:
        if current_year % 4 == 0 and \
            current_year % 100 != 0 or current_year % 400 == 0:
            upcomming_years.append(current_year)
        current_year +=1
   
    return upcomming_years



print(leap_years(2001))