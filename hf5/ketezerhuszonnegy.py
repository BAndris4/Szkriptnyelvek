def str2024():
    """A függvény visszaadja 2024-et úgy, hogy a forráskódban nem használ semmilyen számot"""

    abc = [chr(i) for i in range(ord("a"), ord("{"))]
    return (
        str(abc.index("c"))
        + str(abc.index("a"))
        + str(abc.index("c"))
        + str(abc.index("e"))
    )


if __name__ == "__main__":
    print(str2024())
