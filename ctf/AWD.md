[TOC]

����ı�����:
ID:HSCTF
HSCTF 7 https://hsctf.com/
����16Сʱ18�ֺ����������ʱ��6��8����
ID:Defenit
2020 Defenit CTF https://ctf.defenit.kr/about
����1Сʱ18�ֺ�ʼ����ʼʱ�����17����������ʱ��7��17����
ID:RA
Really Awesome CTF 2020 https://ractf.co.uk/
����9Сʱ18�ֺ�ʼ����ʼʱ��6��1����������ʱ��10��1����
ID:BwtPwn
BatPwn - BSides Ahmedabad CTF 2020 https://bsidesahmedabad.in/BATPWN/
����13Сʱ18�ֺ�ʼ����ʼʱ��6��5����������ʱ��7��5����
ID:CyberHack
CyberHackCTF 2020 https://cyberhack.tech/
����1��2Сʱ��ʼ����ʼʱ��6��18��룬����ʱ��7��18���


SQL labs



# CTF���¹�����

## SSH��¼�޸�����

### ����Web��Ϣ

### ��WAF
### �ļ����

log���� - ���ñ��˼ҵĽű�

### �˿�ɨ��

## ��������

RouterScan.exe , HttpScan.py

### �˿�ɨ�� - Nmap

�������

### �ںв���

* Ŀ¼ɨ��
    
    * ���ű��� - k8һ�仰����
    * k8fly

#### Ȩ��ά��

��ֲ������(�ļ�����) - �������� - �����ϴ�+��������

    �������������� 1.ɱ���� 2.����д��3.��Apache�������ֿ۷֣�
    �������md5����ֹ����
    echo system("curl 10.0.0.1") => ������ȡ

����shell

��Ϣ����

     �ļ�ǰ���.����1.php => .1.php
     ���Ŀ¼������asp, jsp�������¡�

[AWD���±���¼](https://www.fuzzer.xyz/2019/04/02/AWD����׼��ָ��/)

#### ����ۼ�

var/log, ��־
bash_history�� ��

# AWD 
ABC3��

1.dumpĿ¼��Դ�롣���������¡� /var/www/html��
2.D��ɨһ�¡�
2.1 ͬʱ��һ���� nmap�ȹ��� ��Ϣ�ռ�
�رշǱ�Ҫ�˿ڣ����»����˿ڡ�
����Ŀ¼�ṹ��
׼��waf�����ϣ�Ȼ������Լ������ķ��񣨲�Ҫ���Լ������������������췽��ʱ��check����������û�С�
���ļ���غ��������(Wireshark���һ��)
��/var/log �����־��

   
�Զ��������ύ�ű�, curl, getflag,

## ��������

3. ��WAF���ϼ�ء�ֻ����Ҫ�˿�

����WAF

�����ļ���ؽű�

�������̼�ؽű�������������־��¼��

[AWD������֮����©��FIX����](https://www.freebuf.com/articles/web/208778.html)

## ��������

    ssh <-p �˿�>  �û���@IP
    scp �ļ�·��  �û���@IP�����·��
    tar -zcvf web.tar.gz /var/www/html
    pkill -kill -t <�û�tty>

�鿴�ѽ����������Ӽ�����

    netstat -antulp | grep EST

�鿴ָ���˿ڱ��ĸ�����ռ��

    lsof -i:�˿ں� ���� netstat -tunlpl | grep �˿ں�

������������

    kill PID
    killall <������>
    kill - <PID>

��ɱĳ��IP����ip�Σ� ��:

    iptables -I INPUT -s . j DROP 
    iptables -I INPUT-S ./ j DROP

��ֹ��ĳ������sshԶ�̷��ʵ�½����������123..

    iptable -t filter -A INPUT -s . p tcp -- dport j DROP

����mysql���ݿ�

    mysqldump -u �û��� -p���� ���ݿ��� > back.sql
    mysqldump --all-databases >> bak.sql

��ԭmysql���ݿ�

    mysql -u �û��� -p ���� ���ݿ��� < bak.sql
    find / *.php -perm
    awk -F: /etc/passwd
    crontab -l

������е�tcp����������״̬

    netstat --ant | awk | grep | sed -e -e | sort | uniq -c | sort -rn

�鿴ҳ���������ǰʮ��IP
    
    cat /var/1og/apache2/access.1og | cut -f1 -d | sort | uniq -c | sort -k -r | head

����ҳ���������ǰʮ��URL

    cat /var/log/apache2/access.log | cut -f4 -d | sort | uniq -c | sort -k -r | head

## ��Դ����

[AWD ��ԴС�ϼ�(��������)](https://neversec.top/20190415/how-to-awd.html)

[linux-kernel-exploits](https://github.com/SecWiki/linux-kernel-exploits)

[AWD�������ű�����](https://github.com/admintony/Prepare-for-AWD)

### ���ù���

    Burpsuite
    Sqlmap
    Nmap��masscan�� ������wpscan
    nc
    D�ܡ�Seay�� Rips�� ��ȫ��
    MobaXterm��Xshell�� Xftp
    �˵����Ͻ�
    Chrome��Firefox������
    Hackbar
    Kali
    Python�ĸ��ຯ���⡢�����

### ����ȽϹ���

BeyondCompare(Windows)

Kaleidoscope(MacOS)

### һ�仰ľ��

php,asp,aspx,jsp, �ڴ���

## ����׼��

��ǰ׼���ø���cmd��poc��exp(phpwin, phpcms, dz)

���и����Զ����ű��������и�ģ��