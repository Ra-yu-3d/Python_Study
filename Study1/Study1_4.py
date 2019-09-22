print("借金の総額を入力してください")
debt = int(input())
print("1月に返済する金額を入力してください")
month = int(input())
print("返済までにかかる年数は%d年%dヶ月です" %((debt//(12*month)), ((debt%(12*month))//month)+1))

print("毎年のボーナスから返却する金額を入力してください")
bonus = int(input())
print("返済完了が%d年早くなります" %((debt//(12*month))-(debt//(12*month+bonus))))

print("返済を完了したい年数を入力してください")
bonus = int(input())
print("返済を%d年で完了させたい場合ボーナスから%d円返す必要があります" %(bonus, ((debt / bonus)%(12*month))))
