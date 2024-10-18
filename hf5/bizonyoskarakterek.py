def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """A függvény olyan stringgel tér vissza, mely a text paraméterből csak azokat a karaktereket tartalmazza, melyek szerepelnek az opcionális chars paraméterben."""
    result = ""
    for char in text:
        if char in chars:
            result += char
    return result


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
