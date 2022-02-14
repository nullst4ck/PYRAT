import socket
import colorama

colorama.init()
ART = """                                                          
           xxxxxx                  xxxxxxxxxxxxxxxxxxx
      xxxxxx     xx      xxxx     xx                xx
    xx    x  x    x      x   xx   xxxxxxxxxxxxxxxxxxx
          x     xxx      x    xxx       x  xx
         xxxxxxxxx       x  x   xx       x  x
        x xxxxx  x      xxxxxxxxx x      x  xx
      xx   xxxxxxx       x  xxx   x      x   x
     xx   x  xx xxx      x  x xx  x      x   x
    xxx  xx   xx xxx    x  xx  xx x      x   x
      xxxx     xxxxx   x   x    xxx      x   x
xxx                    xxxxx             x   x
  xx                                     xxxxx
   x
   x           xxxxxxxxxxxxxxxx
   xx    xxxxxx                xx
    xxxxxxx                     xxx
        x  xxx                 x  xxx
             xxxxx            xxx   xxxxxxxx
               x xxxx              xxx xx
             xxx    xxxxxxxxxxxxxxx
                                  xxx
"""
print(colorama.Fore.LIGHTGREEN_EX + ART)
print(colorama.Style.RESET_ALL)

#Setup socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Set local server to local ip
local_server = ""

#Ask for bind port
bind_port = input("Server port? ")

#Bind to server ip and port
soc.bind((local_server, int(bind_port)))
soc.listen()

#Stay while true loop
while True:
    print("Listener Started on Port: ", int(bind_port))
    print("Waiting for Connection....")
    conn, address = soc.accept()
    print("Connection OK!: ", address)

    try:
        while True:
            command = input("Command: ")
            #Send command and encode
            conn.sendall(command.encode())
            packet = conn.recv(4096)
            #Decode the incoming packet
            decoded = packet.decode()
            #print the info
            print(decoded)
    except:
        print("Disconnect from: ", address)