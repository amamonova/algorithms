def phonebook():
    contacts = {}
    res = ''
    n = int(input())
    for i in range(n):
        inp = input().split()
        if inp[0] == 'add':
            if inp[1] in contacts:
                del contacts[inp[1]]
            contacts[inp[1]] = inp[2]
        elif inp[0] == 'find':
            if res:
                res += '\n'
            if inp[1] in contacts:
                res += contacts[inp[1]]
            else:
                res += 'not found'
        elif inp[0] == 'del':
            if inp[1] in contacts:
                del contacts[inp[1]]
    return res


if __name__ == '__main__':
    print(phonebook())
