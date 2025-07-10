students = [
    {"name": "Alice", "age": 20, "grades": [85, 92, 78, 96, 88], "city": "New York"},
    {"name": "Bob", "age": 19, "grades": [76, 81, 85, 79, 83], "city": "Chicago"},
    {"name": "Charlie", "age": 21, "grades": [92, 88, 94, 91, 89], "city": "Los Angeles"},
    {"name": "Diana", "age": 18, "grades": [68, 72, 75, 70, 74], "city": "New York"},
    {"name": "Eve", "age": 20, "grades": [95, 98, 92, 97, 94], "city": "Chicago"},
    {"name": "Frank", "age": 22, "grades": [82, 85, 88, 84, 86], "city": "Miami"},
    {"name": "Grace", "age": 19, "grades": [78, 82, 85, 80, 83], "city": "Los Angeles"},
    {"name": "Henry", "age": 21, "grades": [89, 92, 87, 91, 88], "city": "Miami"}
]

task_1 = [grade for student in students for grade in student["grades"]]
#print(task_1)

task_2 = [name["name"] for name in students if sum(name["grades"]) / len(name["grades"]) > 85]
#print(task_2)

task_3 = [{'name': student["name"], 'highest' : max(student["grades"])} for student in students]
#print(task_3)

task_4 = [grade for student in students if student["city"] == "Chicago" or student["city"] == "New York" for grade in student["grades"] if grade > 90]
#print(task_4)(

task_5 = [f"{student['name']} ({student['age']}): {'Excellent' if sum(student['grades']) / len(student['grades']) >= 90 else 'Good' if sum(student['grades']) / len(student['grades']) >= 80 else 'Needs Improvement'}" for student in students]
print(task_5)