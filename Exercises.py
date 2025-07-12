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

fruits.remove('mango')
print('after removing mango', fruits)
#sorteding and reverse sorting
fruits.sort()
print("sorted_fruits", fruits)

fruits.reverse()
print("reverse_sorting", fruits)

reverse_sorting = sorted(fruits, reverse =True)
print("reverse_sorted_frutis", reverse_sorting)

print("original list", fruits)

#itering over a list
print("fruits one by one:")
for fruits in fruits:
    print("fruit itering,", fruits)

print ("fruit in uppercase")
for fruits in fruits:
    print(fruits.upper())

fruit_length = [len(fruits) for fruits in fruits]
print( fruit_length)

# fruits list with the letter containing E
fruit_with_e = [fruits for fruits in fruits if 'o' in fruits]
print(fruit_with_e)

#qns
prices = [20,30,50, 100,80]

def discount_price(prices, discount):
    """apply a discount % to each price."""
    discounted = [round(price * (1 - discount/100), 2) for price in prices]
    return discounted

discount_10 = discount_price(prices,10)
print("price after 10% discount", discount_10)

scores = [
    [85,92,78],  #student 1
    [76,88,90], #student 2
    [90,91,95]  # student 3
]
print("initial scores," ,scores)

#printing scores of student 1 in subject 2
print(scores[0][1])
print(scores[2][2])

print("all scores row by row")
for student_scores in scores:
    print(student_scores)

# printing each student score in tabular form
print("student scores row by row")
for i, student_scores in enumerate(scores):
  for j, score in enumerate(student_scores):
      print(f"student{i+2}:subject{j+2},{score}")

#adding another student scores
scores.append([88,79,85])  #student 4
print(scores)

scores.append([70,80,90])
print(scores)

scores[1][0] = 95
print("scores after updating",scores)
scores[4][1] = 82
print("updated scores of fifth student,",scores)

#priting average of students
print("average of students")
for i, student_scores in enumerate(scores):
    avg = sum(student_scores) / len(student_scores)
    print(f"student:{i+1}, average : {round(avg, 2)}")

#average subject wise
num_subjects = len(scores[0])
num_students = len(scores)

for subj in range(num_subjects):
    total = sum(scores[student][subj] for student in range(num_students))
    avg = total/ num_students
    print(f"subject{subj+1} average: {round(avg, 2)}")

#flattening a list into a single list
all_scores = [score for student in scores for score in student]
print(all_scores)

#highest score in list

highest = max(all_scores)
print("highest score among all students", highest)


#creating first function
def great():
   print("hello, nice to see you")

great()

def welcome_user():
    print("welcome to ACA")
welcome_user()

name = "karandeep Singh"

def great(name):
    print(f" welcome,{name}! nice to see you")
great(name)

great("karan")

#function with multiple parameters
def adding(a,b):
    result = a + b
    print(f"sum of {a} and {b} is {result}")
adding(10,5)

def substract(a,b):
    result = a - b
    print(f"substract {a} and {b} is {result}")

substract(12, 8)

def multiply(a,b):
    return a* b
my_age = multiply(2,3)
print("my age", my_age)

def divide(a,b):
    if b==0:
       return "error cannot divide by zero"
    return a/b

print("division", divide(12,7))


#function with default parameters
def greet_city(name, city = "vancouver"):
    print(f"{name}, lives in {city}")

greet_city("karan", "Punjab")

def introduce(name, age = 25):
    print(f"my name is {name} and i am {age} years old")

introduce("karan", 24)

def square(n):
    return [n*n]

numbers = [1,2,3,4,5]
squares= []

for n in numbers:
    squares.append(square(n))

print(squares)

def is_even(num):
    return num % 2 ==0

even_numbers = [n for n in numbers if is_even(n)]

print('even numbers,', even_numbers)


#built in functions
#get length of any list
print("length of fruits list", len(popped_fruits))

print("length of analytics,", len("analytics"))

#sum up values
numbers = [1,2,3,4,5]
print("sum of numbers,", sum(numbers))

print("sum of [1,3,5]:", sum([1,3,5]))




