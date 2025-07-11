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
