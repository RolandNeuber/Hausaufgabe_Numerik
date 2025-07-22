# Aufgabe 4
# Gegeben sei das LGS
# 0.035 x1 + 3.62 x2 = 9.12
# 1.17 x1 + 1.42 x2 = 5.89
# • Bestimmen Sie die exakte Lösung
# • Wir rechnen nun in einem Zahlensystem mit 3 Stellen Genauigkeit. Bes-
# timmen Sie in diesem System die Lösung jeweils mit der Diagonalstrategie
# und der Spaltenmaximumstrategie!

from fractions import Fraction
import math
import random

def round_sig(x, sig=3):
    """Runden auf `sig` signifikante Stellen."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def main():
    A = [[0.035, 3.62], [1.17, 1.42]]
    b = [9.12, 5.89]
    # A = [[random.random() ** 3 * 10 for r in range(5)] for zeile in range(5)]
    # b = [random.random() ** 3 * 10 for r in range(5)]
    M = [[*c, x] for c, x in zip(A, b)]

    print("Erweiterte Matrix:")
    for zeile, res in zip(A, b):
        print("  ".join(f"{element:>8.4f}" for element in zeile) + " | " + f"{res:>8.4f}")

    print()

    xs = lgs_exakt([[Fraction.from_float(element) for element in zeile] for zeile in M])
    print("Exakte Berechnung: \n" + " \n".join(list("x" + str(i + 1) + ": " + format(x, ".15g") for i, x in enumerate(xs))) + "\n")

    xs = lgs_diagonal(M)
    print("Diagonalstrategie Berechnung: \n" + " \n".join(list("x" + str(i + 1) + ": " + format(x, ".15g") for i, x in enumerate(xs))) + "\n")

    xs = lgs_spaltenmaximum(M)
    print("Spaltenmaximumsstrategie Berechnung: \n" + " \n".join(list("x" + str(i + 1) + ": " + format(x, ".15g") for i, x in enumerate(xs))))

def lgs_exakt(M: list[list[Fraction]]) -> list[Fraction]:
    # Dreiecksmatrix herstellen    
    for i, akt_zeile in enumerate(M):
        for j, zeile in enumerate(M):
            if i >= j: 
                continue
            faktor = zeile[i] / akt_zeile[i]
            for k, element in enumerate(zeile):
                zeile[k] = element - akt_zeile[k] * faktor

    xs: list[Fraction] = []
    # Rücksubstitution
    for i, akt_zeile in enumerate(reversed(M)):
        rest = Fraction(0, 1)
        for j in range(i):
            rest += akt_zeile[-2 - j] * xs[j]
        xi = (akt_zeile[-1] - rest) / akt_zeile[-2 - i]
        xs.append(xi)

    xs.reverse()

    return xs

def lgs_diagonal(M: list[list[float]], precision: int = 3) -> list[float]:
    # Runden auf "Maschinengenauigkeit"
    M = [[round_sig(x, precision) for x in zeile] for zeile in M]

    # Dreiecksmatrix herstellen
    for i, akt_zeile in enumerate(M):
        for j, zeile in enumerate(M):
            if i >= j:
                continue
            faktor = round_sig(zeile[i] / akt_zeile[i], precision)
            for k, element in enumerate(zeile):
                zeile[k] = round_sig(element - round_sig(akt_zeile[k] * faktor, precision), precision)

    xs: list[float] = []
    # Rücksubstitution
    for i, akt_zeile in enumerate(reversed(M)):
        rest = 0.
        for j in range(i):
            rest = round_sig(rest + round_sig(akt_zeile[-2 - j] * xs[j], precision), precision)
        xi = round_sig(round_sig(akt_zeile[-1] - rest, precision) / akt_zeile[-2 - i], precision)
        xs.append(xi)

    xs.reverse()

    return xs

def lgs_spaltenmaximum(M: list[list[float]], precision: int = 3) -> list[float]:
    # Runden auf "Maschinengenauigkeit"
    M = [[round_sig(x, precision) for x in zeile] for zeile in M]

    # Dreiecksmatrix herstellen
    M.sort(key=lambda x: abs(x[0]), reverse=True)
    for i, akt_zeile in enumerate(M):
        for j, zeile in enumerate(M):
            if i >= j:
                continue
            faktor = round_sig(zeile[i] / akt_zeile[i], precision)
            for k, element in enumerate(zeile):
                zeile[k] = round_sig(element - round_sig(akt_zeile[k] * faktor, precision), precision)
        M[i + 1:] = sorted(M[i + 1:], key=lambda x: abs(x[i + 1]), reverse=True)

    xs: list[float] = []
    # Rücksubstitution
    for i, akt_zeile in enumerate(reversed(M)):
        rest = 0.
        for j in range(i):
            rest = round_sig(rest + round_sig(akt_zeile[-2 - j] * xs[j], precision), precision)
        xi = round_sig(round_sig(akt_zeile[-1] - rest, precision) / akt_zeile[-2 - i], precision)
        xs.append(xi)

    xs.reverse()

    return xs

if __name__ == "__main__":
    main()
