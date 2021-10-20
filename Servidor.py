import socket
import sys

#deixar vazio para receber conexões fora da rede local
host = ''

#porta onde o servidor irá escutar
port = 1234

#cria um UDP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#garante que o socket será destruído (pode ser reusado) após uma interrupção da execução 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
#associa o socket à uma porta
s.bind((host, port))
    
while True:
	print('waiting to receive message')
	data, address = s.recvfrom(1024)
		
	print ('received: ' + data + '\nfrom: ' + address[0] + '\nlistening on port: ' + str(address[1]))