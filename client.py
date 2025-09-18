import socket

HOST = '127.0.0.1'
PORT = 65432

word = input("Enter a word to search in poem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(word.encode())

    data = s.recv(4096).decode()
    print("Response from server:\n", data)
