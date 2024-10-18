#!/usr/bin/env python3

import requests

corpuslink = (
    "https://raw.githubusercontent.com/jabbalaci/Programozas_1/main/datasets/DT2.csv"
)


def matching_words(li):
    words = []
    for word in li:
        jhely = word.find("j")
        shely = word.find("s")
        uhely = word.find("u")
        nhely = word.find("n")
        if (
            jhely != -1
            and shely != -1
            and uhely != -1
            and nhely != -1
            and jhely < shely < uhely < nhely
        ):
            words.append(word)
    return words


def main():
    corpus = requests.get(corpuslink).text
    corpuslist = []
    for word in corpus.split():
        corpuslist.append(word.split(",")[0])

    words = matching_words(corpuslist)
    if words:
        print(f"A magyar nyelvben vannak ilyen szavak: \n{"\n".join(words)}")
    else:
        print("Sajnos nincsenek ilyen szavak!")


"#################################################################################"

if __name__ == "__main__":
    main()
