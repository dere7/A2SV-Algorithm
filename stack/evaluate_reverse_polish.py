import math


def evaluate_reverse_polish(tokens: [str]) -> int:
    '''for given tokens of reverse polish expersion evaluate expression'''
    stack = []
    for token in tokens:
        if token in '+-*/':
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                result = num1 / num2
                stack.append(math.floor(result) if result >=
                             0 else math.ceil(result))
        else:
            stack.append(int(token))
    return stack[0]


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    print(evaluate_reverse_polish(tokens))  # 22
    tokens = ["4", "13", "5", "/", "+"]
    print(evaluate_reverse_polish(tokens))  # 6
