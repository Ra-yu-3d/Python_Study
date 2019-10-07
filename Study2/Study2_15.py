#現在のディレクトリのファイルリストを出力

import os

path = os.getcwd()
print(path)

fileList = os.listdir()
print(fileList)
