def is_valid(isbn):
    s = isbn.replace('-','').strip()
    if len(s) != 10:
        return False

    total = 0
    for i,ch in enumerate(s):
        weight = 10-i

        if ch == 'X':
            if i != 9:
                return False
            value = 10
        elif ch.isdigit():
            value = int(ch)
        else:
            return False

        total += value * weight

    return total % 11 == 0
    