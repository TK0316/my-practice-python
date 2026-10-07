def input_numbers():
    is_input = True
    while is_input:
        num1 = input("数字を入れて下さい:")
        if num1 == "q":
            return False
        try:
            number = float(num1)
            is_input = False
        except ValueError:
                print("不正な入力を検知")
                continue
    return number
def input_operators():
    is_input = True
    while is_input:
        operator = input("+,-,*,/,%,//,**:")
        if operator not in operators:
            print("不正な入力を検知")
            continue
        is_input = False
    return operator
def add(num1, num2):
    return num1 + num2
    
def subtract(num1, num2):
    return num1 - num2
    
def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    return num1 / num2

def remainder(num1, num2):
    return num1 % num2

def floor_division(num1, num2):
    return num1 // num2

def power(num1, num2):
    return num1 ** num2
    
operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": remainder,
        "//": floor_division,
        "**": power
        }
def main():
    
    running = True
    
    while running:
        num1 = input_numbers()
        if num1 is False:
            running = False
            continue
            
        operator = input_operators()
            
        is_zero = True 
        while is_zero:
            num2 = input_numbers()
            
            if num2 is False:
                running = False
                is_zero = False
                continue
                
            if operator in ("/", "//", "%") and num2 == 0:
                print("0では割れません")
                continue
            is_zero = False
            
        if running:
            print(operators[operator](num1,num2))
        
        
if __name__ == "__main__":
    print("Sakura Calculator起動！")
    main()