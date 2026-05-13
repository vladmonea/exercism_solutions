class Matrix(object):
    def __init__(self, matrix_string):
        self.string_rows = matrix_string.split('\n')
        self.matrix = self.parse_matrix()

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index-1])
        return column

    def parse_matrix(self):
        matrix = [[] for i in range(len(self.string_rows))]
        for ix, row in enumerate(self.string_rows):
            matrix[ix].extend([int(num) for num in row.split()])
        return matrix
