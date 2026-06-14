'''Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1
'''
import random
from collections import Counter
from typing import List, Dict
def generate_random_grades(students: List[str]) -> Dict[str, int]:
    grades = {student: random.randint(1, 5) for student in students}
    return grades
def count_grades(grades: Dict[str, int]) -> Dict[int, int]:
    grade_counts = Counter(grades.values())
    return dict(grade_counts)   
def calculate_pass_percentage(grades: Dict[str, int]) -> float:
    total_students = len(grades)
    passing_students = sum(1 for grade in grades.values() if grade > 1)
    pass_percentage = (passing_students / total_students) * 100 if total_students > 0 else 0
    return pass_percentage
if __name__ == "__main__":
    students = ["Ana", "Marko", "Ivana", "Petar", "Luka"]
    grades = generate_random_grades(students)
    print("Ocjene studenata:", grades)
    
    grade_counts = count_grades(grades)
    print("Broj ocjena:", grade_counts)
    
    pass_percentage = calculate_pass_percentage(grades)
    print(f"Postotak prolaznosti: {pass_percentage:.2f}%")
