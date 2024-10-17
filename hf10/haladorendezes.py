#!/usr/bin/env python3


def f1key(t):
    return t[-1]


def f2key(s):
    return int(s.split(":")[0])


def f3key(li):
    return li[1]


def f1():
    data = [
        (1, "Albany", "NY", 162692),
        (121, "Wyoming", "NY", 8722),
        (3, "Allegany", "NY", 11986),
        (123, "Yates", "NY", 5094),
    ]
    print(sorted(data, key=f1key))


def f2():
    users = ["10:User1", "80:User2", "100:User3", "00:User4", "75:User4", "45:User5"]
    for user in sorted(users, key=f2key, reverse=True):
        print(user)


def f3():
    matrix = [[2, 6], [1, 3], [5, 4]]
    print(sorted(matrix, key=f3key))


def main():
    f1()
    f2()
    f3()


"#################################################################################"

if __name__ == "__main__":
    main()
