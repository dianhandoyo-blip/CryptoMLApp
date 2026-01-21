from mapping import hero_map

reverse_map = {v: k for k, v in hero_map.items()}

def password_key(password):
    return sum(ord(c) for c in password) % 26

def inverse_shift(text, password):
    shift = (len(text) + password_key(password)) % 26
    return ''.join(chr(((ord(c) - 65 - shift) % 26) + 65) for c in text)

def inverse_block_transpose(blocks):
    result = []
    for i in range(0, len(blocks), 4):
        chunk = blocks[i:i+4]
        if len(chunk) == 4:
            result.extend([chunk[1], chunk[3], chunk[0], chunk[2]])
        else:
            result.extend(chunk)
    return result

def decrypt(cipher, password):
    blocks = cipher.split()
    blocks = inverse_block_transpose(blocks)
    text = ''.join(reverse_map[b] for b in blocks)
    return inverse_shift(text, password)