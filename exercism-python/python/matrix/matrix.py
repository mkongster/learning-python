class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(i) for i in row.split(' ')] for row in matrix_string.split('\n')]

        # zip transposes the rows
        self.columns = [list(l) for l in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]