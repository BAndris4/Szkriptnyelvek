import math


def distance(p1, p2):
    x1, x2, y1, y2 = p1[0], p1[1], p2[0], p1[1]
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print("A ket pont kozti tavolsag:", distance(p1, p2))


#############################################################################

if __name__ == "__main__":
    main()
