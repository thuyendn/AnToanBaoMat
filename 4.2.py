def caesar_shift(text, k):
    result = []
    mapping = [] 
    for ch in text:
        if 'A' <= ch <= 'Z':
            orig_idx = ord(ch) - ord('A')
            new_idx = (orig_idx + k) % 26
            new_ch = chr(new_idx + ord('A'))
            result.append(new_ch)
            mapping.append((ch, orig_idx, new_ch, new_idx))
        elif 'a' <= ch <= 'z':
            orig_idx = ord(ch) - ord('a')
            new_idx = (orig_idx + k) % 26
            new_ch = chr(new_idx + ord('a'))
            result.append(new_ch)
            mapping.append((ch, orig_idx, new_ch, new_idx))
        else:
            result.append(ch)
            mapping.append((ch, None, ch, None))
    return ''.join(result), mapping

plaintext = "NguyenDoanThuyen"
k = 8

ciphertext, mapping = caesar_shift(plaintext, k)

print("Plaintext:", plaintext)
print("k =", k)
print("Ciphertext:", ciphertext)

