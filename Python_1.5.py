def computepay(hours, rate, overtime, multiplier) :
    if hours > overtime :
        regularpay = rate * hours
        overtimepay = (hours - overtime) * (rate * (multiplier - 1.0))
        pay = regularpay + overtimepay
    else:
        pay = hours * rate
    return pay    

hours = input('Enter your weekly hours:')
overtime = input('Enter the number of hours before overtime kicks in:')
multiplier = input('Enter the multiplier for pay on your overtime hours:')
rate = input('Enter your hourly rate:')

try:
    flovertime = float(overtime)
    flmultiplier = float(multiplier)
    flhours = float(hours)
    flrate = float(rate)
except:
    print("Error, please enter numeric input!")
    quit()

finalpay = computepay(flhours, flrate, flovertime, flmultiplier)

print('Pay:', finalpay)