class Stack:
    stack = []

    def __init__(self):
        pass

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        result = self.stack[len(self.stack) - 1]
        self.stack.remove(result)
        return result

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return True if len(self.stack) == 0 else False
