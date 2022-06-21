import os, time, pickle
from cryptography.fernet import Fernet
import re


import argparse
parser = argparse.ArgumentParser(conflict_handler="resolve",add_help=False)
parser.add_argument("-r","--reset",default=0, help=argparse.SUPPRESS)
parser.add_argument("-ck","--change_key",default=0, help=argparse.SUPPRESS)
parser.add_argument("-t","--timeout",default=7, help=argparse.SUPPRESS)
args,_ = parser.parse_known_args()



V_NAME="Value"
K_NAME="Key" # "C://Users//Andrea//Desktop//Folder1//Folder2//Key"
HELP_TIMEOUT=args.timeout

# By default relative paths point to the .py directory
current_directory=os.path.dirname(__file__)
os.chdir(current_directory)

def write_key():
    """
    Generates a key and save it into a key.key file in the same directory of the .py
    """
    key = Fernet.generate_key()
    with open(re.escape(K_NAME), "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open(re.escape(K_NAME), "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and writes it
    """
    try:
       f = Fernet(key)
    except Exception as e:
       print(e)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if args.reset:
   write_key()
   A={"WEBSITE1":"password"} # initial key-password dictionary
   with open(re.escape(V_NAME), "wb") as file_to_store:
      pickle.dump(A, file_to_store)
   key = load_key()
   encrypt(re.escape(V_NAME), key)

if args.change_key:
   key = load_key()
   decrypt(re.escape(V_NAME), key)
   write_key()
   key = load_key()
   encrypt(re.escape(V_NAME), key)


clear = lambda: os.system('cls')

key = load_key()

while True:
   password = input("Addendum 1: ")
   if password=="lp":
      clear()
      try:
         decrypt(re.escape(V_NAME), key)
         file_to_read = open(re.escape(V_NAME), "rb")
         A = pickle.load(file_to_read)
         file_to_read.close()
         encrypt(re.escape(V_NAME), key)
      except Exception as e:
         print(e)
      #clear()

      call=str(input()).upper()

      if call not in ["ADD","REM","HELP"]:
         if call.upper() in A:
            print(A[call.upper()])
            time.sleep(4.4)
            clear()
         else:
            print("Not Found")
            time.sleep(0.5)
            clear()
      if call=="HELP":
         try:
            lista=list(A.keys())
            lista.sort()
            for Nickname in lista:
               print(Nickname)
            time.sleep(HELP_TIMEOUT)
         except KeyboardInterrupt:
            pass
         clear()
      elif call=="ADD":    # to add or change a password
         call1=str(input()).upper()
         call2=str(input())
         A[call1]=call2
         clear()
         file_to_store = open(re.escape(V_NAME), "wb")
         pickle.dump(A, file_to_store)
         file_to_store.close()
         encrypt(re.escape(V_NAME), key)
      elif call=="REM": # to remove a password
         call=str(input()).upper()
         try:
            del A[call]
         except:
            print("Not Found")
            time.sleep(0.5)
         clear()
         file_to_store = open(re.escape(V_NAME), "wb")
         pickle.dump(A, file_to_store)
         file_to_store.close()
         encrypt(re.escape(V_NAME), key)
   else:
      addendum2=input("Addendum 2: ")
      try:
         print("Somma: "+str(int(password)+int(addendum2)))
      except:
         print("Valori non numerici sono stati inseriti")
      print()