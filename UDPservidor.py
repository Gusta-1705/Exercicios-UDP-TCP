import socket

# Meu endereço IP = 19.168.2.103
localIP     = "192.168.2.103";
localPort   = 20001;
bufferSize  = 1024;

msgFromServer       = "Oi UDP Cliente";
bytesToSend         = str.encode(msgFromServer);

# Cria socket datagram (UDP)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM);

# Bind entre endereco e IP
UDPServerSocket.bind((localIP, localPort));
 
print("Servidor UDP up e escutando...");

# Função para calcular a expressão aritmética
def calcular(expressao): 
    try: 
        # Avalia a expressão recebida
        return str(eval(expressao));
    except Exception as e: 
        return "Erro: " + str(e);

# Escutando datagramas que chegam
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize);
    message = bytesAddressPair[0];
    address = bytesAddressPair[1];
    clientMsg = "Mensagem do Cliente:{}".format(message);
    clientIP  = "Endereco IP do Cliente:{}".format(address);
    
    print(clientMsg);
    print(clientIP);

    # Calcula o resultado da expressão aritmética 
    resultado = calcular(message);
    bytesToSend = str.encode(resultado);

    # Enviando msg de reply ao client
    UDPServerSocket.sendto(bytesToSend, address);