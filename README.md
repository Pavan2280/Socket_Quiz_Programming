# Quiz Using Socket Programming

# Objective
> The objective of this project is to develop a quiz application using socket programming in Python.

# Project Overview:
> Socket programming allows communication between different computers over a network. In this project, we will leverage socket programming to     
  create a simple quiz application where one machine acts as the server, and multiple machines can connect to it as clients to participate in the 
  quiz.

# Technologies Used
- Python 3.11.4

# Feature
- Server-Client Architecture: Create a server that listens for incoming connections from clients. Clients can connect to the server to participate 
  in the quiz.
- Quiz Management: The server should manage the quiz questions and answers. It should have a predefined set of questions and correct answers.
- Multiplayer Support: Multiple clients should be able to connect to the server simultaneously and play the quiz in a multiplayer mode.

# Usage
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
