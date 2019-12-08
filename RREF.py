class Matrix:
    def __init__(self, data):
        self.matrix = []
        self.m = 0 #number of rows
        self.n = 0 #number of columns
        if ";" in data:
            self.m = len(data.split(";"))
            self.n = len(data[0:data.find(";")].split())
            for data_row in data.split(";"):
                self.matrix.append([int(i) for i in data_row.split()])
        else:
            self.m = 1;
            self.n = len(data.split())
            self.matrix.append([int(i) for i in data.split()])

    def print_matrix(self): #print matrix, only works well with 1 digit numbers
        out = ""    #initialize out string for matrix contents
        for i, row in enumerate(self.matrix):   #iterate through m size
            for j in range(0, self.n):      #iterate through each element in row
                out += str(row[j]) + " "    #append row element to out string, add space
            print(out)     #print the matrix, create new line
            out = ""       #clear out string

    def rref(self):
        for i in range(0, self.n):
            if i >= self.m or i >= self.n:
                break
            if self.matrix[i][i] == 0:
                self.swap_rows(i)
            self.divide_row(i, self.matrix[i][i])
            self.reduce_row(i)

    def swap_rows(self, index):
        for i in range(index, self.m):
            if self.matrix[i][index] != 0:
                temp = self.matrix[index]
                self.matrix[index] = self.matrix[i]
                self.matrix[i] = temp

    def divide_row(self, index, div):
        if div != 0:
            for i in range(0, self.n):
                self.matrix[index][i] /= div

    def reduce_row(self, index):
        for i in range(0, self.m):
            if i != index:
                scaled_current_row = [-1 * j * self.matrix[i][index] for j in self.matrix[index]]
                self.matrix[i] = [val + scaled_current_row[j] for j, val in enumerate(self.matrix[i])]
                          

a = Matrix(input())
a.print_matrix()
print()
a.rref()
print()
a.print_matrix()