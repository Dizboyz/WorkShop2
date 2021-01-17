# EX 1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # Output:{'apple', 'cherry'}

# EX 2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # Output:{'cherry', 'apple'}

# EX3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(thisset)


# EX4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)