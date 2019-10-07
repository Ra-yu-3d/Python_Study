#リストの最初と最後の色を表示しなさい

'''
現状意味のないクラスです
class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    WHITE = '\033[37m'
'''

print("赤、緑、白、黒を好きな順序で入力してください")

color_list = []
for i in range(4):
    color = input()
    color_list.append(color)

print("{}, {}" .format(color_list[0], color_list[3]))
