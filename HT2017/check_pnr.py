def check_pnr(n):

    pnr_summa = 0

    # Add digit sums
    for i in range(len(n)-1):
        if (i % 2 == 0):
            tmp = (int(n[i]) * 2)
            if tmp > 9:
                pnr_summa += 1 + tmp % 10 # Digit sum = 1 + 18 % 10 = 1 + 8 = 9
            else:
                pnr_summa += tmp
        else:
            pnr_summa += int(n[i])

    # Check the sum value
    if pnr_summa % 10 == 0:
        return n[9] == 0
    else:
        return (10 - (pnr_summa % 10) == int(n[9]))
