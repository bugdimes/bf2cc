# this file will take input of plain text and the key
# any apply caesar cipher on it
# then it will return the result in a file 'ciphertext.txt'

plain_text = input('Enter the statement: ')
key = int(input('Enter the key: '))
lenth = len(plain_text)
new = ''
for i in range(lenth):
    number = 0
    number = ord(plain_text[i])
    number = number + key
    new = new + chr(number)

file = open('ciphertext.txt', 'w')
file.write(new)
print("Written...")
file.close()




