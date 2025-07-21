a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide, modulo, power): ")

match operation:
    case 'add':
        print("Result:", a + b)
    case 'subtract':
        print("Result:", a - b)
    case 'multiply':
        print("Result:", a * b)
    case 'divide':
        if b == 0:
            print("Error: Division by zero")
        else:
            print("Result:", a / b)
    case 'modulo':
        print("Result:", a % b)
    case 'power':
        print("Result:", a ** b)
    case _:
        print("Invalid operation")