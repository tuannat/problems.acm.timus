def check(x):
	if (x - 4) <= 0:
		return "few"
	elif (x - 9) <= 0:
		return "several"
	elif (x - 19) <= 0:
		return "pack"
	elif (x - 49) <= 0:
		return "lots"
	elif (x - 99) <= 0:
		return "horde"
	elif (x - 249) <= 0:
		return "throng"
	elif (x - 499) <= 0:
		return "swarm"
	elif (x - 999) <= 0:
		return "zounds"
	else:
		return "legion"
		
print check(int(raw_input()))