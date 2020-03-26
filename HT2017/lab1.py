def check_pnr(n):
	a = []
	pnr_summa = 0

	# Create list from input
	for i in range(len(str(n))):
		a.append(str(n)[i])

	# Add digit sums
	for i in range(len(a)-1):
		if (i % 2 == 0):
			tmp = (int(a[i]) * int(2))
			if tmp > 9:
				pnr_summa += 1 + tmp % 10 # Digit sum = 1 + 18 % 10 = 1 + 8 = 9
			else:
				pnr_summa += tmp
		else:
			pnr_summa += int(a[i])

	# Check the sum val
	if pnr_summa % 10 == 0:
		return n[9] == 0
	else:
		return (10 - (pnr_summa % 10) == int(a[9]))
