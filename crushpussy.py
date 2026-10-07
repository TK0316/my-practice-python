enemy_hp = 1000
while enemy_hp > 0:
    while True:
        flag1 = input("1.舐める", "2.挿入", sep=" ")
        if flag1 == "1":
            enemy_hp -= 100
            print("そこはだめぇ♡")
            print(enemy_hp)
            break
        elif flag1 == "2":
            enemy_hp -= 200
            print("ナカに入って来ないでぇ♡")
            print(enemy_hp)
            break
        else:
            print("下手くそ！挿入れるモノが違うわ！")
print("イッちゃった……")
print("GAME CLEAR")    