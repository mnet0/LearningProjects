hours = input('Enter your hours:')
rate = input('Enter your rate:')

flhours = float(hours)
flrate = float(rate)

if flhours > 40 :
    print('Overtime')
    regularpay = flrate * flhours
    overtimepay = (flhours - 40.0) * (flrate * 0.5)
    pay = regularpay + overtimepay
else:
    print('Regular')
    pay = flhours * flrate

print('Pay:', pay)