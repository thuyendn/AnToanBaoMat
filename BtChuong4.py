def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():  # chỉ mã hóa chữ cái
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char
    return result

# Dữ liệu đề bài
plaintext = "NguyenDoanThuyen"
k = 8

ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
