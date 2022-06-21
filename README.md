# Password collector
A convenient tool to keep safe your passwords and remember them all by just knowing a single "super" password. <br>

Once converted to executable a camouflaged python script will be the only way to retrieve all your passwords from an encrypted file. <br>
Your passwords will stored in a python dictionary object and encrypted using Fernet's symmetric authenticated cryptography.

- Install the following library to encode your passwords
```
$ pip install cryptography
```
The file simulates a trivial program made by a beginner which is able to take any two numbers and to sum them up if no invalid input is given; however you can access the real program if you enter a specific word as first "addendum". <br>

Before starting collecting and encrypting your passwords you have to:

- modify the script by specifying the unique password required to access all the others and the directories of the Value (the encrypted dictionary object) and the Key (the file used to decrypt) files. <br>
  The parts to be modified are the tokens V_PATH, K_PATH and PASSWORD. The default Value and Key directories are the same as the .py file. <br>

- run the script from the command-line by passing -r 1 as argument, it will initialize the Key and the Value files in the directories you indicated.

```
$ python "C://Users//Andrea//Desktop//Frenet password collector.py" -r 1
```

The Value file initially contains a single example of key-password pair.

- convert the script to executable (for you security)

At this point you can access your dictionary of passwords by entering the PASSWORD token as first input and the key (not to be confused with the Key file to encrypt-decrypt) of the password you want to display. <br>
For instance if you type "website1" (the key is not case-sensitive) you see "password1" for 7 seconds (is it possible to permanently modify this value by changing PASS_TIMEOUT, or temporarily by using the argument --ptimeout).
<br>

If you pass "help" instead of passing a key, you will see the entire list of keys for 15 seconds (is it possible to permanently modify this value by changing HELP_TIMEOUT, or temporarily by using the argument --timeout).
<br>

Again if you pass "add" you can add (or modify an existing one) a new key and a new password to your secret storage (the first input is the key the second is the password).
<br>

If you type "rem" you can remove passwords by entering the key.
<br>

Is it possible to generate a new key and replace the old one by running the program in the command-line using the command --change_key 1. <br> In this case the Value file will be automatically decrypted with the old key and encrypted with the new one.

- Warnings and suggestions <br>

You can use each time a different path for Value and Key by passing the desiderd path using the arguments --value_path and --key_path. <br>

It may be an option to keep the Key far away from the Value altough it should **never** get lost.
