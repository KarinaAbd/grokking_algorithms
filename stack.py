# Write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given string.

class MyStack():
    def __init__(self) -> list:
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, elem) -> None:
        if not self.stack:
            self.stack.append(elem)
        elif isinstance(self.stack[0], type(elem)):
            self.stack.append(elem)
        else:
            raise TypeError("The stack can only contain data of one type.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("The Stack is empty")
    
    def get_top(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("The Stack is empty")
 

def is_balanced(brackets: str) -> bool:
    pairs = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    stack = MyStack()
    for bracket in brackets:
        if stack.is_empty() or bracket in pairs:
            stack.push(bracket)
        elif not stack.is_empty() and pairs.get(stack.get_top()) == bracket:
            stack.pop()
        
    if stack.is_empty():
        return True
    return False


assert is_balanced('[]{}()') == True
assert is_balanced('[()]{}{[()()]()}') == True
assert is_balanced('[(])') == False
assert is_balanced('[(]') == False
assert is_balanced(']()') == False
assert is_balanced(']()[') == False

