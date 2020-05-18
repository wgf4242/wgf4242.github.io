ida分析后

发现了'Oo.0'这几个字符。。每个if最终进入label15

```c
LABEL_15:
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  const char *v3; // rsi
  signed __int64 v4; // rbx
  signed int v5; // eax
  char v6; // bp
  char v7; // al
  const char *v8; // rdi
  __int64 v10; // [rsp+0h] [rbp-28h]

  v10 = 0LL;
  puts("Input flag:");
  scanf("%s", &s1, 0LL);
  if ( strlen(&s1) != 24 || strncmp(&s1, "nctf{", 5uLL) || *(&byte_6010BF + 24) != 125 )// 匹配nctf{***} 长度为24
  {
LABEL_22:
    puts("Wrong flag!");
    exit(-1);
  }
  v4 = 5LL;
  if ( strlen(&s1) - 1 > 5 )
  {
    while ( 1 )
    {
      v5 = *(&s1 + v4);                         // 第1个字符
      v6 = 0;
      if ( v5 > 78 )
    ##   {
        v5 = v5;
        if ( v5 == 'O' ) // 显示的79按R显示出字符。
        {
          v7 = sub_400650(&v10 + 1);
          goto LABEL_14;
        }
        if ( v5 == 'o' )
        {
          v7 = sub_400660(&v10 + 1);
          goto LABEL_14;
        }
      }
      else
      {
        v5 = v5;
        if ( v5 == '.' )
        {
          v7 = sub_400670(&v10);
          goto LABEL_14;
        }
        if ( v5 == '0' )
        {
          v7 = sub_400680(&v10, v3);
LABEL_14:
          v6 = v7;
          goto LABEL_15;
        }
      }
LABEL_15:
      v3 = HIDWORD(v10);
      if ( !sub_400690(asc_601060, SHIDWORD(v10), v10) )
        goto LABEL_22;
      if ( ++v4 >= strlen(&s1) - 1 )
      {
        if ( v6 )
          break;
LABEL_20:
        v8 = "Wrong flag!";
        goto LABEL_21;
      }
    }
  }
  if ( asc_601060[8 * v10 + SHIDWORD(v10)] != 35 )
    goto LABEL_20;
  v8 = "Congratulations!";
LABEL_21:
  puts(v8);
  return 0LL;
}
```

```c
__int64 __fastcall sub_400690(__int64 a1, int a2, int a3)
{
  __int64 result; // rax

  result = *(a1 + a2 + 8LL * a3);
  LOBYTE(result) = result == 32 || result == 35;
  return result;
}
```
a1 = `'  *******   *  **** * ****  * ***  *#  *** *** ***     *********'`

8LL*a3 发现是个二维数组，v3行。v2列。

SHIDWORD(v10)=>a2, 进入下一结点 , v10=>a3,

得知这点，从上面分析可知：

就将四个函数点进去就可以判断方向了。相对应，其他方向，举例

```c
        if ( v5 == 'O' )
        {
          v7 = sub_400650(&v10 + 1); // 行的下一位，传的是列？
          goto LABEL_14;
        }

=======>
bool __fastcall sub_400650(_DWORD *a1)
{
  int v1; // eax

  v1 = (*a1)--; // 说明'O' => sub_400650 => 列值-1, 那是左
  return v1 > 0;
}
```
同样分析其他， O左 o右 . 上 0下

a1是迷宫。前往#号

```
  ******
*   *  *
*** * **
**  * **
*  *#  *
** *** *
**     *
********
```

最后得到 flag: nctf{o0oo00O000oooo..OO}
