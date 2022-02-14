def maze_runner(N, M):
	# TODO: Input of the table
	# N is the number of rows and M is number of columns
	N = 3
	M = 4
	table = [[3,10,8,14],[1,11,12,12],[6,2,3,9]]
	visited_matrix = [[False for _ in range(M)] for _ in range(N)]
	queue = []

	# Queue is you append at the back, and pop from the front (Stack, append at the back, pop from the back)
	queue.append((0,0))

	# while queue is not empty
	while queue:
		curr_x, curr_y = queue.pop(0) # 1, 1
		print("Visiting: {}, {}".format(curr_x, curr_y))
		print("The visited_matrix is: {}".format(visited_matrix))
	
		# This is exit clause when we reach the final destination
		if curr_x == (N-1) and curr_y == (M-1):
			print("Found an exit!")
			return True

		if visited_matrix[curr_x][curr_y] == True:
			continue

		curr_value = table[curr_x][curr_y] # 3
		print("The current value is: {}".format(curr_value))
		# Find all the possible factors that fit within N by M
		all_possible_pairs = find_all_factors(curr_value, N, M)
		print("The factors found were: {}".format(all_possible_pairs))
		queue += all_possible_pairs
		visited_matrix[curr_x][curr_y] = True

	print("Failed to find an exit")
	return False



# Returns an array of all possible combination of factors that fit within the table
# For ex: if val is 3, it will return [(1,3),(3,1)]
def find_all_factors(val, N, M):
	# Lets use a set here so that it automatically makes sure that every pair is unique (1,3) and (1,3) it will block duplicates
	pair_combinations = []

	# We are starting at 1, not 0
	for i in range(1, val+1):
		if val % i == 0:
			other_pair_val = int(val / i)
			if i > N or other_pair_val > M:
				continue

			pair_combinations.append((i-1, other_pair_val-1))

	return pair_combinations


maze_runner(3,4)