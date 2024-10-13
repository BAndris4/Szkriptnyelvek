import os

pythonalap = ''' #!/usr/bin/env python3


def main():
    print('Py3')

##############################################################################

if __name__ == "__main__":
    main()
'''

def main():
    szoveg = '''---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C      [c]
q) quit'''

    option = ""
    while option != "q":
        print(szoveg)
        option = input()
        if option == "1":
            if os.path.isfile("alap.py"):
                print("Már létezik ilyen file!")
            else:
                f = open("alap.py", "w")
                f.write(pythonalap)
                f.close()
        elif option == "2":
            if os.path.isfile("alap.c"):
                print("Már létezik ilyen file!")
            else:
                f = open("alap.c", "w")
                f.close()

if __name__ == "__main__":
    main()