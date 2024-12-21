import socket

# Função para capturar a operação aritmética do usuário
def get_operacao_usuario(): 
    return input("Digite uma operação aritmética (ex: 2 + 2): ");

# Mensagem contendo a operação aritmética
msgFromClient       = get_operacao_usuario();
bytesToSend         = str.encode(msgFromClient);
# Meu endereço IP = 192.168.2.103
serverAddressPort   = ("192.168.2.103", 20001);
bufferSize          = 1024;

# Cria um socket UDP do lado cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM);

# Envia msg ao servidor usando o socket UDP criado
UDPClientSocket.sendto(bytesToSend, serverAddressPort);

# Recebe a resposta do servidor
msgFromServer = UDPClientSocket.recvfrom(bufferSize);
msg = "Mensagem vinda do Servidor {}".format(msgFromServer[0]);
print(msg);