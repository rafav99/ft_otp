import hashlib
import time
import argparse
import base64
import hmac
import struct

#parsing
parser = argparse.ArgumentParser(description='Generate TOTP key')

parser.add_argument('-g', '--savekey', type=str)
args = parser.parse_args()	

if args.savekey:
    try:
        f = open(args.savekey, 'r')
        key = f.read().strip()
    except:
        print("could not open file")

#get unix timestamp, divided by 30 so changes not every
#second but every 30 seconds
unix_time = int(time.time()/30)

#change time and key to bytes
unix_time_b = unix_time.to_bytes(length=8, byteorder='big', signed=False)
key_b = bytes.fromhex(key)

#hash algorithm
h = hmac.new(key_b, unix_time_b, hashlib.sha1).digest()

#get last 4 bits value from h
last_4 = last_4 = h[19] & 15

#truncate h, 4 bytes starting from last_4 bit value
h = (struct.unpack(">I", h[last_4:last_4+4])[0] & 0x7fffffff) % 1000000

passwdno_0 = str(h)

while len(passwdno_0) < 6:
    passwdno_0 += '0'

print(h)




