print(' *** Wind classification ***')
wind_speed = float(input('Enter wind speed (km/h) : '))
print('Wind classification is ', end='')
if(209<=wind_speed):
    print('Super Typhoon.')
elif(wind_speed<209 and wind_speed>=102):
    print('Typhoon.')
elif(wind_speed<102 and wind_speed>=56):
    print('Tropical Storm.')
elif(wind_speed<56 and wind_speed>=52):
    print('Depression.')
else:
    print('Breeze.')
    