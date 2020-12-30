fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'intro.txt'
handle = open(fname)

# punctuation = {',', '.', ':', '!', '?', '(', ')'}
di = dict()

for line in handle:
    line = line.replace(',','')
    line = line.replace('.','')
    line = line.replace(':','')
    line = line.replace('!','')
    line = line.replace('?','')
    line = line.replace('(','')
    line = line.replace(')','')
    line = line.rstrip()
    line = line.lower()
    words = line.split()
    for word in words:       
        di[word] = di.get(word,0) + 1

largest = -1
theword = None
for w,v in di.items() :
    print(w, v)
    if v > largest :
        largest = v
        theword = w

print('Done',theword, largest)