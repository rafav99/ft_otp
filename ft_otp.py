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
total_b = key_b + unix_time_b
hashkey = hashlib.sha256(total_b).hexdigest()

print(hashkey)
trunc_hk = hashkey[10:18]
print(trunc_hk)
int_trunc = int(trunc_hk, 16)
print(int_trunc)
finalpass =int_trunc % pow(10,6)
print(finalpass)