# Identifiers => All those names which are given by the user while coding are the identifiers.
# For example => variables, function name, class name, module name

# Rules for naming identifiers
# 1. It is case sensitive
a = 1
A = 2

# 2. Identifiers can't be keywords
# 3. Identifiers can't contain special symbols (@, #, $, %, ^)
# a@ = 1

# 4. Identifiers can contain digits but they can't start with a digit

a1 = 20  # Valid
# 1a = 22  # Invalid

# 5. _ is valid in identifier naming

_a = 1
a_ = 1
_ = 2
__ = 2



# Python statement
# 1. Generally a single line is a single python statement
# 2. But sometimes a statement can go to multiple lines and multiple statements can occur in a same line

a ="Hello World. I'm learning " \
   "python"
print(a)

a = 2; b = 3



# Writing a block of code in Python

x = 5
# if(x == 5){
# printf("")
# }

if x == 5:
    print("The number is 5")

# Identation is used to determine a block of code in Python. It is necessary for condition block, loops,
# exceptions

a = """
Hello World.
I'm Learning Python

"""

print(a)


def addition(a, b):
    """
    This is a function two sum two numbers
    """
    return a + b

a = "I'm learning Python"
# b = 'I'm learnng Python'