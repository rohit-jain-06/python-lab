# Q. Check that a tuple cannot be changed in python.

x = ("apple", "banana", "cherry")
# change banana to kiwi
x[1] = "kiwi"
print(x)

# Output : TypeError: 'tuple' object does not support item assignment
