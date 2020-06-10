# TODO
sql怎样fuzz

sql 宽字节注入

DynELF泄露libc，而并不知道它究竟干了些什么。我就不一样，我连用都不会用。

用sage的ipython


曼彻斯特及差分曼彻斯特编码

png 校验 CRC

https://www.baidu.com/s?ie=UTF-8&wd=%E9%80%86%E5%90%91%20angr

ida符号插件

upper of 32 bit RFlags are reversed?

得到一个压缩包解压得到文件data.vmem放入kali使用内存取证工具volatility volatility -fdata.vmem imageinfo命令判断信息

使用ptofile 执行命令volatility-f data.vmem --profile=WinXPSP2x86 pslist查看进程信息

汇编语言转换 学习

    循环
    声明
    赋值
    ++和--
    加固定值，减固定值
    自定义函数的声明
    调用自定义函数，调用系统函数
    符号  >> 和 <<


针对RSA的攻击之 Coppersmith定理攻击
https://www.52pojie.cn/thread-653446-1-1.html

## TODO Crypto

sage库的使用

## TODO pwn

# radare2使用

r2 ./bof

aa分析

afl看函数 analysis function list

跳到main
s main
s 0x1234地址
V 看内存
VV 进入virtual mode，能看图

s sym.hidden
VV
看绿色 call sym.imp.system 参数是 bin/sh
s sym.main(转到main)


执行
./bof1

光标处按:提示:> 修改，
:> afvn改名字
local_10h 改为 input
:> afvn input local_10h

## gdb
fin, 跳出跟踪的函数 
gdb 使用finish命令（缩写fin）

b main 在main断点

p32 用32bit将数字转字符串
p64 用64bit将数字转字符串
