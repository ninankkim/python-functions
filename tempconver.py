temperature = []
while True:
    action  = input('Would you like to convert to?\n(C TO F, F TO C, STOP)').upper()
    if action == "C TO F":
        celcius = int(input('Please enter the celcius temperature you would like to convert to fehrenheit: \n'))
        fehrenheit = (celcius * 9/5) + 32
        print ("The converted temperature is", fehrenheit)
    
    elif action == "F TO C":
        fehrenheit = int(input('Please enter the fehrenheit temperature you would like to convert to celcius: \n'))
        celcius = (fehrenheit - 32) * 5/9
        print ("The converted temperature is", celcius)
    elif action == 'STOP':
        print ('The program will be stopped.')
        break

def temperature (tempC)
    F = (tempC * 9/5) + 32
    print (f'The converted temperature is {F}.')
    return F 

