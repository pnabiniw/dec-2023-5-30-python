# Operators are the special symbols to perform operations in Python (or in any programming language)
# Python also has its set of operators

# 1. Arithmetic Operators
# 2. Logical Operators
# 3. Relational / Comparison Operators
# 4. Membership Operators
# 5. Identity Operators
# 6. Assignment Operators


# 1. Arithmetic (+, -, /, *, %, //, **)

# Modulous Operator => Remainder of the division operation


a = 5
b = 2
print(a % b)  # 1



# Floor Division (//)

a = 5
print(a // 2)  # 2


# Exponent operator (**)

a = 5
print(a ** 2)  # 25



# 2. Comparison Operators (>, <, >=, <=, ==, !=)
# The result of comparison operation is either True or False

a = 5
b = 2
c = 5
print(a > b)  # True
print(a == c)  # True
print(a != b)  # True


# Logical Operators (and, or, not)
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(False and True)  # False

print(True or True)  # True
print(True and False)  # True
print(False and False)  # False
print(False and True)  # True

print(not True)  # False
print(not False)  # True


a = 5  # (non-zero is a truthy value)
print(not a)  # False

b = 0  # (falsy)
print(not b)  # True



# Membership Operator ("in" and "not in")
# Result of membership check is also in True and False

print(2 in [1, 2, 3, 4])  # True
print(2 not in [1, 2, 3, 4])  # False
print('k' in 'kathmandu')  # True


# Identity Operator ('is' and 'is not')
a = 1
b = 1
print(a ==  b)  # True
print(a is b)  # True. value of a and b are in the same memory location


a = []
b = []
print(a is b)  # False. Here a and b are two different objects


# Assignment Operator (=, +=, -=, /= ...)
a = 5
a = a + 1
a += 1



# Precedence and Associativity
# Precedence is the rule which defines which operation to execute first


a = 2 + 5 / 5  # precedence of / is greater than +
print(a)

# If two operators have the same precedence then associativity is taken into consideration
# Associativity in Python always goes from left to right
a = 2 * 3 / 3  # 2

# But the only exception is ** operator

a = 3 ** 2 ** 2
print(a)  # 81