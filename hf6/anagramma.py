def normalize(word):
    return "".join(word.lower().split())


def isanagram1(word1, word2):
    word1, word2 = normalize(word1), normalize(word2)
    d1, d2 = {}, {}
    for char in word1:
        d1[char] = d1.get(char, 0) + 1
    for char in word2:
        d2[char] = d2.get(char, 0) + 1
    if d1 == d2:
        return True
    return False


def isanagram2(word1, word2):
    word1, word2 = normalize(word1), normalize(word2)
    chars = list(word1)
    for char in word2:
        if char in chars:
            chars.remove(char)
        else:
            return False
    return True


def main():
    print(isanagram2("listen", "silent"))
    print(isanagram2("A gentleman", "Elegant man"))
    print(isanagram2("Clint Eastwood", "Old west action"))
    print(isanagram2("dormitory", "dirty room"))

    print(isanagram2("alma", "banan"))


if __name__ == '__main__':
    main()
