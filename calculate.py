#タイトル画面
print("="*40)
print("電卓")
print("="*40)
#メイン処理
while True:
    num1 = input("数字を入力して下さい(終了はq):")
    if num1 == "q":
        break
    try:
        num1 = float(num1)
    except ValueError:
        print("挿入れるモノが違うわ。数字よ")
        continue
            
    print(num1)
    
    while True:
        operator = input("+,-,*,/,%,//,**:")
        if operator not in ["+", "-", "*", "/", "%", "//", "**"]:
            print("何を挿入れてるの？演算子を挿入れなさい")
            continue
        break
    print(operator)
    
    while True:
        try:
            num2 = float(input("数字を入力して下さい:"))
            if operator in ["/", "%", "//"] and num2 == 0:
                print("0は挿入れないで")
                continue
            break
        except ValueError:
            print("挿入れるモノが違うわ。数字よ")
            continue
            
operators = {
"+": lambda num1, num2:(num1 + num2),
"-": lambda num1, num2:(num1 - num2),
"*": lambda num1, num2:(num1 * num2),
"/": lambda num1, num2:(num1 / num2),
"%": lambda num1, num2:(num1 % num2),
"//": lambda num1, num2:(num1 // num2),
"**": lambda num1, num2:(num1 ** num2)
    }