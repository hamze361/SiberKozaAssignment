# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello_hd(name_hd='Hamze'):
    print(f'Hello {name_hd}')


# Return values
def getSum_hd(num1_hd, num2_hd):
    total_hd = num1_hd + num2_hd
    return total_hd


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum_hd = lambda num1_hd, num2_hd: num1_hd + num2_hd

print(getSum_hd(11, 4))
