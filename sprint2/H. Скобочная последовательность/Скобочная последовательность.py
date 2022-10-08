class Stack:
    def __init__(self):
        self.stack_ = []

    def __bool__(self):
        return bool(self.stack_)

    def is_empty(self):
        if self.stack_ == []:
            return True
        else:
            return False

    def push(self, item):
        return self.stack_.append(item)

    def pop(self):
        return self.stack_.pop()[0]

    def peek(self):
        return self.stack_[-1]


def is_correct_bracket_seq(symbols):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbols) and balanced:
        symbol = symbols[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                popped = s.pop()
                opens = "([{"
                closes = ")]}"
                if opens.index(popped) == closes.index(symbol):
                    balanced = True
                else:
                    balanced = False

        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    symbols = list(input())
    print(is_correct_bracket_seq(symbols))