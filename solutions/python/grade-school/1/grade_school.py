class School:
    def __init__(self):
       self.catalogue = []

    def add_student(self, name, grade):
        """Add a student and their grade to the catalogue."""
        self.catalogue.append((name, grade))

    def roster(self):
        """Return a list of the students ordered by grade, but not
        alphabetically. Students will instead be displayed in the
        order in which they were originally added.."""
        catalogue_sorted = sorted(self.catalogue, key=lambda x: x[1])
        return [n for n, g in catalogue_sorted]

    def grade(self, grade_number):
        """Return an alphabetically ordered list of the students
        of a certain grade."""
        return sorted(
            [
                name for name, grade in self.catalogue
                if grade == grade_number
            ],
        )

