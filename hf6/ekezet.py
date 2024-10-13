TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""


def main():
    d = {"á": "a", "Á": "A", "í": "i", "Í": "I", "é": "e", "É": "E", "ú": "u", "Ú": "U", "Ü": "U", "ü": "u", "Ű": "U",
         "ű": "u", "ó": "o", "Ó": "O", "Ö": "O", "ö": "o", "Ő": "O", "ő": "o"}

    new_text = ""
    for char in TEXT:
        if char in d:
            new_text += d[char]
        else:
            new_text += char
    print(new_text)


if __name__ == '__main__':
    main()
