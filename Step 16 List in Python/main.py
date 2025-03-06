# Introduction to Lists 
# Defination : Alist is a collection of items in a particular order. Lists are mutable, meaning you can change their contents.

# fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
# print(fruits)

# Accessing Elements in a list
# Using Indexing :
#List are zero-indexed, meaning the first item is at index 0.
#Example :

# fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
# print(fruits[0]) # Output : apple
# print(fruits[2]) # Output : orange
# print(fruits[-1]) # Output : ?


# Modifying Elements in a List
# Change the value of an item :
# Lists are mutable, so you can modify elements after creating the list.
# Example :


# fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
# print(fruits[0]) # Output : apple
# print(fruits[2]) # Output : orange
# print(fruits[-1]) # Output : ?
# fruits[1] ='cherry'
# print(fruits) # Outputs : ['apple', 'cherry', 'orange', 'grapes', 'mango'] 


# Slicing Lists
# Use Start : Stop to extract a portion of a list.
# Example :

fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(fruits[1:3]) # Output ['banana', 'orange']