import hashlib
import time
import argparse

parser = argparse.ArgumentParser(description='Generate TOTP key')

parser.add_argument('-g', '--savekey', type=str)
args = parser.parse_args()	

if args.savekey:
    try:
        open(args.savekey, 'r')

#get unix timestamp, divided by 30 so changes not every
#second but every 30 seconds
unix_time = int(time.time()/30)
print(unix_time)

#change time and key to bytes
unix_time = int.to_bytes(5, byteorder='big', signed=False)

print(unix_time)