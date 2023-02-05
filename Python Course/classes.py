# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User_hd:

    # Constructor
    def __init__(self, name, email, age):
        self.name_hd = name
        self.email_hd = email
        self.age_hd = age

        # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
        self._private_hd = 1000  # Encapsulated variables are declares with '_' in the constructor.

    def greeting_hd(self):
        return f'My name is {self.name_hd} and I am {self.age_hd}'

    def has_birthday_hd(self):
        self.age_hd += 1

    # function for encap variable
    def print_encap_hd(self):
        print(self._private_hd)


# Extend class
class Customer_hd(User_hd):
    # Constructor
    def __init__(self, name, email, age):
        User_hd.__init__(self, name, email,
                         age)  # Called proper parent class constructor to make this as proper child inehriting all methods.
        self.name_hd = name
        self.email_hd = email
        self.age_hd = age
        self.balance_hd = 0

    def set_balance_hd(self, balance):
        self.balance_hd = balance

    def greeting_hd(self):
        return f'My name is {self.name_hd} and I am {self.age_hd} and my balance is {self.balance_hd}'


#  Init user object
hamze = User_hd('Hamze Ahmed', '210201929@ostimteknik.edu.tr', 21)
# Init customer object
jenna = Customer_hd('Jenna Smith', 'jennasmith23@email.com', 32)

jenna.set_balance_hd(500)
print(jenna.greeting_hd())

hamze.has_birthday_hd()
print(hamze.greeting_hd())

# Encapsulation -->
hamze.print_encap_hd()
hamze._private_hd = 800  # Changing for brad
hamze.print_encap_hd()

# Method inherited from parent
jenna.print_encap_hd()  # Changing the variable for brad doesn't affect janets variable --> Encapsulation
jenna._private_hd = 600
jenna.print_encap_hd()

# Similary changing janet's doesn't affect brad's variable.
hamze.print_encap_hd()
