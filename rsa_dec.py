from decimal import Decimal


def convert(txt):
    if (txt == "A"):
        k = 1
    elif (txt == "B"):
        k = 2
    elif (txt == "C"):
        k = 3
    elif (txt == "D"):
        k = 4
    elif (txt == "E"):
        k = 5
    elif (txt == "F"):
        k = 6
    elif (txt == "G"):
        k = 7
    elif (txt == "H"):
        k = 8
    elif (txt == "I"):
        k = 9
    elif (txt == "J"):
        k = 10
    elif (txt == "K"):
        k = 11
    elif (txt == "L"):
        k = 12
    elif (txt == "M"):
        k = 13
    elif (txt == "N"):
        k = 14
    elif (txt == "O"):
        k = 15
    elif (txt == "P"):
        k = 16
    elif (txt == "Q"):
        k = 17
    elif (txt == "R"):
        k = 18
    elif (txt == "S"):
        k = 19
    elif (txt == "T"):
        k = 20
    elif (txt == "U"):
        k = 21
    elif (txt == "V"):
        k = 22
    elif (txt == "W"):
        k = 23
    elif (txt == "X"):
        k = 24
    elif (txt == "Y"):
        k = 25
    elif (txt == "Z"):
        k = 26
    elif (txt == "a"):
        k = 27
    elif (txt == "b"):
        k = 28
    elif (txt == "c"):
        k = 29
    elif (txt == "d"):
        k = 30
    elif (txt == "e"):
        k = 31
    elif (txt == "f"):
        k = 32
    elif (txt == "g"):
        k = 33
    elif (txt == "h"):
        k = 34
    elif (txt == "i"):
        k = 35
    elif (txt == "j"):
        k = 36
    elif (txt == "k"):
        k = 37
    elif (txt == "l"):
        k = 38
    elif (txt == "m"):
        k = 39
    elif (txt == "n"):
        k = 40
    elif (txt == "o"):
        k = 41
    elif (txt == "p"):
        k = 42
    elif (txt == "q"):
        k = 43
    elif (txt == "r"):
        k = 44
    elif (txt == "s"):
        k = 45
    elif (txt == "t"):
        k = 46
    elif (txt == "u"):
        k = 47
    elif (txt == "v"):
        k = 48
    elif (txt == "w"):
        k = 49
    elif (txt == "x"):
        k = 50
    elif (txt == "y"):
        k = 51
    elif (txt == "z"):
        k = 52
    elif (txt == "0"):
        k = 53
    elif (txt == "1"):
        k = 54
    elif (txt == "2"):
        k = 55
    elif (txt == "3"):
        k = 56
    elif (txt == "4"):
        k = 57
    elif (txt == "5"):
        k = 58
    elif (txt == "6"):
        k = 59
    elif (txt == "7"):
        k = 60
    elif (txt == "8"):
        k = 61
    elif (txt == "9"):
        k = 62
    elif (txt == "!"):
        k = 63
    elif (txt == "@"):
        k = 64
    elif (txt == "#"):
        k = 65
    elif (txt == "$"):
        k = 66
    elif (txt == "%"):
        k = 67
    elif (txt == "^"):
        k = 68
    elif (txt == "&"):
        k = 69
    elif (txt == "*"):
        k = 70
    elif (txt == "("):
        k = 71
    elif (txt == ")"):
        k = 72
    elif (txt == "-"):
        k = 73
    elif (txt == "+"):
        k = 74
    elif (txt == "/"):
        k = 75
    else:
        k = "hash"

    return k


def revconvert(num):
    if (num == 1):
        k = "A"
    elif (num == 2):
        k = "B"
    elif (num == 3):
        k = "C"
    elif (num == 4):
        k = "D"
    elif (num == 5):
        k = "E"
    elif (num == 6):
        k = "F"
    elif (num == 7):
        k = "G"
    elif (num == 8):
        k = "H"
    elif (num == 9):
        k = "I"
    elif (num == 10):
        k = "J"
    elif (num == 11):
        k = "K"
    elif (num == 12):
        k = "L"
    elif (num == 13):
        k = "M"
    elif (num == 14):
        k = "N"
    elif (num == 15):
        k = "O"
    elif (num == 16):
        k = "P"
    elif (num == 17):
        k = "Q"
    elif (num == 18):
        k = "R"
    elif (num == 19):
        k = "S"
    elif (num == 20):
        k = "T"
    elif (num == 21):
        k = "U"
    elif (num == 22):
        k = "V"
    elif (num == 23):
        k = "W"
    elif (num == 24):
        k = "X"
    elif (num == 25):
        k = "Y"
    elif (num == 26):
        k = "Z"
    elif (num == 27):
        k = "a"
    elif (num == 28):
        k = "b"
    elif (num == 29):
        k = "c"
    elif (num == 30):
        k = "d"
    elif (num == 31):
        k = "e"
    elif (num == 32):
        k = "f"
    elif (num == 33):
        k = "g"
    elif (num == 34):
        k = "h"
    elif (num == 35):
        k = "i"
    elif (num == 36):
        k = "j"
    elif (num == 37):
        k = "k"
    elif (num == 38):
        k = "l"
    elif (num == 39):
        k = "m"
    elif (num == 40):
        k = "n"
    elif (num == 41):
        k = "o"
    elif (num == 42):
        k = "p"
    elif (num == 43):
        k = "q"
    elif (num == 44):
        k = "r"
    elif (num == 45):
        k = "s"
    elif (num == 46):
        k = "t"
    elif (num == 47):
        k = "u"
    elif (num == 48):
        k = "v"
    elif (num == 49):
        k = "w"
    elif (num == 50):
        k = "x"
    elif (num == 51):
        k = "y"
    elif (num == 52):
        k = "z"
    elif (num == 53):
        k = "0"
    elif (num == 54):
        k = "1"
    elif (num == 55):
        k = "2"
    elif (num == 56):
        k = "3"
    elif (num == 57):
        k = "4"
    elif (num == 58):
        k = "5"
    elif (num == 59):
        k = "6"
    elif (num == 60):
        k = "7"
    elif (num == 61):
        k = "8"
    elif (num == 62):
        k = "9"
    elif (num == 63):
        k = "!"
    elif (num == 64):
        k = "@"
    elif (num == 65):
        k = "#"
    elif (num == 66):
        k = "$"
    elif (num == 67):
        k = "%"
    elif (num == 68):
        k = "^"
    elif (num == 69):
        k = "&"
    elif (num == 70):
        k = "*"
    elif (num == 71):
        k = "("
    elif (num == 72):
        k = ")"
    elif (num == 73):
        k = "-"
    elif (num == 74):
        k = "+"
    elif (num == 75):
        k = "/"
    else:
        k = "Honey"
    return k
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def rsa_dec(p,q):
    n = p * q

    k10 = ""
    k20 = ""
    li = []
    file=open("sample2.txt","r")
    s=file.read()
    #s=int(s)
    ct12=list(map(int,s.split()))
    print(ct12)
    l = len(ct12)
    s1 = set(ct12)
    ct = list(s1)
    print(ct)
    l1 = len(ct)

    for i in range(0, len(ct)):
        t = (p - 1) * (q - 1)
        e = 7
        for j in range(1, 10):
            x = 1 + j * t
            if x % e == 0:
                d = int(x / e)
                break
        dtt = 0

        dtt = pow(ct[i], d)
        dt = dtt % n

        li.append(dt)


    for i in range(l):
        for j in range(l1):
            if (ct12[i] == ct[j]):
                ct12[i] = li[j]
                break

        k2 = revconvert(ct12[i])
        k20 = k20 + k2

    file = open("s10.txt", "w")
    file.write(k20)

