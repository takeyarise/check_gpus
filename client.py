import socket

IPADDR = socket.gethostname()
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPADDR, PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

msg = b''
while True:
    m = s.recv(1024)
    if len(m) <= 0:
        break
    msg += m
print(msg.decode('utf-8'))
