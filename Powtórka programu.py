import os
import time




print(os.getcwd())
os.chdir('C:\\Users\\longi\\Desktop')
print(os.getcwd())
os.mkdir('New_folder')
time.sleep(2)
os.rename('New_folder', 'Newer_folder')
time.sleep(2)
os.rmdir('Newer_folder')
os.system('cmd /c "ipconfig /all >> result.txt"')

