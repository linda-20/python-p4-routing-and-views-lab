#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  
    return f"{parameter}"  

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(n) for n in range(num)) + '\n'
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        output = num1 + num2
    elif operation == "-":
        output = num1 - num2
    elif operation == "*":
        output = num1 * num2
    elif operation == "div":
        output = num1 / num2
    elif operation == "%":
        output = num1 % num2
    else:
        return "Input a valid operator!"
    return f'{output}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
