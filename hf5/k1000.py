def kisebbmint1000():
    '''A függvény visszaadja azon 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek töbszörösei.'''

    return sum([num for num in range(1,1000) if num % 3 == 0 or num % 5 == 0])


if __name__ == "__main__":
    print(kisebbmint1000())