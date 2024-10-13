def diamond(magassag):
    result = """"""
    if magassag % 2 == 0:
        print("Páratlant adj meg!")
    else:
        for i in range(magassag//2+1):
            text = "*"*(i*2+1)
            #print(text.center(magassag, " "))
            result += text.center(magassag, " ") + "\n"
        
        for i in range(magassag//2-1, -1, -1):
            text = "*"*(i*2+1)
            #print(text.center(magassag, " "))
            result += text.center(magassag, " ") + "\n"
    return result

def main():
    print(diamond(5))
    return 0

if __name__ == "__main__":
    main()