#!/usr/bin/python
import sys
import argparse
import os
import ntpath

def get_args():
    parser = argparse.ArgumentParser(description='XOR Encryptor')
    parser.add_argument('-i', dest='filename', type=str, required=True, help='Input File')
    parser.add_argument('-o', dest='fileout', type=str, required=False, help='Output File')
    parser.add_argument('-k', dest='key', type=str, required=True, help='Key')
    return parser.parse_args()

def readfile(filename):
    with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    return contents


def xorcrypt(data, key):
    no_of_itr = len(data)
    result = ""
    for i in range(no_of_itr):
        current = data[i]
        current_key = key[i%len(key)]
        result += chr(ord(current) ^ ord(current_key))     
    return result

if __name__ == '__main__':
    args = get_args()

    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    data = readfile(args.filename)

    dataxor = xorcrypt(data, args.key)


if args.fileout == None:  
    head,tail = ntpath.split(args.filename)
    sc_filename = tail.split('.')[0]+'.xor'
    sc_filepath = os.path.join(os.getcwd(),sc_filename)
    fileb = open(sc_filepath,'w')
    fileb.write(dataxor)
    fileb.close()
else:
    sc_filename = args.fileout
    sc_filepath = os.path.join(os.getcwd(),sc_filename)
    fileb = open(sc_filepath,'w')
    fileb.write(dataxor)
    fileb.close()
    
    
print(f"[+] XOR version is written to:\n    {sc_filepath}")
