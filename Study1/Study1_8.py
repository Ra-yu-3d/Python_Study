print("番号を入力してください")
num = int(input())

if (num % 4) == 0:
    print("進捗ダメです")
elif (num % 2) == 0:
    print("曲ができました！！！！")
else:
    print("モデルができました！！！！")
