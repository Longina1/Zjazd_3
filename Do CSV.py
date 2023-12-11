with open('rozliczenie.csv', 'r') as file1:
    content = file1.readlines() # plik nadal otwarty
print(content) # bez indentacji - plik już jest zamknięty

content[0] = content[0].split(',')
print(content)

for item in range (len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3])
print(content[3][2]) # dostęp do pól

#policzyć, ile osób na macierzyńśkim
#policzyć średnią wypłatę
