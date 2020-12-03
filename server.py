import socket

with open ('./data/data.csv', 'r') as f:
    print(f.read())

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('192.168.10.200', 6666))
    while True:
        data, addr = s.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))
