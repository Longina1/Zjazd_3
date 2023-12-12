import os
import time

print(os.getcwd())
os.chdir('C:\\Users\\longi\\Desktop')
print(os.getcwd())
time.sleep(2)
os.mkdir('New_file')
time.sleep(2)
os.rename('New_file', 'Newer_file')
time.sleep(2)
os.rmdir('Newer_file')
os.system('cmd /c "dir /s new.txt >> result.txt"')
#os.system('cmd /c "ipconfig /all new.txt >> result.txt"')
os.system('cmd /c "ipconfig /all new.txt > result.txt"')
