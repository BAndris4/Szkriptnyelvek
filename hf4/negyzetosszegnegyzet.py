def main():
    szum1, szum2 = 0, 0

    for i in range(1,101):
        szum1 += i**2
        szum2 += i
    szum2 **= 2

    print(szum2-szum1)
    return 0

if __name__ == "__main__":
    main()