class MinStack:

    def __init__(self):
        self.stack = []
        self.min_el = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:  # empty
            self.min_el = val
            self.stack.append(val)
        else:
            if val >= self.min_el:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.min_el)
                self.min_el = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val < self.min_el:
            self.min_el = 2 * self.min_el - val
        if not self.stack:
            self.min_el = None

    def top(self) -> int:
        val = self.stack[-1]
        if val < self.min_el:
            return self.min_el
        return val

    def getMin(self) -> int:
        return self.min_el


if __name__ == '__main__':
    obj = MinStack()
    for i in [-2, 0, -3]:
        obj.push(i)
    print(obj.getMin(), -3)
    obj.pop()
    print(obj.top(), 0)
    print(obj.getMin(), -2)
    obj.pop()
    obj.pop()
    obj.push(3)
    obj.push(-34)
    print(obj.top(), obj.getMin())
