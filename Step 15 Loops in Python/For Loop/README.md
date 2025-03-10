# What is a for Loop ?
- **Defination :** A for loop is used to interate over a sequence (such as a list, string, or range) and execute a block of code for each element in the sequence.
- **Why Use For Loops ?** Simplifies code when you need to repeat action for every items in a each number.

# For Loop Syntax and Example
- **Syntax:**
``` 
for variable in sequence:
   # Code to execute for each item in sequence
```

- **Example :**
```
for letter in 'Python':
    print(letter)# First Example
```   

# How for Loops Work
- **Visualize the Iteration :**
- The for loop picks the first item from the sequence, assigns it to the loop variable, runs the code, then moves to the next item in the sequence.

- **Example with a List :**
```
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit)
```

# The range () Function
- **What is range()?** A function used to generate a sequence of number, commonly used in for loops.
   - range **(start,stop,step)**
- **start :** The starting number (default is 0).  
- **stop :**  The number at which the sequqnce stops (exclusive).
- **step :** The increment between numbers (default is 1).  
```
for number in range(1, 5):
    print(number)
```    

# Looping Over Strings
- **Explanation :** Strings are sequences, so you can use a for loop to iterate over each character in a string.

- **Example :**
```
for letter in 'Python':
    print(letter)
```

# Looping Over Lists
- **Example :**
```
cities = ['New York', 'Paris', 'London']
for city in cities:
    print(city)
```

# Nested for Loops
- **Explanation :** You can place one for loop inside another to perform more complex tasks.
- **Example :**
```
for i in range(1, 4):
    for j in range(1, 4):
        print(f'i = {i}, j = {j}')
```

# The Break Statement in For Loops
- **Explanation :** The break statement allows you to exit a loop before it has looped through all the items.
- **Example**
```
for num in range (1,11):
   if num == 5:
      break # # Exit the loop when num is 5
   print(num)
```

# The Continue Statement in For Loops 
- **Explanation :** The continue statement skips the rest of the current iteration and moves to the next iteration.
- **Example**   
```
for num in range (1,11):
   if num == 5:
      continue # Skip the rest of the code in the loop
   print(num)
   ```

# Looping over a Dictionary
- **Explanation :** You can loop over dictionaries to access keys and values.
- **Example :**
```

person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')
```

