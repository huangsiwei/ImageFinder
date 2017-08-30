def count_alphabet(text):
    alphabet_count = 0
    for uchar in text:
        if ('\u0041' <= uchar <= '\u005a') or ('\u0061' <= uchar <= '\u007a'):
            alphabet_count += 1
        else:
            alphabet_count += 0
    return alphabet_count
