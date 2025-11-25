def response(utterance):
    if utterance is None:
        utterance = ""

    raw = utterance
    stripped = raw.strip()

    # Silence
    if stripped == "":
        return "Fine. Be that way!"

    # Detect question
    is_question = stripped.endswith("?")

    # Detect yelling (must have at least one letter AND all letters uppercase)
    has_letter = False
    all_alpha_upper = True

    for ch in stripped:
        if ch.isalpha():
            has_letter = True
            if not ch.isupper():
                all_alpha_upper = False

    is_yelling = has_letter and all_alpha_upper

    # Decision logic
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."

