#!/usr/bin/env python
from pwn import *
import string

s = open( 'KingMaker' ).read()
new = open( './KingMaker.patched' , 'w+' )

k = [ 'lOv3' , 'D0l1' , 'HuNgRYT1m3' , 'F0uRS3aS0n' , 'T1kT4kT0Kk' ]

p = [
    (0x330f,0xf0,1) , (0x33ff,0x1e,1) , (0x341d,0xf0,1) , (0x32c0,0x1e,1) , (0x32de,0x31,1) , (0x3197,0x129,1) , (0x30d4,0xc3,1),
    (0x2D55,0xfa,2) , (0x2c25,0x112,2) , (0x2d37,0x1e,2) , (0x27e9,0x44,2) , (0x29b9,0xe6,2) , (0x2b2b,0xfa,2) , (0x271c,0xcd,2) , (0x28b5,0xe6,2) , (0x299b,0x1e,2) , (0x2a9f,0x4e,2) , (0x2aed,0x3e,2),
    (0x282d,0x44,2) , (0x2871,0x44,2),
    (0x20e2,0x18d,3) , (0x201f,0xc3,3),
    (0x1b0a,0xf0,4) , (0x19f2,0xfa,4) , (0x1aec,0x1e,4) , (0x192c,0xa8,4) , (0x19d4,0x1e,4) , (0x16d0,0xc3,4),
    (0x11BB,0x131,5) , (0xf25,0xDC,5) , (0x108b,0x130,5) , (0xde7,0x120,5) , (0xf07,0x1e,5) , (0x1001,0x1e,5) , (0x101f,0x4e,5) , (0x106d,0x1e,5) , (0xC8C,0x15B,5)
]
p.sort( key=lambda x:x[0] )

ss = ''
now = 0
for i , l , kn in p:
    ss += s[now:i]
    for j in xrange( l ):
        ss += chr( ord( s[ i + j ] ) ^ ord( k[ kn - 1 ][j % len( k[ kn - 1 ] )] ) )
    now = i + l

ss += s[now:]

new.write(ss)
new.close()




