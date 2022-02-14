# PYRAT
A Python Remote Administration Tool
Server:
- Binds to local ip and a port of your choice
- Loop to wait for commands
- Send encoded commands
•	Receive 4096 size packets annd decode the output then print it to the screen
•	Once client disconnects; display to the screen
Client:
•	Ask for Server IP information then validate that the IP meet IP Address format.
•	Ask for Server Port
•	Print the Server info and port
•	Run Command Loop with a subprocess to send command output back to the server
Usage Instructions:
-start server.py and enter the binding port at the prompt – sudo python3 server.py
-start client.py and enter the server IP and port at the prompt – sudo python3 client.py
-Enter command at the prompt and they will be executed on the client with the output sent back to the server
