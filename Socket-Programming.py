#!/usr/bin/env python
# coding: utf-8

# # Socket Programming Program by `Mr. Harshit Dawar!`

# In[1]:


import socket


# In[3]:


# Recieving Program using UDP Protocol
def receive(ip, port):
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_ip = ip
    receiver_port = port
    receiver.bind((receiver_ip, receiver_port))
    
    while True:
        data = receiver.recvfrom(512)  # Max Number of bytes in data
        clientIP = data[1][0]
        clientPort = data[1][1]
        message = data[0].decode()
        print(clientIP + ":" + message)


# In[7]:


def send(ip, port, message):
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = message.encode()
    receiverIP = ip
    receiverPort = port
    sender.sendto(message, (receiverIP, receiverPort))


# ## Congratulations, you have implemented a socket/network program to send & receive Message is built!
