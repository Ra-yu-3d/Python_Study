
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
