# Creating variables
num = None
Totalnum = 0
i = 0

# Main loop
while num != "done":
    num = input("Enter a number:")
    try:
        intnum = int(num)
        Totalnum = Totalnum + intnum
        i = i + 1
    except:
        print("bad data")
# Averaging
flaverage = Totalnum / i

# Printing Total, Number of inputs and Average!
print(Totalnum, i, flaverage)
