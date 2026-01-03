number = 123

digits_list = []


while number > 0:
    last_digit = number % 10
    digits_list.append(last_digit)
    number //=10

digits_list.reverse()

for i in digits_list:
    print(i)
 