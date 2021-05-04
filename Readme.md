# Readme

## sports.py
Simple portscanner. Always needed in very restricted environments but python on the box. Copy and Paste or transfer how you like and get a basic idea about your 
environment.

Get Help
```
usage: ./sports.py [-h] [-l HOST] [-L HOSTLIST] [-Ps START_PORT]
                   [-Pe END_PORT] [-tc TIMEOUT_CONNECT] [-tr TIMEOUT_READ]

quick and dirty tcp portscanner

optional arguments:
  -h, --help            show this help message and exit
  -l HOST, --host HOST  host to check ports
  -L HOSTLIST, --hostlist HOSTLIST
                        hostlist run checks against
  -Ps START_PORT, --start-port START_PORT
                        start port (default:1)
  -Pe END_PORT, --end-port END_PORT
                        end port (default:1)
  -tc TIMEOUT_CONNECT, --timeout-connect TIMEOUT_CONNECT
                        timeout_connect
  -tr TIMEOUT_READ, --timeout-read TIMEOUT_READ
                        timeout_connect
```
Scan:  
```
./sports.py -Ps 80 -Pe 90 -l
 github.com -tc 1
github.com:80,OPEN
github.com:81,CLOSED,timeout('timed out')
[...]
github.com:90,CLOSED,timeout('timed out'
```
## fingerprint.py

Another day i tried to get the cert with openssl, convert it and get the fingerprint...had a shellscript...and finally decided to put this task to a simple and working
python script.

Get Help:

```
./fingerprint.py -h
usage: fingerprint by dash version v0.2 [-h] [-l HOST] [-p PORT]

get fingerprint from remote ssl layer

optional arguments:
  -h, --help            show this help message and exit
  -l HOST, --host HOST  host to get ssl cert from, default: 127.0.0.1
  -p PORT, --port PORT  port (default:443)
```
Fingerprint:  
```
./fingerprint.py -l imap.gmail.com -p 995

Results
-------
imap.gmail.com:995,md5:904AC8D5445AD06A8A10FFCD8B11BE16
imap.gmail.com:995,sha1:4259517CD4E48A289D332AB3F0AB52A366322824
imap.gmail.com:995,sha256:D5129635A050F63DD607FFA9271EEFAAB597C0975809765DAD253973FC554D25
imap.gmail.com:995,sha512:4CF1C747DA7F62335273A00328E92B8F3CD9CD2CB5832EF58FDC78DA11E84F245DDE107B5B666F7230B5A705B2E3E9D28BD9B91322EA6267EEE9B55E1737FA6D
```

## utime2date

Simple convert unix time to date

```
./utime2date.py 167466789
```

## jwtdec

Decode JWToken 

```
./jwtdec.py -t ey...
```
