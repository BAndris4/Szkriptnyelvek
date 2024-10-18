def kiralynok(li):
    print("+-----------------+")
    for i in range(7, -1, -1):
        kiralynopoz = li.index(i)
        print("| ", end="")
        for i in range(kiralynopoz):
            print(". ", end="")
        print("Q ", end="")
        for i in range(7 - kiralynopoz):
            print(". ", end="")
        print("|")
    print("+-----------------+")


def main():
    kiralynok([7, 3, 0, 2, 5, 1, 6, 4])
    kiralynok([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == "__main__":
    main()
