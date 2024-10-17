#!/usr/bin/env python3


def is_prime(num):
    if num == 1 or num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def is_palindrom(num):
    num = str(num)
    reversed_num = str(num)[::-1]
    if num == reversed_num:
        return True
    return False


def test(num):
    while True:
        if is_palindrom(num) and is_prime(num):
            print(num)
            break
        num += 1


def main():
    test(31)
    test(130)
    test(131)
    test(1977)


"#################################################################################"

if __name__ == "__main__":
    main()
