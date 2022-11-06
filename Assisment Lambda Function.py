#...Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

#...sample input: 10
#...sample output: 35


r = lambda a : a + 25
r = lambda x, y : x + y
print(r(25, 10))