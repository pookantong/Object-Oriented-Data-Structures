print(' *** Wind classification ***')
wind_speed = float(input('Enter wind speed (km/h) : '))
if 209<=wind_speed:
    print('Wind classification is Super Typhoon.')
elif wind_speed<209 and wind_speed>=102:
    print('Wind classification is Typhoon.')
elif wind_speed<102 and wind_speed>=56:
    print('Wind classification is Tropical Storm.')
elif wind_speed<56 and wind_speed>=52:
    print('Wind classification is Depression.')
elif wind_speed<52 and wind_speed>=0:
    print('Wind classification is Breeze.')
else:
    print('!!!Wrong value can\'t classify.')