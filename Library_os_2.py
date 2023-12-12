import os
import time
import socket

print(os.getcwd())
os.chdir('C:\\Users\\longi\\Desktop')
print(os.getcwd())
time.sleep(2)
os.mkdir('New_folder')
time.sleep(2)
os.rename('New_folder', 'Newer_folder')
time.sleep(2)
#os.rmdir('Newer_file')
#os.system('cmd /c "dir /s new.txt >> result.txt"')
#os.system('cmd /c "cd C:\\Users\\longi\\Desktop\\Newer_folder\\"')
#os.system('cmd /c "ipconfig /all new.txt >> result.txt"')
#os.system('cmd /c "ipconfig /all new.txt > result.txt"')

os.system('cmd /c "cd C:\\Users\\longi\\Desktop\\Newer_folder\\ && ipconfig /all new.txt > result.txt"')

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)
