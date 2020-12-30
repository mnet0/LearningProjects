hours = input('Enter your hours:')
rate = input('Enter your rate:')

try:
    flhours = float(hours)
    flrate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if flhours > 40 :
    # print('Overtime')
    regularpay = flrate * flhours
    overtimepay = (flhours - 40.0) * (flrate * 0.5)
    pay = regularpay + overtimepay
else:
    # print('Regular')
    pay = flhours * flrate

print('Pay:', pay)