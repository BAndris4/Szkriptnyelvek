def xor(str1, str2):
    return bool(str1) != bool(str2)


def main():
    print(xor("", None))
    print(xor("P", 0))
    print(xor(None, "x"))
    print(xor("X", "p"))
    return 0


if __name__ == "__main__":
    main()
