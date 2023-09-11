import socket

# Create a client server 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

print("Note:Your answer should be in caps(A,B,C,D)")

try:
    client_socket.connect(server_address)

    while True:
        question = client_socket.recv(1024).decode()
        if not question:
            break
        print(question)

        client_socket.send("ACK".encode())

        options = client_socket.recv(1024).decode()
        print(options)

        answer = input("Your answer: ").strip()
        client_socket.send(answer.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    score = client_socket.recv(1024).decode()
    print(score)

except ConnectionAbortedError:
    print("Connection to the server was aborted.")
except KeyboardInterrupt:
    print("Quiz session terminated by the user.")
finally:
    client_socket.close()