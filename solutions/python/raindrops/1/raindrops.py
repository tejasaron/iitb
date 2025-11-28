def convert(number):
    return_value = ""
    if number % 3 == 0:
        return_value += "Pling"
    if number % 5 == 0:
        return_value += "Plang"
    if number % 7 == 0:
        return_value += "Plong"

    if return_value == "":
        return_value = str(number)
    
    return return_value
