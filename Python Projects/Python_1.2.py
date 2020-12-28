hours = input('Enter your hours:')
rate = input('Enter your rate:')

flhours = float(hours)
flrate = float(rate)

if flhours > 40 :
    print('Overtime')
else:
    print('Regular')
pay = flhours * flrate
print('Pay:', pay)