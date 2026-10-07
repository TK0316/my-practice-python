import random
playing = True
while playing:
    result = random.randint(1, 6)
    while True:
        try:
            answer = int(input("1〜6までの数値を入れて下さい"))
        except ValueError:
            print("数字を入れて下さい")
            continue
        if 1<= answer <= 6:# 比較演算子を連結できる
                               # 1 <= answer <= 6 は「1以上かつ6以下」
            break
        else:
            print("値が範囲外です")
    if result == answer:
        print("当たり！")
        
    else:
        print("ハズレ！")
    
    while True:
        flag1 = input("もう一回遊ぶ？(Y/n)")
        if flag1 == "Y":
            print("もう一回遊ぶぞ！わーい！")
            break
        elif flag1 =="n":
            print("また遊んで欲しいぞ！バイバイ")
            playing = False
            break
        else:
            print("不正な文字が入力されました")
            continue