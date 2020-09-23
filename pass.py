from cryptography.fernet import Fernet
import pyperclip
import sqlite3
import random
import string
import sys

#Set to permanent location of database 
FILES_DIR=''

#Set to location of keydir. eg /mnt/usb to store key on external drive
KEY_DIR=''

#Create the key
def write_key():
    key = Fernet.generate_key()
    with open(KEY_DIR + '/key.key', 'wb') as key_file:
        key_file.write(key)
        #print('key generated')

#Load the key
def load_key():
    try:
        return open(KEY_DIR + '/key.key', 'rb').read()
        #print('key loaded')
    
    #If keyloading fails create key and load it
    except OSError:
        #print('could not open key')
        #print('generating new key')
        write_key()
        load_key()

#Create table
def create_table(conn):
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE login
                (site text, pass text)''')
        conn.commit()
    
    #if table exists do nothing
    except sqlite3.Error:
        pass

#load key
key = load_key()
f = Fernet(key)

#connect to database
conn = sqlite3.connect(FILES_DIR + '/pass.db')

#create table if required
create_table(conn)

c = conn.cursor()

site = None

#if an argument is supplied use it as site
if len(sys.argv) == 2:
    site = sys.argv[1]

#use input as site
else:
    site = input()

c.execute('SELECT * FROM login WHERE site=?', (site,))
res = c.fetchall()

#if password does not exist create it
if len(res) == 0:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    for character in range(20):
        password.append(random.choice(characters))
    password = ''.join(password)
    pyperclip.copy(password)
    password = password.encode()
    password = f.encrypt(password)
    insert = (site, password,)
    c.execute('INSERT INTO login VALUES (?,?)', insert)
    conn.commit()

#if password exists use it
else:
    res = res[0]
    password = res[1]
    password = f.decrypt(password)
    password = password.decode()
    pyperclip.copy(password)

conn.close()

