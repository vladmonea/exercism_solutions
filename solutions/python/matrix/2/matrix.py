from copy import deepcopy


class Matrix(object):
    def __init__(self, matrix_string):
        self.string_rows = matrix_string.splitlines()
        self.matrix = self.parse_matrix()

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index-1])
        return column

    def parse_matrix(self):
        matrix = [[int(num) for num in row.split()]
                  for row in self.string_rows]
        return matrix
