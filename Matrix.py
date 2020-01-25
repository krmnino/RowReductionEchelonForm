class Matrix:
    def __init__(self, data):
        self.matrix = []
        self.m = 0 #number of rows
        self.n = 0 #number of columns
        if ";" in data: #if ";" exists, there is more than 1 row in the matrix
            self.m = len(data.split(";")) #count the number of rows in the input
            self.n = len(data[0:data.find(";")].split()) #count the number of element per row
            for data_row in data.split(";"): #append each splited row into the matrix
                self.matrix.append([int(i) for i in data_row.split()]) 
                #append each element into a list (row) and then to matrix
        else: #input has only 1 row
            self.m = 1; #set number of rows to 1
            self.n = len(data.split()) #split data into single elements and count how many there are
            self.matrix.append([int(i) for i in data.split()]) #append the single row to matrix
    
    def swap_rows(self, index1, index2):
        if index1 < self.m or index2 < self.m: #if any of two indexes is less than number of rows, do normal swap
            temp_row = self.matrix[index1]
            self.matrix[index1] = self.matrix[index2]
            self.matrix[index2] = temp_row

    def row_addition(self, index1, index2): #add row at index 1 to row at index 2
        for i in range(0, self.n): #for each element from 0 to number of columns
            self.matrix[index1][i] += self.matrix[index2][i] #add current element in row1 to current element in row2
       
    def row_scale_up(self, row, scalar): #scale up a specific row by a given scalar
        for i in range(0, self.n):
            self.matrix[row][i] *= scalar #multiply current element by scalar
    
    def row_scale_down(self, row, scalar): #scale down a specific row by given scalar
        for i in range(0, self.n):
            self.matrix[row][i] /= scalar #divide current element by scalar

    def print_matrix(self): #print matrix, only works well with 1 digit numbers
        out = ""    #initialize out string for matrix contents
        for i, row in enumerate(self.matrix):   #iterate through m size
            for j in range(0, self.n):      #iterate through each element in row
                out += str(row[j]) + " "    #append row element to out string, add space
            print(out)     #print the matrix, create new line
            out = ""       #clear out string
