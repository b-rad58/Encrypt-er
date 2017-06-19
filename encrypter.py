#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
	print("Incorrect number of arguments entered")
	sys.exit(1)

fin = open(sys.argv[1], 'r')
key = sys.argv[2]
fout = open(sys.argv[3], 'a')
keyList = list()
i = 0

for a in key:
	keyList.append(ord(a.upper()))
for line in fin:
  for x in line:
    if (ord('A') <= ord(x.upper()) <= ord('Z')):
      if (i < len(key)):
      	y = ((ord(x.upper())) + keyList[i] - (2 * ord('A')))%26
      	y = chr(y + ord('A'))
      	fout.write(y)
      	i = i + 1
      else:
      	i = 0
      	y = ((ord(x.upper())) + keyList[i] - (2 * ord('A')))%26
      	y =chr(y + ord('A'))
      	fout.write(y)
      	i = i + 1
    elif x.isdigit():
    	fout.write(x)
   

