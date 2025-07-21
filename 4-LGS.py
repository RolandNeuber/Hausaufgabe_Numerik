# Aufgabe 4
# Gegeben sei das LGS
# 0.035 x1 + 3.62 x2 = 9.12
# 1.17 x1 + 1.42 x2 = 5.89
# • Bestimmen Sie die exakte Lösung
# • Wir rechnen nun in einem Zahlensystem mit 3 Stellen Genauigkeit. Bes-
# timmen Sie in diesem System die Lösung jeweils mit der Diagonalstrategie
# und der Spaltenmaximumstrategie!

from fractions import Fraction

def main():
    A = [[0.035, 3.62], [1.17, 1.42]]
    b = [9.12, 5.89]
    M = [[*c, x] for c, x in zip(A, b)]
    
    xs = lgs_exakt([[Fraction.from_float(element) for element in zeile] for zeile in M])
    print("Exakte Berechnung: " + str(list(format(x, ".15g") for x in xs)))

    xs = lgs_diagonal(M)
    print("Diagonalstrategie Berechnung: " + str(list(format(x, ".15g") for x in xs)))
    

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
    M = [[round(x, precision) for x in zeile] for zeile in M]

    # Dreiecksmatrix herstellen    
    for i, akt_zeile in enumerate(M):
        for j, zeile in enumerate(M):
            if i >= j:
                continue
            faktor = round(zeile[i] / akt_zeile[i], precision)
            for k, element in enumerate(zeile):
                zeile[k] = round(element - round(akt_zeile[k] * faktor, precision), precision)

    xs: list[float] = []
    # Rücksubstitution
    for i, akt_zeile in enumerate(reversed(M)):
        rest = 0.
        for j in range(i):
            rest += round(akt_zeile[-2 - j] * xs[j], precision)
        rest = round(rest, 3)
        xi = round(round(akt_zeile[-1] - rest, precision) / akt_zeile[-2 - i], precision)
        xs.append(xi)

    xs.reverse()

    return xs

def lgs_spaltenmaximum(M: list[list[float]], precision: int = 3) -> list[float]:
    return [1]

if __name__ == "__main__":
    main()
