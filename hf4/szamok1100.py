def szamjegyekosszege():
    szum = 0
    for i in range(1,101):
        li = list(str(i))
        for j in li:
            szum += int(j)
    return szum

def main():
    print((1+100)//2*100) #5050
    print(szamjegyekosszege()) #901

if __name__ == "__main__":
    main()