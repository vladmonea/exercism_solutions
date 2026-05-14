from enum import Enum


class Plants(Enum):
    V = "Violets"
    R = "Radishes"
    C = "Clover"
    G = "Grass"


class Garden:
    students = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harrit",
        "Ileana", "Joseph", "Kincaid", "Larry"
    ]
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.positions = self.assign_positions(students)

    def assign_positions(self, students):
        if not students:
            students = self.__class__.students
        students = sorted(students)
        positions = {
            student: 2 * pos for pos, student in enumerate(students)
        }
        return positions

    def plants(self, name):
        pos = self.positions.get(name)
        if pos is None:
            raise KeyError("No such student")
        plants = []
        for row in self.diagram.split('\n'):
            plants.extend(list(row[pos: pos + 2]))
        return [
            Plants[plant].value for plant in plants
        ]

