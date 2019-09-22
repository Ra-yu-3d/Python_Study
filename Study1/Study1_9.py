print("文字列を入力してください")
str = input()

if str == str[::-1]:
    print("回文です")
else:
    print("回文ではありません")
