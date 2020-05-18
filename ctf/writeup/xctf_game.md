# wp

game

题目来源： ZSCTF

题目描述：菜鸡最近迷上了玩游戏，但它总是赢不了，你可以帮他获胜吗

## 方法1 使用od爆破

载入od中，插件-中文搜索-智能搜索，ctrl+F找flag，"done the flag is"。

往上找到push ebp，从下面的跳转来自，向回跳 。

看到地址下方显示，调用来自
```
0031E940=a0f2af98.0031E940
本地调用来自 0031F66C -------右击这里。跳。

```
发现一堆判断，是0到8的。到最上面的判断。。


```asm
0031F5C9  |.  B8 01000000   |mov eax,0x1
0031F5CE  |.  6BC8 00       |imul ecx,eax,0x0
0031F5D1  |.  0FB691 282E3F>|movzx edx,byte ptr ds:[ecx+0x3F2E28]
0031F5D8  |.  83FA 01       |cmp edx,0x1         ; 判断1
0031F5DB     /0F85 90000000 jnz a0f2af98.0031F671 ; 4. 点击这里，按空格 从这里改一下，跳到0031F66C关键call，运行即可得flag
0031F5E1  |. |B8 01000000   |mov eax,0x1
0031F5E6  |. |c1e0 00       |shl eax,0x0
0031F5E9  |. |0FB688 282E3F>|movzx ecx,byte ptr ds:[eax+0x3F2E28]
0031F5F0  |. |83F9 01       |cmp ecx,0x1           
0031F5F3  |. |75 7C         |jnz short a0f2af98.0031F671
0031F5F5  |. |B8 01000000   |mov eax,0x1
0031F5FA  |. |D1E0          |shl eax,1
0031F5FC  |. |0FB688 282E3F>|movzx ecx,byte ptr ds:[eax+0x3F2E28]
0031F603  |. |83F9 01       |cmp ecx,0x1
0031F606  |. |75 69         |jnz short a0f2af98.0031F671
0031F608  |. |B8 01000000   |mov eax,0x1
0031F60D  |. |6BC8 03       |imul ecx,eax,0x3
0031F610  |. |0FB691 282E3F>|movzx edx,byte ptr ds:[ecx+0x3F2E28]
0031F617  |. |83FA 01       |cmp edx,0x1
0031F61A  |. |75 55         |jnz short a0f2af98.0031F671
0031F61C  |. |B8 01000000   |mov eax,0x1
0031F621  |. |C1E0 02       |shl eax,0x2
0031F624  |. |0FB688 282E3F>|movzx ecx,byte ptr ds:[eax+0x3F2E28]
0031F62B  |. |83F9 01       |cmp ecx,0x1
0031F62E  |. |75 41         |jnz short a0f2af98.0031F671
0031F630  |. |B8 01000000   |mov eax,0x1
0031F635  |. |6BC8 05       |imul ecx,eax,0x5
0031F638  |. |0FB691 282E3F>|movzx edx,byte ptr ds:[ecx+0x3F2E28]
0031F63F  |. |83FA 01       |cmp edx,0x1
0031F642  |. |75 2D         |jnz short a0f2af98.0031F671
0031F644  |. |B8 01000000   |mov eax,0x1
0031F649  |. |6BC8 06       |imul ecx,eax,0x6       ; 3. 判断6
0031F64C  |. |0FB691 282E3F>|movzx edx,byte ptr ds:[ecx+0x3F2E28]
0031F653  |. |83FA 01       |cmp edx,0x1
0031F656  |. |75 19         |jnz short a0f2af98.0031F671
0031F658  |. |B8 01000000   |mov eax,0x1
0031F65D  |. |6BC8 07       |imul ecx,eax,0x7         ; 2. 判断7
0031F660  |. |0FB691 282E3F>|movzx edx,byte ptr ds:[ecx+0x3F2E28]
0031F667  |. |83FA 01       |cmp edx,0x1
0031F66A  |. |75 05         |jnz short a0f2af98.0031F671
0031F66C  |. \E8 4384FFFF   |call a0f2af98.00317AB4   ; 1. 现在在这里，输出flag call的，向上分析。
0031F671  |>^ E9 85FEFFFF   \jmp a0f2af98.0031F4FB
```

## 方法2 静态分析解码

IDA, Shift+F12 , Ctrl+F, flag,找到 done the flag is 。双击跳入

`.rdata:0050B0F0 aDoneTheFlagIs  db 'done!!! the flag is ',0`

光标移到 aDoneTheFlagIs按X，Enter。跳到了关键处。。。

前面定义了100多个变量。后面是关键语句。
```c
  for ( i = 0; i < 56; ++i )
  {
    *(&v2 + i) ^= *(&v59 + i); // *(&v59 + i) --- v59地址取第i个字符 和  v2开始的第i个字符异或
    *(&v2 + i) ^= 0x13u; // v2开始的第i个字符 和 0x13 异或
  }
```

```python
lst1 = [123, 32, 18, 98, 119, 108, 65, 41, 124, 80, 125, 38, 124, 111, 74, 49, 83, 108, 94, 108, 84, 6, 96, 83, 44, 121, 104, 110, 32, 95, 117, 101, 99, 123, 127, 119, 96, 48, 107, 71, 92, 29, 81, 107, 90, 85, 64, 12, 43, 76, 86, 13, 114, 1, 117, 126, 0]
lst2 = [18,64,98,5,2,4,6,3,6,48,49,65,32,12,48,65,31,78,62,32,49,32,1,57,96,3,21,9,4,62,3,5,4,1,2,3,44,65,78,32,16,97,54,16,44,52,32,64,89,45,32,65,15,34,18,16,0]

print(len(lst1))
print(len(lst2))

for i in range(56):
    lst1[i] ^= lst2[i]
    lst1[i] ^= 0x13

print(''.join(chr(x) for x in lst1))

# zsctf{T9is_tOpic_1s_v5ry_int7resting_b6t_others_are_n0t}
```

## 方法3 ida keypatch

1.伪代码窗口中 选中要使用Patch的位置，

    1.1 直接Ctrl+Alt+K 或
    1.2 按Tab, 进入反汇编窗口,  菜单 Edit-KeyPatch (Ctrl+Alt+K)

2. 修改，菜单 Edit-"Patch Program" - Apply Patches to input file.

我们在一个不重要的call的位置，直接调重要call

sub458054是输出一些`'----------'`，字符串的，我们这里Ctrl+Alt+K直接改成调 457ab4，就是输出flag的。

然后 菜单  Edit-"Patch Program" - Apply Patches to input file.

![Alt text](xctf_game.png "Optional title")
