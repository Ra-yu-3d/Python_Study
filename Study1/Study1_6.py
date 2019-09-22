print("aを入力で終了")

while True:
    print("数値を入力してください")
    jugde = input()

    if jugde is 'a':
        break

    num = int(jugde)
    if ((num % 7) == 0) or (num % 3 == 0) or (num < 0):
        if (num % 7) == 0:
            print("%dは7の倍数です。" %num)
        if (num % 3) == 0:
            print("%dは3の倍数です。" %num)
        if num < 0:
            print("%dは負の値です。" %num)
    else:
        print("%dは7の倍数でも、3の倍数でも、負の値でもありません。")
