from Matrix import *
import copy

def find_pivot_row(matrix_obj, row, col):   #returns pivot row position if found
    i = row #set index equal to i
    while(i < matrix_obj.n):    #while index is less than number of columns
        if matrix_obj.matrix[i][col] != 0:  #if element at index row and column position is not zero 
            return i    #return index position
        i += 1  #else, increase index by 1
    return -1 #if not found, return -1

def rref(matrix_obj):
    copy_matrix = copy.deepcopy(matrix_obj) #create deep copy of matrix object, use this copy to return rref()'ed matrix
    row = 0 #set row and column indexes to zero
    col = 0
    while(row < copy_matrix.m): #while row index is less than number of rows in matrix
        while(True): #while True...
            if row >= copy_matrix.m or col >= copy_matrix.n: #if row index greater than number of rows or col index creater than number of columns... 
                return copy_matrix  #return rref()'ed copy matrix
            new_pivot_row = find_pivot_row(copy_matrix, row, col) #get new pivot row position
            if new_pivot_row == col:    #if new pivot row position equals current column index
                break   #break while(True) loop
            elif new_pivot_row == -1:   #else if no pivot position found
                col += 1    #increase column index by 1
            else:
                copy_matrix.swap_rows(new_pivot_row, row) #else, swap rows with new pivot row and current row index
                break   #break while(True) loop
        if copy_matrix.matrix[row][col] != 0:   #if element at row index and column index is not zero
            copy_matrix.row_scale_down(row, copy_matrix.matrix[row][col]) #scale down row current element at row and column position
        i = 0   #initialize index i
        while(i < copy_matrix.m):   #while index i is less than the number of rows in matrix
            if row != i:    #if current row index is different to i index
                mul = -1 * copy_matrix.matrix[i][col]   #set multiplier equal to -1 times current element at i row position and column index position
                j = 0   #initialize index j
                while(j < copy_matrix.n):   #traverse through all elements in a row
                    copy_matrix.matrix[i][j] = copy_matrix.matrix[i][j] + copy_matrix.matrix[row][j] * mul 
                    #set element at i and j equal to the current element plus element at row index and j column times multiplier
                    j += 1 #increase j index by 1
            i += 1  #increase i index by 1
        col += 1    #increase column index by 1
        row += 1    #increase row index by 1
    return copy_matrix  #return rref()'ed copy matrix
