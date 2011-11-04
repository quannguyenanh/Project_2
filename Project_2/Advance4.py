#C1
def create_zero_matrix(size):
	matrix = []
	for i in xrange(size):
		matrix.append([])
		for j in xrange(size):
			matrix[i].append(0)
	return matrix

def print_matrix(matrix):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix)):
			print "%2d" %matrix[i][j],
		print "\n"

def spiral_matrix(n):
	dx,dy = 0,1 # increment indicator, follows clockwise	   
	x,y = 0,0   # start 
	matrix = create_zero_matrix(n)
	for i in xrange(1,(n**2+1)): # list of integer to input 1,2,3,...,N^2
		matrix[x][y] = i
		nx = x+dx # use nx, ny to check reach boundary
		ny = y+dy
		if 0<=nx<n and 0<=ny<n and matrix[nx][ny] == 0: # check boundary
			x = nx
			y = ny
		else:
			dx,dy = dy,-dx # if reach boundary then turn right and come back, take care of this assignment
			x += dx
			y += dy
	return matrix
	
N = raw_input("Enter the size of spiral matrix: >> ")
matrix = spiral_matrix(int(N))

print_matrix(matrix)