def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def process_students():
    students = {}
    
    while True:
        name = input("Student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
            
        score = input(f"Score for {name}: ")
        score = int(score)
        
        grade = calculate_grade(score)
        students[name] = {"score": score, "grade": grade}
    
    # Generate report
    report_name = input("Report filename: ")
    with open(report_name, 'w') as f:
        for name, data in students.items():
            f.write(f"{name}: {data['score']} ({data['grade']})\n")
    
    print(f"Report saved to {report_name}")

def search_student():
    filename = input("Which grade file to search? ")
    student_name = input("Student name: ")
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if student_name in line:
                print(f"Found: {line}")
                return
    print("Student not found")

print("1. Process new students")
print("2. Search existing records")
choice = input("Choose option: ")

if choice == "1":
    process_students()
elif choice == "2":
    search_student()