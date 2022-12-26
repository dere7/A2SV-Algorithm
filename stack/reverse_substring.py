def reverse_substring(s):
    '''
    reversing substring between each pair of parentheses
    Eg. (abcd) -> bcda
    '''
    stack = []
    for i in s:
        if i != ')':
            stack.append(i)
        else:
            rev_str = []
            while True:
                v = stack.pop()
                if v == '(':
                    break
                rev_str.append(v)
            stack += rev_str
    return ''.join(stack)


if __name__ == '__main__':
    print(reverse_substring('(abcd)'), 'dcba')
    print(reverse_substring('(u(love)i)'), 'iloveu')
    print(reverse_substring('(ed(et(oc))el)'), 'leetcode')
