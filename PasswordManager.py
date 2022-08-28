from cryptography.fernet import Fernet #If you don't have the cryptography module ,use (pip install cryptography) to dowload it
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
def load_key():
    file=open("key.key","rb")
    key=file.read()
    return key
write_key()
key=load_key()
fer=Fernet(key)
def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,password=data.split("|")
            print("User:",user,"| Password:",fer.decrypt(password.encode()).decode())
 
def add():
    name=input("Account Name: ")
    pwd=input("Password: ")
    with open('passwords.txt','a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n") 


while True:
    mode=input("would you like to add new passaword or view an existing(add,view) to quit press q").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid input")
        continue
