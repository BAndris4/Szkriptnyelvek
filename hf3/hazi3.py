TEXT = """
3Z 4Z UZ3N37 4Z7 4 C3L7 5Z0LG4LJ4, H0GY B3B1Z0NY1754
M1LY3N C50D4L4705 D0LG0KR4 K3P35 4Z 3LM3.
3LK3P35Z70 D0LG0KR4! N3H3Z V0L7 3L05Z0R 3L0LV45N0D
3Z7, D3 M1R3 1D33R5Z 3HH3Z 4 50RH0Z, 4Z 3LM3D
4U70M471KU54N 3L 7UDJ4 0LV45N1.
4N3LKUL H0GY G0ND0LK0DN0D K3LL3N3 R4J74.
L3GY BU5ZK3! C54K K3V35 3MB3R K3P35 3L0LV45N1 3Z7.
H4 7375Z377, 05ZD M3G M450KK4L 15!
"""

UZENET = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def listaszorzat(li):
    szorzat = 1
    for iter in li:
        szorzat *= iter
    return szorzat


def szovegfeld(szoveg):
    betuk = ["O", "I", "", "E", "A", "S", "", "T"]
    result = ""
    for item in szoveg:
        if item in "013457":
            result += betuk[int(item)]
        else:
            result += item
    return result


def palindromiter(szoveg):
    result = ""
    for item in szoveg:
        result = item + result
    return szoveg == result


def palindromrek(szoveg):
    if len(szoveg) <= 1:
        return True
    if szoveg[0] != szoveg[-1]:
        return False
    return palindromrek(szoveg[1:-1])


def valami():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp in ["y", "Y", "yes"]:  # <- egyszerűbben?
        print('bye')
        # sys.exit(0)
    # for any other input:
    print('The show goes on...')


def stringtisztazas(szoveg):
    whitespaces = [" ", "\t", "\v", "\n", "\r", "\f"]
    for item in whitespaces:
        szoveg = szoveg.replace(item, "")
    return szoveg


def rejtelyesuzenet(szoveg):
    '''abc = "abcdefghijklmnopqrstuvwxyz"
    Abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for item in szoveg:

        if item in abc:
            betuindex = abc.index(item) + 2
            if betuindex >= len(abc):
                betuindex -= len(abc)
            result += abc[betuindex]

        elif item in Abc:
            betuindex = Abc.index(item) + 2
            if betuindex >= len(Abc):
                betuindex -= len(Abc)
            result += Abc[betuindex]

        else:
            result += item'''

    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Abc = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"

    result = ""

    for i in UZENET:
        if i in abc:
            result += Abc[abc.find(i)]
        else:
            result += i

    return result


def main():
    # print(listaszorzat([1,2,3,4,5]))
    # print(szovegfeld(TEXT))
    # print(palindromrek(""))
    # print(stringtisztazas("206.130.99.82:\n8080"))
    print(rejtelyesuzenet(UZENET))


if __name__ == "__main__":
    main()
