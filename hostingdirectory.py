#
import os
os.chdir(os.getcwd())
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Go to this to get the hosted directory:-  "+IPAddr+":8080")
import webbrowser
webbrowser.open('http://localhost:8080', new=2)
os.system("python -m http.server 8080")