print("Enter a number: ")
number = int(input("Enter any number of your choice:- "))
number_entered = number
fac = 1

if number == 0:
    result = 1
else:
    while number >= 1:
        fac = fac * number
        number = number -1
    result = fac
print('The factorial of {} is {}'.format(number_entered, result),'.')