from Utils.Get_Input import get_input
from cryptography.fernet import Fernet


def load_key():
    with open("key.key", 'rb') as file:
        key = file.read()
    return key


Master_pwd = get_input('Enter Master password: ')
key = load_key() + Master_pwd.encode()
fer = Fernet(key)


def view():
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip().split('|')
            if len(data) == 2:
                user, passw = data
                try:
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print(f'User: {user}\nPassword: {decrypted_pass}')
                except Exception as e:
                    print(f"Failed to decrypt password for user {user}. Error: {e}")
            else:
                print(f"Skipping line: {line}, as it does not match the expected format.")


def add():
    name = get_input('Name: ')
    pwd = get_input('Password: ')
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('password.txt', 'a') as f:
        f.write(f'{name} | {encrypted_pwd}\n')


while True:
    mode = get_input("Would you like to add a new password or view existing ones (view, add) or press q to quit: ")

    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
