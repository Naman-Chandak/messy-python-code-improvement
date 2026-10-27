"""Student grade report.

Same output as messy.py, rewritten so every job has its own function,
every number has a name, and the code explains itself.
"""

PASS_MARK = 50

# (minimum average, grade) checked from the top down
GRADE_BOUNDARIES = [(90, "A"), (75, "B"), (60, "C"), (50, "D")]
LOWEST_GRADE = "F"

STUDENTS = [
    {"name": "Aarav", "marks": [78, 85, 92]},
    {"name": "Diya", "marks": [66, 71, 58]},
    {"name": "Kabir", "marks": [90, 95, 88]},
    {"name": "Meera", "marks": [45, 52, 60]},
]


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    for minimum, grade in GRADE_BOUNDARIES:
        if average >= minimum:
            return grade
    return LOWEST_GRADE


def build_results(students):
    """Add total, average and grade to each student."""
    results = []
    for student in students:
        average = calculate_average(student["marks"])
        results.append({
            "name": student["name"],
            "total": calculate_total(student["marks"]),
            "average": average,
            "grade": assign_grade(average),
        })
    return results


def class_average(results):
    return sum(r["average"] for r in results) / len(results)


def count_passed(results):
    return sum(1 for r in results if r["average"] >= PASS_MARK)


def print_report(results):
    for r in results:
        print(r["name"], "-", r["total"], "-", round(r["average"], 2), "-", r["grade"])

    topper = max(results, key=lambda r: r["average"])
    lowest = min(results, key=lambda r: r["average"])

    print("class avg", round(class_average(results), 2))
    print("topper", topper["name"], round(topper["average"], 2))
    print("passed", count_passed(results), "out of", len(results))
    print("lowest", lowest["name"], round(lowest["average"], 2))


def main():
    print_report(build_results(STUDENTS))


if __name__ == "__main__":
    main()
