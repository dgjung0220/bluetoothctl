from bluetooth import *
from datetime import datetime

server_sock=BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]

NAME = 'SampleServer'
uuid = "00001801-0000-1000-8000-00805f9b34fb"

advertise_service(server_sock, NAME, 
		service_id = uuid,
		service_classes = [ uuid, SERIAL_PORT_CLASS ],profiles = [ SERIAL_PORT_PROFILE ],) 

print("Waiting for connection on RFCOMM channel %d" % port)
client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
	while True:
		text = input()
		client_sock.send(bytes(str(datetime.now())+','+text+'\n', 'UTF-8'))

except IOError:
		pass
		print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
