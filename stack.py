class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data): # this adds a new element on top
        new_node = Node(data) # makes the data a Node
        if self.top: # If there is already something in the stack then
            new_node.next = self.top # set the 'next' of the new node as the old top, this "pushes" the old top down
        self.top = new_node # set the new node as the top

    def pop(self): # This removes the top element
        if self.top is None: # checks if there is something in the stack, if none then do nothing
            return None
        else:
            popped_node = self.top # let popped_node hold self.top
            self.top = self.top.next # make the new top the one "under" it 
            popped_node.next = None # this "pops" or deletes the element on top (the old top)
            return popped_node.data

    def peek(self): # Kind of a getter function
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

def precedence(op): # Basically a priority list. higher the num, higher the importance.
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(expr):
    stack = Stack() # creates an object 
    output = []

    expr = expr.replace(" ", "") # removes space

    for token in expr:
        if token.isalnum(): # if index is an operant then append it to output
            output.append(token)

        elif token == '(': # else if token is ( then add it to the stack
            stack.push(token)

        elif token == ')': # else if token is ) then find its partner ( 
            while not stack.is_empty() and stack.peek() != '(': # while the stack is NOT empty and not (
                output.append(stack.pop()) # pop the stack until the ( is found
            stack.pop()  # remove '('

        else: 
            while (not stack.is_empty() and # while stack is not empty and the precedence of stack is higher than of the token
                   precedence(stack.peek()) >= precedence(token)):
                output.append(stack.pop()) # pop the stack and append to output
            stack.push(token) # add the tokens in the stack

    # pop the remaining operators from the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return " ".join(output)


if __name__ == "__main__":
    infix_expr = input("Enter infix expression: ")
    postfix_expr = infix_to_postfix(infix_expr)
    print("Postfix expression:", postfix_expr)
