def rotate(text, key):
    result = []

    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            shifted = (ord(ch) - base + key) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(ch)

    return ''.join(result)

