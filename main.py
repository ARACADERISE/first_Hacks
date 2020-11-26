import socket
import threading

host = '0.0.0.0'
port = 999

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cli.bind((host,port))
cli.listen(5)

while True:

  host,addr = cli.accept()
  print(host,addr)
  break