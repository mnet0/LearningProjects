num = None
Totalnum = 0
i = 0

while num != "done":
    num = input("Enter a number:")
    try:
        intnum = int(num)
        Totalnum = Totalnum + intnum
        i = i + 1
    except:
        print("bad data")

flaverage = Totalnum / i

print(Totalnum, i, flaverage)
