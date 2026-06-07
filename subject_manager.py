class SubjectManager:
    def __init__(self):
        self.subjects = []

    def add_subject(self, name, grade):
        self.subjects.append([name, grade])

    def clear_subjects(self):
        self.subjects.clear()

    def calculate_gwa(self):
        if not self.subjects:
            return None

        total = sum(subject[1] for subject in self.subjects)
        return total / len(self.subjects)