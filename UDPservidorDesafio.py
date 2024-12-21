import socket 
import random 
import time 
import threading 

localIP = "192.168.2.103"; 
localPort = 20001; 
bufferSize = 1024; 
buffer = []; 
buffer_size = 10; 
# Tempo de vida dos elementos em segundos
TTL = 30; 

# Cria socket datagram (UDP) 
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM); 

# Bind entre endereco e IP 
UDPServerSocket.bind((localIP, localPort)); 

print("Servidor UDP up e escutando...");

# Função para limpar o buffer periodicamente 
def limpar_buffer(): 
    while True: 
        time.sleep(TTL); 
        if buffer: 
            # Remove o elemento mais antigo
            buffer.pop(0);  
            print("Elemento expirou. Buffer atual:", buffer); 
            
# Inicia a thread de limpeza do buffer 
threading.Thread(target=limpar_buffer, daemon=True).start(); 

while True: 
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize); 
    message = bytesAddressPair[0].decode(); 
    address = bytesAddressPair[1]; 
    
    print(f"Mensagem do Cliente: {message}"); 
    
    if len(buffer) >= buffer_size: 
        # Política de substituição FIFO 
        buffer.pop(0);
        # Política de exclusão randômica 
        if buffer: 
            buffer.pop(random.randint(0, len(buffer)-1)); 
            
    buffer.append(message); 
    
    if len(buffer) >= buffer_size: 
        ack_message = "Buffer cheio. Pare de enviar pacotes.";
    else: 
        ack_message = "ACK: Recebido";
    
    bytesToSend = str.encode(ack_message);
    UDPServerSocket.sendto(bytesToSend, address); 
    print(f"Buffer atual: {buffer}");