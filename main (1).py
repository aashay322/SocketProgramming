###First Socket program, uncomment to run
# import socket 
# import sys 

# try: 
#   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   print ("Socket successfully created")
# except socket.error as err:
#   print("socket creation failed with error %s" %(err))

# #default port for socket 
# port = 80 

# try: 
#   host_ip = socket.gethostbyname('www.google.com')
# except socket.gaierror:
#   print("There was an error resolving the host")
#   sys.exit()


# s.connect((host_ip, port))

# print("The socket has successfully connected to google")

###Second socket program 
import socket

s = socket.socket()
print("Socket created successfully")

port = 12345

#Next bind to the port 
s.bind(('', port))

print("socket binded to %s" %(port))

#put the socket into listening mode 
s.listen(5)
print("socket is listening")

while True: 

  #Establish a connection with a client 
  c, addr = s.accept()
  print('Got connection from', addr)

  #send a thank you message to the client
  messg = "Welcome to socket programming. Thank you for joining us" 
  c.sendall(bytes(messg.encode()))

  #Close the connection with the client 
  c.close()


