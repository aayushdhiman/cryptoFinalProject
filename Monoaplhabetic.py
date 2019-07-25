
# Additive Encryption
def encrypt_with_additive(plain_text, n, block_size):
    cipher_text = ''
    for index in range(len(plain_text)):
        letter = enc_letter(plain_text[index].lower())
        cipher_text += dec_letter(add(letter, n)).upper()
        if index != 0 and (index - 1) % block_size == 0:
            cipher_text += " "
    return cipher_text

# Multiplicative Encryption
def encrypt_with_multiplicative(plain_text, n, block_size):
    cipher_text = ''
    for index in range(len(plain_text)):
        letter = enc_letter(plain_text[index].lower())
        cipher_text += dec_letter(multiply(letter, n)).upper()
        if index != 0 and (index - 1) % block_size == 0:
            cipher_text += " "
    return cipher_text


# Affine Encryption
def encrypt_with_affine(plain_text, n, r, block_size):
    plain_text = encrypt_with_additive(plain_text, n, block_size)
    plain_text = encrypt_with_multiplicative(plain_text.replace(" ", ''), r, block_size)
    return plain_text
