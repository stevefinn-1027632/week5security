from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":

    try:
        load_key()
    except FileNotFoundError:
        print("Geen sleutel gevonden. Genereren van nieuwe sleutel...")
        generate_key()
    
    choice = input("Wil je (e)ncrypten of (d)ecrypten? ")

    if choice == 'e':
        message = input("Voer de tekst in die je wilt versleutelen: ")
        encrypted_message = encrypt_message(message)
        print(f"Versleutelde tekst: {encrypted_message.decode()}")

    elif choice == 'd':
        encrypted_message = input("Voer de versleutelde tekst in: ")
        decrypted_message = decrypt_message(encrypted_message.encode())
        print(f"Ontsleutelde tekst: {decrypted_message}")

    else:
        print("Ongeldige keuze! Kies 'e' om te encrypten of 'd' om te decrypten.")
