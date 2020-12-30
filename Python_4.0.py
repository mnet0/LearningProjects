fh = open("mbox-short.txt")

for line in fh:
    linestriped = line.rstrip()
    print(linestriped.upper())