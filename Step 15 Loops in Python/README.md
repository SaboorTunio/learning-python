<h1 style="text-align: center;"> What is Loop ? </h1>

- **Defination:** A loop is control flow structure that repeats a block of code as long as a condition is true.
- **Why use loops ?**
 - Automate repetitive times.
 - Process data multiple times.
 - Reduce redundancy in code.

## There are two main types of loops in Python:
1. **For loop**
   - The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or any other iterable object.
     -  *Example:**
```
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

```
2. **While loop**
   - The while loop is used to repeatedly execute a block of code as long as a given condition is true. 
     -  *Example:**
```
count = 0
while count < 5:
    print(count)
    count += 1

```

# **Comparing For and While Loops**

<h1 style="text-align: center;">While Loop</h1>

- **A while loop runs while a condition is True**
- **It's useful when you don't know how many times you need to loop.**
- **Example :**
```
i = 1
while i <=5:
    print(i)
    i += 1
```

<h1 style="text-align: center;">For Loop</h1>

- **A For loop iterates over a known sequence or range.**
- **Its useful when you know how many time you want to iterate.**
- **Example :**

```
for i in range(1,6):
    print(i)
```    

