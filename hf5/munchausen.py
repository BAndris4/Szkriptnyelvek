# Előre számolt hatványok tárolása
squarenums = [pow(i, i) if i != 0 else 0 for i in range(10)]


def munchausenszam(num):
    result = 0
    num_str = str(num)

    for i in num_str:
        result += squarenums[int(i)]
        if result > num:
            return -1
    return result


def main():
    print("0 és 9999 közötti Münchausen-számok:")
    for i in range(10000):
        if munchausenszam(i) == i:
            print(i)

    limit = 440000000
    for i in range(limit):
        if i % 1000000 == 0:
            print(f"{i} szám feldolgozva...")
        if munchausenszam(i) == i:
            print(i)


if __name__ == '__main__':
    main()
