import socket 

serverAddressPort = ("192.168.2.103", 20001); 
bufferSize = 1024;

# Cria um socket UDP do lado cliente 
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM); 

def enviar_numero(numero): 
    UDPClientSocket.sendto(str(numero).encode(), serverAddressPort); 
    msgFromServer = UDPClientSocket.recvfrom(bufferSize); 
    print(f"Mensagem do Servidor: {msgFromServer[0].decode()}"); 
    
print("Enviando números para o servidor. Digite 'sair' para parar."); 
while True: 
    numero = input("Digite um número: "); 
    if numero.lower() == "sair": 
        break; 
    enviar_numero(numero);
    
UDPClientSocket.close();