# RSA
# n, c 求 明文 , 已经 PQ积 官文 求明文

import gmpy2
# 1. 打开rsa tools
# 2. 填n,e求pq， 填好点Factor N => Calc D.
p = 13574881
q = 23781539
n = 322831561921859

e = 23
c = 0xdc2eeeb2782c
d = gmpy2.invert(e,(p-1)*(q-1))
p = pow(c ,d ,n)  # M = pow(C ,d , n) = C ** d % n
p = hex(p)
print(p)
print(bytearray.fromhex(p[2:]).decode('latin'))

