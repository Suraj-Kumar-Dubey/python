class Matrix:
	def __init__(self,array):
		self.array = array

	def __add__(self,other):
		new_matrix = []
		for i in range(len(self.array)):
			row = []
			for j in range (len(self.array[0])):
				row.append((self.array[i][j])+ (other.array[i][j]))
				new_matrix.append(row)
        	return Matrix(new_matrix)
	def __str__(self):
		return str(self.array)
	def multiply(self,other):
		new_matrix1 = []
		for i in range(len(self.array)):
			row1 = []
			for j in range(len(self.array[0])):
				for k in range(i,j):
				a=(self.array[i][j])*(self.array[j][i]))
				new_matrix1.append(row1)
		return Matrix(new_matrix1)


num_row = int(input("Eneter the number of row"))
num_column = int(input("Enter the number of coloumn"))
matrix = []
for i in range(num_row):
    row = []
    for j in range(num_column):
        cell = int(input())
        row.append(cell)
    matrix.append(row)
m1 = Matrix(matrix)
m2 = Matrix(matrix)
m3 = Matrix(matrix)
m4 = Matrix(matrix)

print m1
m5 = m1+m2
print m5
m6 = Matrix.multiply(m3,m4)
print m6
