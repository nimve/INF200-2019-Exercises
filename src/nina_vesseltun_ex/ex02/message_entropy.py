from math import log2


def letter_freq(txt):
    txt = txt.lower()
    found_letters = {}
    for sign in txt:
        if sign in found_letters:
            found_letters[sign] += 1
        if sign not in found_letters:
            found_letters[sign] = 1
    return found_letters


def entropy(message):
    n = len(message)
    letters = letter_freq(message)
    msg_entropy = 0
    for i in letters:
        p_i = letters[i] / n
        msg_entropy += p_i * log2(p_i)
    return -msg_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
