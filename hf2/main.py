import sys


def palindrom():
    s = input("Adj meg egy stringet!\n")
    sf = s[::-1]
    if s == sf:
        print("Ez a string palindróm")
    else:
        print("Ez a string nem palindróm")
    return 0


def szamforditas(szam):
    return str(szam)[::-1]


def szamjegyek():
    print(len(str(2 ** 256)))


def osszeadasa():
    a = int(input("A="))
    b = int(input("B="))
    return a + b


def osszeadasb():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    return a + b


def haladostring():
    nev = input("Név:")
    ige = input("Ige:")
    targy = input("Tárgy:")
    print("{} {} a(z) {}".format(nev, ige, targy))
    print("{0} {1} a(z) {2}".format(nev, ige, targy))
    print(f"{nev} {ige} a(z) {targy}")
    print("{n} {i} a(z) {t}".format(n=nev, i=ige, t=targy))


def main():
    haladostring()


if __name__ == "__main__":
    main()
