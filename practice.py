fruits = ["apple", "banana", "cherry", "mango", "orange"]

for baaz in fruits:
    print( baaz)

fruits.append("baaz")
print(fruits)

fruits.pop()
print(fruits)
fruits.insert(2,"kela")
print(fruits)
print(fruits[0])
print(fruits[1])


changing_first_place = fruits.index("apple")
fruits[changing_first_place] = "daksh"
print( fruits)

fruits.remove("daksh")
print(fruits)


fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

sorted_frut = sorted(fruits)

reverse_sort = sorted(fruits, reverse= True)

for baaz in fruits:
    print( baaz.upper())

fruit_len = [len(fruits) for fruit in fruits]
print(fruit_len)

b_containing_letter = [baaz for baaz in fruits if 'b' in fruits]
print(b_containing_letter)

#functions

def greet():
    print("nice to see you")

def multiply(a,b):
    result = a + b
    print(f"sum of {a}  and sum of {b} is {result}")

multiply(3,4)



import numpy as np

print("zeros:\n", np.zeros([2,2]))
print("np ones", np.ones([2,4]))
print(np.full(2,3))
print(np.arange(1,10,2))
print("linspace", np.linspace(1,5, num = 5))
print("np.eye", np.eye(3))

numbersing = [11,22,33,25]

print(np.square(numbersing))
print( np.sqrt(numbersing))
print(np.exp(numbersing))
print(np.log(numbersing))




