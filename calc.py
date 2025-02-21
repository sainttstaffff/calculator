from flask import Flask, render_template, request

app = Flask(__name__)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "ошибка"

def degree(num1, num2):
    return num1 ** num2

def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'degree':
            result = degree(num1, num2)
        elif operation == 'maximum':
            result = maximum(num1, num2)
        elif operation == 'minimum':
            result = minimum(num1, num2)

    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)