image = [
	[0,1,0,0],
	[0,0,0,0],
	[0,1,1,1],
	[0,1,1,1]
]

start_pixel = (1,3)
target_value = image[1][3]

height = len(image)
width = len(image[0])


def isInBounds(row,col):
	#returns boolean
	#true if row,col are within the input image bounds
	#false otherwise
	if row >= 0 and col >= 0 and row < height and col < width:
		return True

	return False

def pixelPerimeter(row,col):
	#returns int
	#the given pixel's perimeter
	#up, down, left, right
	perimeter = 0
	neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
	for i,j in neighbors:
		if not isInBounds(row+i,col+j) or image[row+i][col+j] != target_value:
			perimeter += 1
	return perimeter


##start solution

def dfs():
	stack = [start_pixel]
	visited = set()

	perimeter = 0
	neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
	while len(stack) > 0:
		row,col = stack.pop(-1)
		if (row, col) not in visited:
			print((row,col))
			visited.add((row,col))
			perimeter += pixelPerimeter(row, col)


		for i,j in neighbors:
			if isInBounds(row+i, col+j) and image[row+i][col+j]== target_value and (row+i, col+j) not in visited:
				stack.append((row+i,col+j))
				
	return perimeter

print(dfs())

def bfs():
	queue = [start_pixel]
	visited = set()
	visited.add(start_pixel)
	#print(visited)
	#neighbors up down left right
	directions = [(-1,0),(1,0),(0,-1),(0,1)]
	perimeter = 0
	#while queue non empty
	while len(queue) > 0:
		row,col = queue.pop(0)
		#visited.add((row,col))
		print((row,col))

		perimeter += pixelPerimeter(row,col)

		for i,j in directions:
			r = row+i
			c = col+j
			if isInBounds(r, c) and image[r][c] == target_value and (r,c) not in visited:
				queue.append((r,c))
				visited.add((r,c))
	return perimeter

print(bfs())








