'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]．
このリストaを取得し，このリストの 偶数要素のみを含む新しいリストを作成する
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Even_number = []

for i in range(len(a)):
    if (a[i] % 2) == 0:
        Even_number.append(a[i])

print(Even_number)
