DISPLAY_WIDTH = 20
DISPLAY_HEIGHT = 20
quit = True
while quit:
    
    prompt = input("SakuraCoder>")
    
    if prompt == "open":
        file_name = input("ファイル名を入力:")
        try:
            file = open(file_name, "r")
            
        except FileNotFoundError:
            print("そんなファイルはありません")
            continue
        while hoge:
            line = file.readline()
            if line = "":
                pass
            else:
                char = len(line)
                for x in range(0, char, DISPLAY_WIDTH):
                    y = x + DISPLAY_WIDTH
                    if "\n" in line[x: y]:
                        print(line[x: y], end="")
                    else:
                        print(line[x: y], end="\n")
        
        while True:
        flag1 = input("他のファイルを開きますか？")
        if flag1 == "Y":
            break
        elif flag1 == =="n":
            qait = False
            break
        else:
            continue
            
            
def input_prompts():
    is_input = True
    while is_input:
        prompts = input()
        if prompts == "":
            continue
        is_input = False
        return prompts
        
def open_file():
    is_input = True
    while is_input:
        file_name = input("ファイル名を入力:")
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print("不正なファイル名")
            continue
        else:
            is_input = False
            return file
            
def display_file(file):
    print(file)
    