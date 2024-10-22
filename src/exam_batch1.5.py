students = {
    "Alice": {"Math": 80, "English": 75, "Science": 90},
    "Bob": {"Math": 70, "English": 85, "Science": 75},
    "Charlie": {"Math": 95, "English": 60, "Science": 85}
}

def cal_avg(students):
    avg = {}
    for student, subjects in students.items():
        total = 0
        num = len(subjects)
        for mark in subjects.values():
            total+=mark
        avg[student] = round(total/ num, 2)
    print(avg)
    
    top_student = max(avg, key=avg.get)
    return top_student

print(f"Our top student with most highest average is {cal_avg(students)}")