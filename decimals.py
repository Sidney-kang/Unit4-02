# Created by : Sidney Kang
# Created on : 28 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit4-02
# This program accepts decimal numbers and lets user choose how many decimal
#   places they want to round

def decimal(user_input, user_power):
    user_input = long(user_input * (10 ** user_power) + 0.5) / (10 ** user_power)
    print(str(user_input))
    
user_input = raw_input("Type any decimal number: ")
user_input = float(user_input)
user_power = raw_input("Type how many decimal places you want to round the number: ")
user_power = float(user_power)
decimal(user_input, user_power)
