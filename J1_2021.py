def boiling_water(B):
	P = 5 * B - 400
	if P < 100:
		sea_level = 1
	elif P == 100:
		sea_level = 0
	else:
		sea_level = -1

	print(P)
	print(sea_level)


B = int(input())
boiling_water(B)
