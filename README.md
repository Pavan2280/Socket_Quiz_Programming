# Quiz Using Socket Programming

# Objective
> Welcome to the "Multiplayer Quiz with Socket Programming in Python" project! This project aims to provide a fun and interactive way to engage 
  multiple players in a quiz game over a network. By leveraging socket programming in Python, we've created a server-client architecture that 
  allows players to connect to a central server and compete in a quiz.

# Technologies Used
- Python 3.11.4

# Table of contents

<details>
<summary>Introduction</summary>
<br>

Socket programming is a fundamental concept in computer networking and communication, allowing applications to exchange data over a network, such as the internet or a local network. It forms the backbone of how computers communicate with each other in a distributed environment.

In the world of computer networking, a "socket" is essentially an endpoint for sending or receiving data across a computer network. Socket programming enables software applications to create, open, close, read from, and write to these sockets, facilitating data transfer between different machines.
</details>

<details>
<summary>Features</summary>
<br>
  
- Server-Client Architecture: Create a server that listens for incoming connections from clients. Clients can connect to the server to participate 
  in the quiz.
- Quiz Management: The server should manage the quiz questions and answers. It should have a predefined set of questions and correct answers.
- Multiplayer Support: Multiple clients should be able to connect to the server simultaneously and play the quiz in a multiplayer mode.
</details>

<details>
<summary>Procedure</summary>
<br>
  
1) Client Connections:
  Clients should connect to the server using a suitable client application or script.
  The server will wait for a specific number of clients to join the quiz before proceeding. The number of clients required is determined by user input.
  Quiz Gameplay:

  Once the required number of clients have connected, the quiz begins.
  Each client will be presented with three questions one by one.
  Clients should provide their answers within a specified time limit.

2) Scoring:

  After each client has answered all three questions, the server calculates their scores.
  Scores are based on the correctness and speed of responses.
  Clients receive their scores after completing the quiz.

3) Connection Closure:
  After the quiz is completed for all clients, or when a client disconnects, the server will close the connection.
  Clients can no longer participate in the quiz or receive scores.
</details>

<details>
<summary>Usage</summary>
<br>

+ Start the server by running the server script in one terminal.
```
python server.py
```
![image](https://github.com/Pavan2280/Socket_Quiz_Programming/assets/131603225/3a58a311-9d13-4a50-9633-e8eda4dfa7ab)


+ Open a new terminal window or tab for each client you want to run.
+ In each terminal window, navigate to the project directory
+ Once you are inside the project directory, clients can connect to the server by running the client script. Run the following command in each terminal window:
```
python client.py
```
![image](https://github.com/Pavan2280/Socket_Quiz_Programming/assets/131603225/d2c81437-717e-47f1-a899-ecbc88437c7a)
![image](https://github.com/Pavan2280/Socket_Quiz_Programming/assets/131603225/c0a0f3cb-c8b2-4981-b155-b1308f3cd5f2)

+ Once the quiz is over the connection will be closed
![image](https://github.com/Pavan2280/Socket_Quiz_Programming/assets/131603225/5dcb5295-62b0-41b3-bf0f-c2f93c214d4c)
</details>
