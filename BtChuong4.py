def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char
    return result

plaintext = "NguyenDoanThuyen"
k = 8

ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
