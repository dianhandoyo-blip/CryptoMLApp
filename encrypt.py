from mapping import hero_map

def normalize(text):
    return ''.join(c for c in text.upper() if c.isalpha())

def password_key(password):
    return sum(ord(c) for c in password) % 26

def shift_dynamic(text, password):
    shift = (len(text) + password_key(password)) % 26
    return ''.join(chr(((ord(c) - 65 + shift) % 26) + 65) for c in text)

def block_transpose(blocks):
    result = []
    for i in range(0, len(blocks), 4):
        chunk = blocks[i:i+4]
        if len(chunk) == 4:
            result.extend([chunk[2], chunk[0], chunk[3], chunk[1]])
        else:
            result.extend(chunk)
    return result

def encrypt(text, password):
    text = normalize(text)
    shifted = shift_dynamic(text, password)
    blocks = [hero_map[c] for c in shifted]
    return ' '.join(block_transpose(blocks))