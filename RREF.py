from Matrix import *
import copy

def find_pivot_row(matrix_obj, row, col):
    i = row
    while(i < matrix_obj.n):
        if matrix_obj.matrix[i][col] != 0:
            return i
        i += 1
    return -1

def rref(matrix_obj):
    copy_matrix = copy.deepcopy(matrix_obj)
    row = 0
    col = 0
    while(row < copy_matrix.m):
        while(True):
            if row >= copy_matrix.m or col >= copy_matrix.n:
                return copy_matrix
            new_pivot_row = find_pivot_row(copy_matrix, row, col)
            if new_pivot_row == col:
                break
            elif new_pivot_row == -1:
                col += 1
            else:
                copy_matrix.swap_rows(new_pivot_row, row)
                breaks
        if copy_matrix.matrix[row][col] != 0:
            copy_matrix.row_scale_down(row, copy_matrix.matrix[row][col])
        i = 0
        while(i < copy_matrix.m):
            if row != i:
                mul = -1 * copy_matrix.matrix[i][col]
                j = 0
                while(j < copy_matrix.n):
                    copy_matrix.matrix[i][j] = copy_matrix.matrix[i][j] + copy_matrix.matrix[row][j] * mul
                    j += 1
            i += 1
        col += 1
        row += 1
    return copy_matrix
