#!/usr/bin/env python3

def main():
    #1
    elems = ["auto", "villamos", "metro"]
    result = [s.upper()+"!" for s in elems]
    print(result)
    #2
    elems = ["aladar", "bela", "cecil"]
    result = [s.capitalize() for s in elems]
    print(result)
    #3
    result = [0 for i in range(10)]
    print(result)
    #4
    elems = [i for i in range(1,11)]
    result = [i*2 for i in elems]
    print(result)
    #5
    elems = [str(i) for i in range(1,11)]
    result = [int(s) for s in elems]
    print(result)
    #6
    elem = "1234567"
    result = [int(i) for i in elem]
    print(result)
    #7
    elem = "The quick brown fox jumps over the lazy dog"
    result = [len(word) for word in elem.split()]
    print(result)
    #8
    elem = "python is an awesome language"
    result = [word[0] for word in elem.split()]
    print(result)
    #9
    elem = "The quick brown fox jumps over the lazy dog"
    result = [(word, len(word)) for word in elem.split()]
    print(result)
    #10
    result = [i for i in range(10) if i%2 == 0]
    print(result)
    #11
    result = [i*i for i in range(20) if (i*i)%2 == 0]
    print(result)
    #12
    result = [i*i for i in range(20) if str(i*i)[-1]=="4"]
    print(result)
    #13
    result = "".join([chr(i) for i in range(65,91)]) 
    print(result)
    #14
    elems = [' apple ', ' banana ', ' kiwi']
    result = [word.strip() for word in elems]
    print(result)
    #15
    elems = [1, 0, 1, 1, 0, 1, 0, 0]
    result = "".join(str(d) for d in elems)
    print(result)



    return 0


if __name__ == "__main__":
    main()