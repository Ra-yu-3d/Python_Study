'''
1. キーボードから入力した 10 個の数の中に 5 がなければ Boo と表示する．  
2. 入力した 10 個の数の中に負の数があるかどうかを表示するようにしましょう
'''

list = []
result = 0

for i in range(10):
    num = int(input())
    if num == 5:
      result = 1
    if  num < 0:
        list.append(num)

if result != 1:
    print("Boo")

if len(list) != 0:
    print(list)
