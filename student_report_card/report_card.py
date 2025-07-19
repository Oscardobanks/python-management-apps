import json
import os

DATA_FILE = "students.json"


class Student:
    def __init__(self, name, subjects, scores):
        self.name = name
        self.subjects = subjects
        self.scores = scores
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def calculate_grade(self):
        avg = self.average
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B+"
        elif avg >= 60:
            return "B"
        elif avg >= 55:
            return "C+"
        elif avg >= 50:
            return "C"
        elif avg >= 45:
            return "D+"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "scores": self.scores,
            "average": self.average,
            "grade": self.grade,
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["subjects"], data["scores"])


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump([s.to_dict() for s in students], f)


def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Student.from_dict(d) for d in data]
    return []


def add_student(students):
    name = input("Student name: ")
    subjects = input("Subjects (comma separated): ").split(",")
    subjects = [s.strip() for s in subjects]
    scores = []
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Score for {subject}: "))
                break
            except:
                print("Invalid score.")
        scores.append(score)
    student = Student(name, subjects, scores)
    students.append(student)
    print("Student added.")


def view_students(students):
    if not students:
        print("No students yet.")
    for s in students:
        print(f"\nName: {s.name}")
        for subj, score in zip(s.subjects, s.scores):
            print(f"  {subj}: {score}")
        print(f"Average: {s.average:.2f}, Grade: {s.grade}")


def update_student(students):
    name = input("Enter student name to update: ")
    for s in students:
        if s.name.lower() == name.lower():
            print("Updating scores...")
            for i, subj in enumerate(s.subjects):
                try:
                    new_score = float(
                        input(f"New score for {subj} (old: {s.scores[i]}): "))
                    s.scores[i] = new_score
                except:
                    print("Invalid. Keeping old score.")
            s.average = s.calculate_average()
            s.grade = s.calculate_grade()
            print("Student updated.")
            return
    print("Student not found.")


def main():
    students = load_students()
    while True:
        print("\n1. Add student\n2. View students\n3. Update student\n4. Save & Exit")
        op = input("Choose: ")
        if op == "1":
            add_student(students)
        elif op == "2":
            view_students(students)
        elif op == "3":
            update_student(students)
        elif op == "4":
            save_students(students)
            print("Saved. Bye!")
            break
        else:
            print("Invalid.")


if __name__ == "__main__":
    main()
