def rabin_karp_algorithm(text, pattern):
    x = 256
    p = 1000000007
    text_len = len(text)
    pattern_len = len(pattern)
    h = pow(x, pattern_len-1) % p
    pattern_hash = 0
    text_hash = 0
    result = ''

    for i in range(pattern_len):
        pattern_hash = (x * pattern_hash + ord(pattern[i])) % p
        text_hash = (x * text_hash + ord(text[i])) % p

    for seq in range(text_len-pattern_len+1):
        if pattern_hash == text_hash and pattern[i] == text[seq+pattern_len-1]:
            result += str(seq)
            result += ' '
        if seq < text_len-pattern_len:
            text_hash = (text_hash - h * ord(text[seq])) % p
            text_hash = (text_hash * x + ord(text[seq+pattern_len])) % p
            text_hash = (text_hash + p) % p

    return result


def find():
    pattern = input()
    text = input()
    return rabin_karp_algorithm(text, pattern).strip()


if __name__ == '__main__':
    find()
