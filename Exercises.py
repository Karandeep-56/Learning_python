#creating list

fruits = ["apple","banana", "carrot", "mango", "grapes"]
print("initial list", fruits)

#updatng a list
fruits.append("orange")
print("list after adding orange", fruits)

#accessing list elements
print('first fruit', fruits[0])
print("last fruit", fruits[-1])
print("second and third fruit",fruits[1:3])

fruits[2] = "strawberry"

index_apple = fruits.index("apple")
fruits[index_apple] ='watermelon'
print(fruits)

#adding something at first place
fruits.insert(0, "lemon")
print("adding lemon on first place",fruits)

#removing fruit from list
fruits.remove("banana")
print("after removing banana", fruits)
popped_fruits = fruits.pop()
print("removing last item", popped_fruits)
















