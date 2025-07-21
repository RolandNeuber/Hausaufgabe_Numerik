zahlen = 0
for e in range(-2, 3): # -2 bis 2
    for a1 in range(1, 3):
        for a2 in range(0, 3):
            for a3 in range(0, 3):
                print("(0." + str(a1) + str(a2) + str(a3) + ") * 3^" + str(e) + " = " + str(3 ** e * (a1 * 3 ** -1 + a2 * 3 ** -2 + a3 * 3 ** -3)))
                zahlen += 1

print("Anzahl normalisierter Zahlen: " + str(zahlen))

print()

zahlen_den = 0
a1 = 0
e = -2
for a2 in range(0, 3):
    for a3 in range(0, 3):
        print("(0." + str(a1) + str(a2) + str(a3) + ") * 3^" + str(e) + " = " + str(3 ** e * (a1 * 3 ** -1 + a2 * 3 ** -2 + a3 * 3 ** -3)))
        zahlen_den += 1

print("Anzahl denormalisierter Zahlen: " + str(zahlen_den))