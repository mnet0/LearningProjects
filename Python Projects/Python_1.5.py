def computepay(hours, rate) :
    if hours > 40 :
        regularpay = rate * hours
        overtimepay = (hours - 40.0) * (rate * 0.5)
        pay = regularpay + overtimepay
    else:
        pay = hours * rate
    return pay    

hours = input('Enter your weekly hours:')
overtime = input('Enter the number of hours before overtime kicks in:')
multiplier = input('Enter the multiplier for pay in overtime hours:')
rate = input('Enter your hourly rate:')

try:
    flhours = float(hours)
    flrate = float(rate)
except:
    print("Error, please enter numeric input!")
    quit()

finalpay = computepay(flhours, flrate)

print('Pay:', finalpay)