# Introduction to Lists 
- **Defination :** Alist is a collection of items in a particular order. Lists are mutable, meaning you can change their contents.
```
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(fruits)
```

# Accessing Elements in a list
- **Using Indexing :**
  - List are zero-indexed, meaning the first item is at index 0.
- **Example :**
```

fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(fruits[0]) # Output : apple
print(fruits[2]) # Output : orange
```

# Modifying Elements in a List
- Change the value of an item :
  - Lists are mutable, so you can modify elements after creating the list.
- **Example :**
```
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(fruits[0]) # Output : apple
print(fruits[2]) # Output : orange
print(fruits[-1]) # Output : ?
fruits[1] ='cherry'
print(fruits) # Outputs : ['apple', 'cherry', 'orange', 'grapes', 'mango'] 
```

# Slicing Lists
- Use **Start : Stop** to extract a portion of a list.
- **Example :**
```
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(fruits[1:3]) # Output ['banana', 'orange']
```

# Looping Through a List

```
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
for fruit in fruits:
    print(fruit)
```

# List Operations
- **Length of a List :** Use **len()** to find out how many items are in a list.
- **Example :**
```
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(len(fruits)) # Output : 5
```

# List Comprehensions
- **What is List Comprehensions?** : Aconcise way to generate a list.
```
squares = [value**2 for value in range(1,11)]
print(squares) # Output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```