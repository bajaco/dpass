from cryptography.fernet import Fernet
import pyperclip
import sqlite3
import random
import string

FILES_DIR=''

def write_key():
    key = Fernet.generate_key()
    with open(FILES_DIR + '/key.key', 'wb') as key_file:
        key_file.write(key)
        #print('key generated')

def load_key():
    try:
        return open(FILES_DIR + '/key.key', 'rb').read()
        #print('key loaded')
    except OSError:
        #print('could not open key')
        #print('generating new key')
        write_key()
        load_key()

def create_table(conn):
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE login
                (site text, pass text)''')
        conn.commit()
    except sqlite3.Error:
        pass

key = load_key()
f = Fernet(key)
conn = sqlite3.connect(FILES_DIR + '/pass.db')
create_table(conn)
c = conn.cursor()
site = input()
c.execute('SELECT * FROM login WHERE site=?', (site,))
res = c.fetchall()
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
else:
    res = res[0]
    password = res[1]
    password = f.decrypt(password)
    password = password.decode()
    pyperclip.copy(password)

conn.close()

