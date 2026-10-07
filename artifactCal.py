while True:
    try:
        crit_rate = float(input("会心率の値を入れて下さい"))
    except ValueError:
        print("数字を入れてくれよな！")
        continue
    while True:
        try:
            crit_damage = float(input("会心ダメージの値を入れて下さい"))
            break
        except ValueError:
            print("数字を入れてくれよな！")
            continue
    break
    
crit_rate *= 2
print("会心スコアを計算するぞ！", crit_rate + crit_damage, "お疲れ様だぞ", sep="\n")