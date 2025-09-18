import socket
import poem

HOST = '127.0.0.1'  # localhost
PORT = 65432

# Initialize Poem object
p1 = poem.Poem()
p1.clean()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is listening on", HOST, PORT)

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)

        # Receive word from client
        word = conn.recv(1024).decode()
        print("Client sent word:", word)

        result = p1.getLines(word)

        # Prepare response
        response = f'<lines word="{word}" total="{len(result)}>\n'
        for num, text in result:
            response += f'<line line_number="{num}">\n{text}\n</line>\n'
        response += '</lines>'

        # Send back to client
        conn.sendall(response.encode())
