playing = True
while playing:
    print("問題:", "七七は氷元素である")
    while True:
        answer = input("Y:〇 N:✕")
        if answer == "Y":
            print("正解")
            break
        elif answer == "N":
            print("不正解。答えは〇だぞ")
            break
        else:
            print("ちゃんと入力してください")
    print("終了")
    break