# this code will take input of cipher text form file 'ciphertext.txt'
# that was encoded using caesar cipher
# and apply brute force attack on it
# and at last returns the plain text in a separate file

print("brute force is being activated...")
file = open('ciphertext.txt', 'r')
output = open('brute.txt', 'w')
cipher = file.read()
# cipher to plain text
lenth = len(cipher)
key = 0
while key <= 26:
    plain = ''
    for i in range(lenth):
        number = 0
        number = ord(cipher[i])
        number = number - key
        plain = plain + chr(number)
    output.write(plain + '\n')
    key += 1

print("brute force applied...")



