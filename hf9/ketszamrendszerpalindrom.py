#!/usr/bin/env python3


def is_palindrom(num):
    num = str(num)
    reversed_num = str(num)[::-1]
    if num == reversed_num:
        return True
    return False


def toBinary(num):
    binary = ""
    while num:
        binary += str(num % 2)
        num //= 2
    return binary[::-1]


def main():
    result = 0
    for i in range(1000000):
        if is_palindrom(i) and is_palindrom(toBinary(i)):
            result += i
    print(result)


"#################################################################################"

if __name__ == "__main__":
    main()
