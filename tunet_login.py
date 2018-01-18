from hashlib import md5
from binascii import hexlify
import json
import requests
import sys
import time
from os import path


def md5_hash(password):
    m = md5()
    data = password.encode('latin-1')
    m.update(data)
    return hexlify(m.digest())

def login(username, password):
    hashed_password = '{MD5_HEX}' + str(md5_hash(password))[2:-1]

    data = {
        'action': 'login',
        'username': username,
        'password': hashed_password,
        'ac_id': 1
    }

    print(data)

    r = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data)

    print(r)

def logout():
    data = { 'action': 'logout' }
    r = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data)
    print(r)


def main():
    while 1:
        time.sleep(10):
        if len(sys.argv) == 1:
            dir = path.dirname(__file__)
            filename = path.join(dir, 'configure.json')
            if (path.isfile(filename)):
                with open(filename, 'r') as f:
                    data = json.load(f)
                    username = data['username']
                    password = data['password']
            else:
                username = input('username: ')
                password = input('password: ')
                autosave = input('save?(y/n): ')
                if (autosave == 'y'):
                    with open(filename, 'w+') as f:
                        json.dump({ 'username': username, 'password': password }, f)

            login(username, password)
        elif sys.argv[1] == 'logout':
            logout()

if __name__ == '__main__':
    main()
