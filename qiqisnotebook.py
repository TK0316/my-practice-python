memo = input("メモしたいことを入力して下さい")
file = open("qiqi.txt", "a")
file.write(memo + "\n")
file .close