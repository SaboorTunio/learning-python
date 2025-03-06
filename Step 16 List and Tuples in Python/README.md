# Tuples vs Lists

- **Mutability :**
  - **Lists :** Mutable - you can change, add, or remove items.
  - **Tuples :** Immutable - you cannot modify the contents once a tuple is created.
- **Use Case :** 
  - Use lists when you need a collection of items that can change.
  - Use tuples when the data is fixed and should not altered.

- **Nesting List and Tuples**
```
my_data = [("saboor",17),('maaz',18)]
for person in my_data :
    print(f"Name: {person[0]}, Age: {person[1]}")
```    