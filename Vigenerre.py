def encrypt_with_viginere(message, key):
    key_length = len(key)
    int_key = [ord(i) for i in key]
    int_message = [ord(i) for i in message]
    cipher_text = ''

    for i in range(len(int_message)):
        value = (int_message[i] + int_key[i % key_length]) % 26
        cipher_text += chr(value + 65)

    return cipher_text
