def steps(number):
    count = 0
    n = number
    if n > 0:
        while n!=1:
            if n%2 == 0:
                n/=2
                count+=1
            else:
                n = (n*3)+1
                count+=1
    else:
        raise ValueError("Only positive integers are allowed")

    return count
