from fractions import Fraction


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


if __name__ == "__main__":
    A = [
        [1.2969, 0.8648],
        [0.2161, 0.1441],
    ]
    bs = [
        [0.8642, 0.1440],
        [0.86419999, 0.14400001],
        [0.8641999, 0.1440001],
        [0.864199, 0.144001],
        [0.86419, 0.14401]
    ]
    A_frac = [[Fraction.from_float(num) for num in equation] for equation in A]
    bs_frac = [[Fraction.from_float(num) for num in equation] for equation in bs]

    for i, b in enumerate(bs_frac):
        M = [[*c, x] for c, x in zip(A_frac, b)]

        xs = lgs_exakt(M)
        print("Exakte Berechnung: \n" + " \n".join(list("x" + str(i + 1) + ": " + format(x, ".15g") for i, x in enumerate(xs))) + "\n")
