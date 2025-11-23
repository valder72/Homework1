def filter_students():
    scores = {"Anna": 95, "Bob": 57, "Clara": 82}
    passed_students = {name: score for name, score in scores.items() if score >= 60}
    print("Результати:")
    for name, score in passed_students.items():
        print(f"|{name:^10s}|{score:^10d}|")
filter_students()