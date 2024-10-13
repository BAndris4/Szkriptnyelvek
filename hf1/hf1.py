def main():
    #Bekér a felhasználótól egy váltózóba egy nevet, azután meg egy számot. A program a szót pozicionálja a megadott számosságú szóköz
    #karakter közé. Például ha a név Laci, a szám pedig 6, akkor " Laci " lesz a végeredmény.
    nev = input("Add meg a neved!\n")
    db = int(input("Adj meg egy számot!\n"))
    print(nev.center(db))

if __name__ == "__main__":
    main()