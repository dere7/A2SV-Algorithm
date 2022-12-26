def valid_parentheses(s: str) -> bool:
    '''Given s containing one of '(){}[]'
    determine if the string is valid.
    - open brackets must be closed by the same type, correct order
    '''
    stack = []
    for i in s:
        if i in '([{':
            stack.append(i)
        else:
            if not stack:
                return False
            top = stack.pop()
            if top == '(' and i != ')' or (
                top == '[' and i != ']' or (
                    top == '{' and i != '}')):
                return False

    return False if stack else True


if __name__ == '__main__':
    strs = ['()', "()[]{}", "(]", ']']
    print([valid_parentheses(s) for s in strs])  # [true, true, false]
