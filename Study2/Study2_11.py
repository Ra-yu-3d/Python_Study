#Pythonのstdlibライブラリを使用してローカルIPアドレスを見つける

import socket

ip = socket.gethostbyname(socket.gethostname())
print(ip)
