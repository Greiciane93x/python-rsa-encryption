from cryptography.fernet import Fernet

message = "hello"

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print(f'original string: ', message)
print(f'encrypted string', encMessage)


