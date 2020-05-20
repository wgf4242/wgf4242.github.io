# BUUCTF WriteUp

## reverse

### reverse3
ida 中shift+F12.看到 `'*11110100001010000101111#'`

运行题目看出来是上下左右走迷宫的。

读代码慢慢弄也行。有经验直接这就是5*5的迷宫。 根据题目方向走出来。

```
*1111
01000
01010
00010
1111#
```
方向
```
1 up
2 down
3 left
4 right
```

### re-刮开有奖

拖入ida分析一下，有些代码手动标记转换一下。下面是已经分析好的。 [参考链接](https://blog.csdn.net/Palmer9/article/details/103078394)

```c
BOOL __stdcall DialogFunc(HWND hDlg, UINT a2, WPARAM a3, LPARAM a4)
{
  const char *v4; // esi
  const char *v5; // edi
  int c[0]; // [esp+8h] [ebp-20030h] 点进来看地址是连续的。
  int c[1]; // [esp+Ch] [ebp-2002Ch]
  int c[2]; // [esp+10h] [ebp-20028h]
  int c[3]; // [esp+14h] [ebp-20024h]
  int c[4]; // [esp+18h] [ebp-20020h]
  int c[5]; // [esp+1Ch] [ebp-2001Ch]
  int c[6]; // [esp+20h] [ebp-20018h]
  int c[7]; // [esp+24h] [ebp-20014h]
  int c[8]; // [esp+28h] [ebp-20010h]
  int c[9]; // [esp+2Ch] [ebp-2000Ch]
  int c[10]; // [esp+30h] [ebp-20008h]
  CHAR String[0]; // [esp+34h] [ebp-20004h] 点进来看地址是连续的。
  char String[1]; // [esp+35h] [ebp-20003h]
  char String[2]; // [esp+36h] [ebp-20002h]
  char String[3]; // [esp+37h] [ebp-20001h]
  char String[4]; // [esp+38h] [ebp-20000h]
  char String[5]; // [esp+39h] [ebp-1FFFFh]
  char String[6]; // [esp+3Ah] [ebp-1FFFEh]
  char String[7]; // [esp+3Bh] [ebp-1FFFDh]
  char s[0]; // [esp+10034h] [ebp-10004h] 点进来看地址是连续的。
  char s[1]; // [esp+10035h] [ebp-10003h]
  char s[2]; // [esp+10036h] [ebp-10002h]

  if ( a2 == 272 )
    return 1;
  if ( a2 != 273 )
    return 0;
  if ( a3 == 1001 )
  {
    memset(&String[0], 0, 0xFFFFu);
    GetDlgItemTextA(hDlg, 1000, &String[0], 0xFFFF);
    if ( strlen(&String[0]) == 8 )
    {
      c[0] = 'Z';
      c[1] = 'J';
      c[2] = 'S';
      c[3] = 'E';
      c[4] = 'C';
      c[5] = 'a';
      c[6] = 'N';
      c[7] = 'H';
      c[8] = '3';
      c[9] = 'n';
      c[10] = 'g';
      sub_4010F0(&c[0], 0, 10);
      memset(&s[0], 0, 0xFFFFu);
      s[0] = String[5];
      s[2] = String[7];
      s[1] = String[6];
      v4 = base64(&s[0], strlen(&s[0]));
      memset(&s[0], 0, 0xFFFFu);
      s[1] = String[3];
      s[0] = String[2];
      s[2] = String[4];
      v5 = base64(&s[0], strlen(&s[0]));
      if ( String[0] == c[0] + '"'
        && String[1] == c[4]
        && 4 * String[2] - 141 == 3 * c[2]
        && String[3] / 4 == 2 * (c[7] / 9)
        && !strcmp(v4, "ak1w")
        && !strcmp(v5, "V1Ax") )
      {
        MessageBoxA(hDlg, "U g3t 1T!", "@_@", 0);
      }
    }
    return 0;
  }
  if ( a3 != 1 && a3 != 2 )
    return 0;
  EndDialog(hDlg, a3);
  return 1;
}
```


4010F0加密部分, 可以直接编译输出一下。 结果是 `3CEHJNSZagn`

```c
 _BYTE *__cdecl sub_401000(int a1, int a2)
 {
   int v2; // eax
   int v3; // esi
   size_t v4; // ebx
   _BYTE *v5; // eax
   _BYTE *v6; // edi
   int v7; // eax
   _BYTE *v8; // ebx
   int v9; // edi
   signed int v10; // edx
   int v11; // edi
   signed int v12; // eax
   signed int v13; // esi
   _BYTE *result; // eax
   _BYTE *v15; // [esp+Ch] [ebp-10h]
   _BYTE *v16; // [esp+10h] [ebp-Ch]
   int v17; // [esp+14h] [ebp-8h]
   int v18; // [esp+18h] [ebp-4h]
 
   v2 = a2 / 3;
   v3 = 0;
   if ( a2 % 3 > 0 )
     ++v2;
   v4 = 4 * v2 + 1;
   v5 = malloc(v4);
   v6 = v5;
   v15 = v5;
   if ( !v5 )
     exit(0);
   memset(v5, 0, v4);
   v7 = a2;
   v8 = v6;
   v16 = v6;
   if ( a2 > 0 )
   {
     while ( 1 )
     {
       v9 = 0;
       v10 = 0;
       v18 = 0;
       do
       {
         if ( v3 >= v7 )
           break;
         ++v10;
         v9 = *(unsigned __int8 *)(v3++ + a1) | (v9 << 8);
       }
       while ( v10 < 3 );
       v11 = v9 << 8 * (3 - v10);
       v12 = 0;
       v17 = v3;
       v13 = 18;
       do
       {
         if ( v10 >= v12 )
         {
           *((_BYTE *)&v18 + v12) = (v11 >> v13) & 0x3F;
           v8 = v16;
         }
         else
         {
           *((_BYTE *)&v18 + v12) = 64;
         }
         *v8++ = byte_407830[*((char *)&v18 + v12)];
         // 这里看了一下 byte_407830 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
         // 猜一下是base64，慢慢分析也行
         v13 -= 6;
         ++v12;
         v16 = v8;
       }
       while ( v13 > -6 );
       v3 = v17;
       if ( v17 >= a2 )
         break;
       v7 = a2;
     }
     v6 = v15;
   }
   result = v6;
   *v8 = 0;
   return result;
 }
```

对照着分析一下，然后跑python
```python
import base64
b = '3CEHJNSZagn'
v4 = base64.b64decode(b'ak1w').decode()
v5 = base64.b64decode(b'V1Ax').decode()
print(v4) # String[5,6,7]
print(v5) # String[2,3,4]

s0 = chr(ord(b[0]) + ord('"'))
s1 = b[4];
flag = 'flag{{{}}}'.format(''.join([s0,s1,v5,v4]))
print(flag)
# flag{UJWP1jMp}
```

## Misc

### 面具下的flag

`foremost mianju.jpg` 分享出zip文件。

zip伪加密。ZipCenOp解压一下。

解压出vmdk文件。

重点：一定要在linux下, 否则缺少文件。 7z x filename

解压出来。 key1 brainfuck, key2 ook 解码即可。