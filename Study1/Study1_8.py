'''
ユーザーに番号を尋ねます．番号が偶数か奇数かに応じて，適切なメッセージをユーザーに出力 します．
また，数値が 4 の倍数の場合、別のメッセージを出力
'''

print("番号を入力してください")
num = int(input())

if (num % 4) == 0:
    print("進捗ダメです")
elif (num % 2) == 0:
    print("曲ができました！！！！")
else:
    print("モデルができました！！！！")
