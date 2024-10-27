INCH_TO_CM_RATIO = 2.54

# Covert inch and cm
print('Welcome to Inch CM Converter')
check_valid_input = True
while check_valid_input:
    input_value = input('Please enter the value of inch: ')
    inch_input = float(input_value)
    check_valid_input = inch_input < 0
    if not check_valid_input:
        cm_result = inch_input * INCH_TO_CM_RATIO
        print(f'{inch_input} inch = {cm_result} cm')
    else:
        print('Please enter a positive value')


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







