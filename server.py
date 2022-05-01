import socket
import subprocess

def get_gpu_usage():
    cmd = 'nvidia-smi --query-gpu=index,name,memory.total,memory.used,utilization.gpu, --format=csv,noheader'
    output = subprocess.check_output(cmd, shell=True)
    return output.decode('utf-8')

IPADDR = socket.gethostname()
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IPADDR, PORT))
s.listen(1)

client_socket, address = s.accept()
print(f'connection from {address=}')
client_socket.send(bytes(get_gpu_usage(), 'utf-8'))
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()
