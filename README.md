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
<summary>Feature</summary>
<br>
  
Feature
- Server-Client Architecture: Create a server that listens for incoming connections from clients. Clients can connect to the server to participate 
  in the quiz.
- Quiz Management: The server should manage the quiz questions and answers. It should have a predefined set of questions and correct answers.
- Multiplayer Support: Multiple clients should be able to connect to the server simultaneously and play the quiz in a multiplayer mode.

</details>

<details>
<summary>Usage</summary>
<br>
  
Usage
+ Start the server by running the server script in one terminal.
```
python server.py
```

+ Open a new terminal window or tab for each client you want to run.
+ In each terminal window, navigate to the project directory
+ Once you are inside the project directory, clients can connect to the server by running the client script. Run the following command in each terminal window:
```
python client.py
```
</details>
