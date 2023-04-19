import hashlib
import time
import argparse

parser = argparse.ArgumentParser(description='Generate TOTP key')

parser.add_argument('-g', '--savekey', type=str)
args = parser.parse_args()	

if args.savekey:
    try:
        f = open(args.savekey, 'r')
        key = f.read()
        print(key)
    except:
        print("could not open file")

#get unix timestamp, divided by 30 so changes not every
#second but every 30 seconds
unix_time = int(time.time()/30)
print(unix_time)

#change time and key to bytes
unix_time_b = int.to_bytes(unix_time, length=5, byteorder='big', signed=False)
key_b = bytes.fromhex(key)

print(unix_time_b)
print(key_b)