#Exercise 3.2

try:
        hours = float(raw_input('Enter Hours: '))
        rate = float(raw_input('Enter Rate: '))
        if hours > 40:
            pay = 1.5*rate*hours
        else:
            pay = rate*hours
        print('Pay:'+str(pay))
except:
        print('Please enter a number')
