def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 :
        raise ValueError('Classification is only possible for positive integers.')
    else:
        factors = [x for x in range(1,number) if number%x == 0 ]
        sum = 0
        div_sum = 0
        for x in factors:
            div_sum += x
        classi = (
            "perfect" if div_sum == number
            else "abundant" if div_sum > number
            else "deficient"
        )
    return classi
                
