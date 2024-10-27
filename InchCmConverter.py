# Covert inch and cm
print('Welcome to Inch CM Converter')
inch_input = float(input('Please enter the value of inch: '))
while True:
    if inch_input < 0:
        print('Please enter a positive value')
        inch_input = float(input('Please enter the value of inch: '))
    else:
        cm_result = inch_input * 2.54
        print(f'{inch_input} inch = {cm_result} cm')
        break




# def inch_cm_converter():
#     while True:
#         try:
#             print('Welcome to Inch CM Converter')
#             inch_input = float(input('Please enter the value of inch: '))
#             cm_result = inch_input * 2.54
#             print(f'{inch_input} inch = {cm_result} cm')
#         except ValueError:
#             print('Please enter a valid number.')
# inch_cm_converter()







