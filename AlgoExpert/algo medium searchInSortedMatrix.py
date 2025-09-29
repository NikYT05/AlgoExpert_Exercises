def searchInSortedMatrix(matrix, target):
   row = 0
   column = 0

   while True:
       if row == len(matrix):
           return [-1,-1]
       
       if matrix[row][column] == target:
           return [row, column]
       
       if target in matrix[row]:
           break
       else:
           row += 1
           
   while column < len(matrix[row]):
       if matrix[row][column] == target:
           return [row, column]
       
       else: column += 1
       
   return [-1,-1]
       
       
searchInSortedMatrix([
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
], 44)