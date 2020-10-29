# Defining all functions
def average(a):
    return float(sum(a)) / float(len(a))
def get_average(a):
    total = 0
    for y in a:
        if y == "homework":
            total += average(a[y])*0.10
        elif y == "quizzes":
            total += average(a[y])*0.30
        elif y == "tests":
            total += average(a[y])*0.60
    return total
def get_letter_grade(a):
    if a >= 90:
        return "A"
    elif a >= 80:
        return "B"
    elif a >= 70:
        return "C"
    elif a >= 60:
        return "D"
    else:
        return "F"
def get_class_average(a):
    results = []
    for z in a:
        results.append(get_average(z))
    return average(results)

# Creating student information
eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}
armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}
# Student list
students = [eren,mikasa,armin]

# Prints individual information as well as class averages
for x in students:
    print("Name:",x["name"],"\nHomework:",x["homework"],"\nQuizzes:",x["quizzes"],"\nTests:",x["tests"],"\nWeighted grades:",get_average(x),"\nLetter Grade:",get_letter_grade(get_average(x)),"\n")
print("Class average grade:",get_class_average(students),"\nClass average letter grade:",get_letter_grade(get_class_average(students)))