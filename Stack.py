"""
Stack Data Structure
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty:
            return self.items[-1]
        else:
            return "EMPTY LIST"

    def get_stack(self):
        return self.items

    def print_stack(self):
        print("Stack:")
        [print("  " + x) for x in reversed(self.items)]
        print()

if __name__ == "__main__":
    stack = Stack()
    stack.push("451 degrees Fahrenheit")
    stack.push("1984")

    stack.print_stack()

    stack.pop()

    stack.print_stack()

    print(stack.is_empty())

    stack.push("Dune")
    stack.push("Ready Player One")

    print(stack.print_stack())
    print(stack.peek())

    """
    Use Stack to check whether parenthesis are balanced or not
        Examples:
        --> (), (()), {[()]} --- Balanced
        --> ()), [{{}]]      --- Not Balanced
    """

    def is_paren_balanced(parenthesis):
        s = Stack()

        is_balanced = True

        for letter in parenthesis:
            print(letter)
            if letter in "{[(":
                s.push(letter)
            else:
                try:
                    sign = s.pop()
                except:
                    is_balanced = False
                    break
                if sign == "[":
                    sign = "]"
                elif sign == "{":
                    sign = "}"
                elif sign == "(":
                    sign = ")"
                is_balanced = (letter == sign)
                print(letter, " == ", sign)
                if is_balanced == False:
                    break

        if s.get_stack() != []:
            is_balanced = False

        if is_balanced:
            return "Paranthesis are balanced"
        else:
            return "Paranthesis are NOT balanced"

    print(is_paren_balanced('{[]()}'))


    """
    Use Stack to convert integer to binary
    """

    def convert_int_to_bin(number, base):
        s = Stack()

        while number > 0:
            s.push(number % base)
            number = number // base

        arr = []
        for i in range(len(s.get_stack())):
            arr.append(s.pop())

        return arr

    for number in convert_int_to_bin(242, 2):
        print(number, end="")

    """
    Use Stack to reverse string
    """

    def reverse_string(input_word):
        s = Stack()
        reversed_word = ""

        for letter in input_word:
            s.push(letter)

        while not s.is_empty():
            reversed_word += s.pop()
        
        print(reversed_word)

    reverse_string("Hi! How are you doing?")

    def reverse_word_order(input_word):
        s = Stack()
        reversed_word = ""
        input_word = input_word.split(" ")

        for word in input_word:
            s.push(word)

        while not s.is_empty():
            reversed_word += s.pop() + " "
        
        print(reversed_word)

    reverse_word_order("Hi How are you doing?")
