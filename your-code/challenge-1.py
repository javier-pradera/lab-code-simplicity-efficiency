"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!\nIt can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

#We first create two dictionaries that relate each number to a string
numbers = [0,1,2,3,4,5,6,7,8,9,10]
strings = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
str_to_num = dict(zip(strings,numbers))
num_to_str = dict(zip(numbers,strings))

#We then compute the calculation and print the result:
valid_numbers = strings[:6]
if (a in valid_numbers and c in valid_numbers) and (b == 'plus' or b == 'minus'):
    a_num, c_num = str_to_num[a], str_to_num[c]
    result = (lambda x,y,z: x + z if y == 'plus' else x - z)(a_num,b,c_num)
    if result >= 0:
        result_str = num_to_str[result]
        print(a,b,c,'equals',result_str)
    else:
        result_str = num_to_str[-result]
        print(a,b,c,'equals negative',result_str)
else:
    print("I am not able to answer this question. Check your input.")

print("Thanks for using this calculator, goodbye :)")
