def is_armstrong_number(number):
    temp = number
    n_digits = 0
    total = 0

    while temp > 0:
        temp //= 10
        n_digits+=1

    temp = number
    digit = 0
    
    for i in range(1,n_digits+1):
        digit = temp % 10
        total += ((digit) ** n_digits)
        temp //= 10

    return total == number
