def chain():
    result = ''
    table_size = int(input())
    hash_table = [[] for _ in range(table_size)]
    n = int(input())
    for i in range(n):
        inp = input().split()
        key = polynomial_hash_func(inp[1], table_size)
        if inp[0] == 'add':
            add(hash_table, inp[1], key)
        elif inp[0] == 'del':
            del_string(hash_table, key, inp[1])
        elif inp[0] == 'find':
            if result:
                result += '\n'
            result += find(hash_table, key, inp[1])
        elif inp[0] == 'check':
            if result:
                result += '\n'
            result += check(hash_table, int(inp[1]))
    return result


def polynomial_hash_func(seq, table_size):
    hash_sum = 0
    p = 1000000007
    x = 263
    for idx, ch in enumerate(seq):
        hash_sum += (ord(ch) * (x ** idx % p)) % p
    return (hash_sum % p) % table_size


def add(hash_table, seq, key):
    if seq not in hash_table[key]:
        hash_table[key].insert(0, seq)


def del_string(hash_table, key, seq):
    sub_arr = hash_table[key]
    if seq in sub_arr:
        sub_arr.remove(seq)


def find(hash_table, key, seq):
    if hash_table[key] and seq in hash_table[key]:
        return 'yes'
    else:
        return 'no'


def check(hash_table, i):
    if hash_table[i]:
        return ' '.join(hash_table[i])
    return ' '


if __name__ == '__main__':
    print(chain())
