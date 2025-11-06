from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            area = 3.14159 * (radius ** 2)
        except ValueError:
            area = "Invalid input!"
    return render_template('areaofcircle.html', area=area)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            area = 0.5 * base * height
        except ValueError:
            area = "Invalid input!"
    return render_template('areaoftriangle.html', area=area)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top
        self.top = self.top.next
        popped.next = None
        return popped.data

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def is_empty(self):
        return self.top is None


def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    output = []
    expression = expression.replace(" ", "")

    for token in expression:
        if token.isalnum(): 
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:
            while (not stack.is_empty() and
                   precedence(stack.peek()) >= precedence(token)):
                output.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        output.append(stack.pop())

    return " ".join(output)


@app.route('/converter', methods=['GET', 'POST'])
def converter():
    result = None
    if request.method == 'POST':
        infix_expr = request.form.get('infix', '')
        result = infix_to_postfix(infix_expr)
    return render_template('converter.html', result=result)



if __name__ == "__main__":
    app.run(debug=True, port=1259)
