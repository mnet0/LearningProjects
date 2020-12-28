def computepay(hours, rate) :
    if hours > 40 :
        regularpay = rate * hours
        overtimepay = (hours - 40.0) * (rate * 0.5)
        pay = regularpay + overtimepay
    else:
        pay = hours * rate
    return pay    

hours = input('Enter your hours:')
rate = input('Enter your rate:')

try:
    flhours = float(hours)
    flrate = float(rate)
except:
    print("Error, please enter numeric input!")
    quit()

finalpay = computepay(flhours, flrate)

print('Pay:', finalpay)