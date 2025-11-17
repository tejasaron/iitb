def equilateral(sides):
    a, b, c = sides
    
    for side in sides :
        if side > 0:
            return a == b == c 
        else:
            return False


def isosceles(sides):
    a, b, c = sides
    for side in sides :
        if side > 0:
            if a+b>= c and b+c >= a and a+c>=b:
                return a == b or b == c or c == a
            else:
                return False
        else:
            return False

def scalene(sides):
    a, b, c = sides
    for side in sides :
        if side > 0:
            if a+b>= c and b+c >= a and a+c>=b:
                return a != b and b != c and a != c
            else:
                return False
        else:
            return False
     