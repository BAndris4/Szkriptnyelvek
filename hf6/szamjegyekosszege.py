def szamjegyekosszege(num):
    numbers = str(num)
    result = 0
    for number in numbers:
        result += int(number)
    return result


def main():
    print(szamjegyekosszege(2**1000))

if __name__ == '__main__':
    main()