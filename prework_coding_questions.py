# Justin Nguyen
# Python Coding Questions
# 10-8-23


#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
print("Question_1:") #ignore, just to make the console readable
def hello_name(user_name): 
    print("hello_" + user_name + "!") #the format the prompt is addressing
    return #returning the line

print("The name of the function is:") #ignore, just to make the console readable
hello_name("USERNAME") #print statment

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
print("Question_2:") #ignore, just to make the console readable
def first_odds():
    for i in range (1, 100, 2): #the numbers in between 1-100 that are odd
        print(i)

print("The following numbers are odd from the numbers from 0-100:") #ignore, just to make the console readable
first_odds() #print statement

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
print("Question_3:") #ignore, just to make the console readable
def max_num_in_list(a_list):
    if not a_list:
        return None # Returns None for an empty list
    
    max_num = a_list[0] # Max_num would be read by the first element

    for num in a_list[1:]: # Going through the rest of the elements
        if num > max_num:
            max_num = num # Updates max_num if a larger number is found
    
    return max_num # Returns the maximum number

ex_list = [0, 5, 19, 48, 60] # Example list
print("The maximum number in the list is:", max_num_in_list(ex_list))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
print("Question_4:") #ignore, just to make the console readable

def is_leap_year(a_year): # How often do we expect a leap year? - approximately every 4 years
    if a_year % 4 == 0: # We want to see if a year is a leap year or not
        if a_year % 100 == 0 and a_year % 400 != 0: #if the year is divisable by 100 and not 400, which would make it false
            return False #if divided by 400, print False
        else:
            return True #if divided by 4 or 100, print True
    else: return False

year = 2020 #example year
print(f"Is {year} a leap year? {is_leap_year(year)}") #print statment


#Question 5
#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
print("Question_5:") #ignore, just to make the console readable
def is_consecutive(a_list):
    if not a_list: #if not in a_list, the answer will become False
        return False
    
    for i in range(1, len(a_list)): # check to see if element in list is equal to previous element and chooses that number (the highest number)
        if a_list[i] != a_list[i-1] +1:
            return False #If the list is not consecutive, it will print False
        
    return True #If all of theelements are consecutive, return True

list1 = [2, 3, 4, 5, 6, 7] #example list
list2 = [1, 2, 4, 5] #example list

print(f"Are {list1} consecutive? {is_consecutive(list1)}") #consecutive, prints out True
print(f"Are {list2} consecutive? {is_consecutive(list2)}") #nonconsecutive, prints out False