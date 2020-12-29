str = 'X-DSPAM-Confidence: 0.8475 '

position = str.find(':')
# print(position)
piece = str[position + 2:]
# print(piece)
value = float(piece)
print(value)