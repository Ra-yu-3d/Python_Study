#数を 10 個入力してその合計を表示するプログラムを作りなさい

sum = 0

for i in range(10):
  num = input()
  num_trans = int(num)
  sum += num_trans

print(sum)
