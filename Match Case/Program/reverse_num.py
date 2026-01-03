number = 123456

reversed_number = 0

while number != 0:
    digits = number % 10
    reversed_number = reversed_number *10 + digits
    number //= 10

print(reversed_number)  
