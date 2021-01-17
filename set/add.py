# EX 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Output:{'cherry', 'orange', 'apple', 'banana'}

# EX2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Output: {'apple','cherry','pineapple','mango','banana','papaya'}