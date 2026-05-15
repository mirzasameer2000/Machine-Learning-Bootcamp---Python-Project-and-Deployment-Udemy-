"""

Mini project: Calculator App

Features:
- Class based calculator
- Basic operations: addition, subtraction, multiplication, division
- loop for repeated use
- History stored in a list
- Save and load history using a text file
- Simple error handling for invalid inputs and division by zero

"""

HISTORY_FILE = "calculator_history.txt"

class Calculator:
    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        data = []
        try:
            with open(HISTORY_FILE, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        data.append(line)
        except FileNotFoundError:
            pass
        return data

    def save_history(self):
        with open(HISTORY_FILE, 'w') as file:
            for entry in self.history:
                file.write(entry + "\n")

    def get_number(self, message):
        while True:
            value = input(message)
            try:
                return float(value)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None
        
    def calculate(self, choice):
        a = self.get_number(message="Enter the first number: ")
        b = self.get_number(message="Enter the second number: ")

        if choice == '1':
            result = self.add(a, b)
            operation = "+"
        elif choice == '2':
            result = self.subtract(a, b)
            operation = "-"
        elif choice == '3':
            result = self.multiply(a, b)
            operation = "*"
        elif choice == '4':
            result = self.divide(a, b)
            operation = "/"
        else:
            return
        
        if result is not None:
            record = f"{a} {operation} {b} = {result}"
            print("Result:", result)
            self.history.append(record)

    def show_history(self):
        if not self.history:
            print("No history available.")
            return
        
        print("Calculation History:")
        for entry in self.history:
            print(entry)

def main():

    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Choose an operation: ")

        if choice in ['1', '2', '3', '4']:
            calc.calculate(choice)
        elif choice == '5':
            calc.show_history()
        elif choice == '6':
            calc.save_history()
            print("Goodbye! - History saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main()