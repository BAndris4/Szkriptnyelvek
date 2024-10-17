#!/usr/bin/env python3


def listaszorzat(li):
    result = 1
    for num in li:
        result *= num
    return result


def main():
    szum = 90
    szorzat = 996300
    for n1 in range(1, 46):
        for n2 in range(n1 + 1, 46):
            for n3 in range(n2 + 1, 46):
                for n4 in range(n3 + 1, 46):
                    for n5 in range(n4 + 1, 46):
                        for n6 in range(n5 + 1, 46):
                            numbers = [n1, n2, n3, n4, n5, n6]
                            if (
                                sum(numbers) == szum
                                and listaszorzat(numbers) == szorzat
                            ):
                                print(numbers)


"#################################################################################"

if __name__ == "__main__":
    main()
