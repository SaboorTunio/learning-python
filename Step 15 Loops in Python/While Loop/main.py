#While Loop 

#Example

# count =1
# while count <= 5:
#     print(count)
#     count += 1

# Infinite loop
# What is an Infinite Loop?
# Occurs when the condition in the while loop never becomes false.
#  Danger: Can cause the program to crush or freeze.

#Example

# count = 1    
# while count > 0:
#     print(count)


# Controlling While Loops with a Counter
# Using a Counter: Often, you wil increment or decrement a variable to control the number of loop interactions.
# Example: 
# num = 10
# while num > 0:
#     print(f"Countdown: {num}")
#     num -= 1 # decrement the counter     

# Breaking Out of a loop
# Break Statement: Used to exit a loop even if the condition is still true.
# Explanation: The loop continues to run until the break statement is executed.
# Example:

# count = 1
# while True:
#     print(count)
#     count += 1
#     if count > 5:
#         break
# print("The loop is done!")


# Continue Statement: 
# continue statement : skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
# Example :

# count = 0
# while count < 10: 
#     count += 1
#     if count % 2 == 0:
#         continue # skipe printing even numbers
#     print(f"Odd number: {count}")


# Flags in While Loops
# what is Flage?
# A variable used to control whether the loop should continue or stop.

# Example :
# flag = True 
# while flag:
#     name = input("Do you want to continue (yes/no)? ")
#     if name == "no":
#         flag = False
#     else:
#         print(f"Hello, {name}")
#Explanation :** The loop continues untill the user types "no", at the point flag is set to False and the loop exits.

# Nested While Loops
#Explanation : A while loop can be placed inside another while loop
#Example :
# i =1
# while i <= 3:
#     j = 1
#     while j <= 3:
#         print(f"i: {i}, j: {j}")
#         j += 1
#     i += 1

# Combining a While Loop with an If Statements
# Example :

number = 1
while number <= 5:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    number += 1