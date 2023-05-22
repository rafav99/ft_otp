import hashlib
import time
import argparse
import base64
import hmac
import struct
from cryptography.fernet import Fernet

#parsing
parser = argparse.ArgumentParser(description='Generate TOTP key')

parser.add_argument('-g', '--savekey', type=str)
parser.add_argument('-k', '--genpass', type=str)
args = parser.parse_args()    


if args.savekey:
    cryptkey = Fernet.generate_key()
    with open('cript.key', 'wb') as keyfile:
        keyfile.write(cryptkey)
    fernet = Fernet(cryptkey)
    try:
        with open(args.savekey, 'rb') as hkeyfile:
            hexkey = hkeyfile.read().strip()
    except:
        print("Could not open file")
    hexcad = 'abcdef123456789ABCDEF'
    ncryptkey = fernet.encrypt(hexkey)
    if len(hexkey) >= 64:
        with open('ft_otp.key', 'wb') as f:
            f.write(ncryptkey)
            print("Key was succesfully saved in ft_otp.key")
    else:
        print("Key has to be at least 64 hexadecimal characters")

if args.genpass:
    try:
        with open('ft_otp.key', 'rb') as otpkeyfile:
            rawkey = otpkeyfile.read()
        with open('cript.key', 'rb') as keyfile:
            criptkey = keyfile.read()
        fernet = Fernet(criptkey)
        key = fernet.decrypt(rawkey)
    except:
        print("could not open files")

    #get unix timestamp, divided by 30 so changes not every
    #second but every 30 seconds
    unix_time = int(time.time()/30)

    #change time and key to bytes
    unix_time_b = unix_time.to_bytes(length=8, byteorder='big', signed=False)
    key_b = bytes.fromhex(key.decode())

    #hash algorithm
    h = hmac.new(key_b, unix_time_b, hashlib.sha1).digest()

    #get last 4 bits value from h
    last_4 = last_4 = h[19] & 15

    #truncate h, 4 bytes starting from last_4 bit value
    h = (struct.unpack(">I", h[last_4:last_4+4])[0] & 0x7fffffff) % 1000000

    passwdno_0 = str(h)

    while len(passwdno_0) < 6:
        passwdno_0 = '0' + passwdno_0

    print(passwdno_0)



