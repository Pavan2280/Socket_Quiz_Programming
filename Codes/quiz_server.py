import socket
import random
import threading

# Limit number of clients 
total_clients = int(input("Enter number of clients:")) 

# Define quiz questions and options 
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "correct_answer": "A"
    },
    {
        "question": "What is 7 + 3?",
        "options": ["A) 5", "B) 10", "C) 15", "D) 20"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
    }
]

# Create a socket server 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(total_clients)  
print("Quiz server is listening...")

def send_question_and_options(client_socket, question, options):
    client_socket.send(question.encode())
    client_socket.recv(1024)  # Wait for acknowledgment
    client_socket.send(options.encode())

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    # Shuffle the questions 
    random.shuffle(questions)

    correct_answers = 0

    for q in questions:
        question_text = q["question"]
        options = "\n".join(q["options"])
        correct_answer = q["correct_answer"]

        send_question_and_options(client_socket, question_text, options)

        client_answer = client_socket.recv(1024).decode().strip()

        if client_answer == correct_answer:
            response = "Correct!\n"
            correct_answers += 1
        else:
            response = f"Wrong! The correct answer is {correct_answer}\n"

        client_socket.send(response.encode())

    score_message = f"You answered {correct_answers}/{len(questions)} questions correctly.\n"
    client_socket.send(score_message.encode())

    client_socket.close()
    print(f"Connection from {client_address} closed.")

try:
    for i in range(total_clients): # Accept up to no of clients (user input)
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

    print("Maximum number of clients reached. No longer accepting connections.")

except KeyboardInterrupt:
    print("Server terminated by the user.")

finally:
    server_socket.close()
