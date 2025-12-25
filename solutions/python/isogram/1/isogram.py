def is_isogram(string):
    word = [c.lower() for c in string if c.isalpha()]
    return len(word) == len(set(word))
