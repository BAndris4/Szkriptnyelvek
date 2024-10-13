def magasmely(text):
    melybetuk = "aáuúoó"
    magasbetuk = "eéiíüűöő"

    mely, magas = False, False
    for i in text:
        if i in melybetuk:
            mely = True
        elif i in magasbetuk:
            magas = True
        if magas and mely:
            return "vegyes"
    
    if magas:
        return "magas"
    elif mely:
        return "mély"
    else:
        return "semmilyen" 

def main():
    print(magasmely("ablak"))
    print(magasmely("erkély"))
    print(magasmely("kisvasút"))
    print(magasmely("magas"))
    print(magasmely("mély"))
    print(magasmely("Pffffff"))


    return 0

if __name__ == "__main__":
    main()