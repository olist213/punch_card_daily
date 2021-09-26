# 1-20

## 01-签到

简单，直接打开就有flag。

flag

```bash
flag{buu_ctf}
```

## 02-金三胖

> 提示：注意：得到的 flag 请包上 flag{} 提交

用mac自带的图片预览工具打开后，可对gif文件的每张图片进行查看。第21、51、79有相应的内容。

![image-20210921212709457](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921212709457.png)

![image-20210921212742501](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921212742501.png)

![image-20210921212802737](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921212802737.png)

windows可以使用GIFFrame工具。

flag

```bash
flag{he11ohongke}
```

## 03 二维码

下载得到QR_code.png图片，是一个二维码。

![image-20210921214006099](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921214006099.png)

扫码，提示secret is here：

![image-20210921214108115](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921214108115.png)

16进制编辑器打开，显示图片中还有压缩包文件。![image-20210921214250228](../../../../../Library/Application Support/typora-user-images/image-20210921214250228.png)

binwalk提取压缩包。

```python
binwalk -e QR_code.png
```

得到压缩包，压缩包需要密码，而下面给了个txt文件

![image-20210921214354328](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921214354328.png)

archpr压缩包密码暴力破解，获得密码：7639。

![image-20210921215439923](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921215439923.png)

flag:

```bash
CTF{vjpw_wnoei}
```

## 04 你竟然赶我走

解压后是一张图片。

![biubiu](https://raw.githubusercontent.com/olist213/olistimg/master/upic/biubiu.jpg)

010editor打开。

![image-20210921220349033](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921220349033.png)

flag:

```bash
flag{stego_is_s0_bor1ing}
```

## 05 N种方法解决

解压出文件，一个key.exe。

010editor打开是一串base64加密的字符串。

![image-20210921220759499](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921220759499.png)

利用网址：https://tool.chinaz.com/tools/imgtobase，base64还原成图片，得到一个二维码。

![image-20210921221034246](../../../../../Library/Application Support/typora-user-images/image-20210921221034246.png)

扫描二维码，得到flag。

![image-20210921221127802](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921221127802.png)

flag:

```bash
flag{dca57f966e4e4e31fd5b15417da63269}
```

## 06 大白

下载得到da bai.png。

> 提示：看不到图？ 是不是屏幕太小了 注意：得到的 flag 请包上 flag{} 提交

根据提示，应该修改了图片的高度。Windows下由于不会验证CRC，因此改任意大值均可。

![image-20210921223054462](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921223054462.png)

010editor打开，00 00 02 A7为宽度，00 00 01 00为高度。

![image-20210921223455425](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921223455425.png)

高度改为00 00 02 A7即可。

保存，重新打开。

![image-20210921223631740](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921223631740.png)

flag:

```bash
flag{He1l0_d4_ba1}
```

## 07 基础破解

> 提示：给你一个压缩包，你并不能获得什么，因为他是四位数字加密的哈哈哈哈哈哈哈。。。不对= =我说了什么了不得的东西。。 注意：得到的 flag 请包上 flag{} 提交

根据提示4位数字。archpr暴力破解。得到密码：2563。

![image-20210921230230577](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921230230577.png)

解压后，得到flag.txt文件，获取到`ZmxhZ3s3MDM1NDMwMGE1MTAwYmE3ODA2ODgwNTY2MWI5M2E1Y30=`。

![image-20210921230433939](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921230433939.png)

flag:

```bash
flag{70354300a5100ba78068805661b93a5c}
```

## 08 LSB

解压后获取图片。

![image-20210921230742867](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921230742867.png)

根据题目，lsb隐写。

![image-20210921231809673](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921231809673.png)

保存为png，得到二维码。

![222](https://raw.githubusercontent.com/olist213/olistimg/master/upic/222.png)

flag:

```bash
cumtctf{1sb_i4_s0_Ea4y}
```

## 09乌镇峰会种图

> 提示：乌镇互联网大会召开了，各国巨头汇聚一堂，他们的照片里隐藏着什么信息呢？

下载得到jpg文件，010editor打开。

![image-20210921232720922](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921232720922.png)

flag:

```bash
flag{97314e7864a8f62627b26f3f998c37f1}
```

## 10 文件中的秘密

> 提示：小明经常喜欢在文件中藏一些秘密。时间久了便忘记了，你能帮小明找到该文件中的秘密吗？

右键，图片属性。

![image-20210921233125409](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921233125409.png)

flag:

```bash
flag{870c5a72806115cb5439345d8b014396}
```

## 11 wireshark

> 提示：黑客通过wireshark抓到管理员登陆网站的一段流量包（管理员的密码即是答案) 

wireshark打开，过滤http包。

![image-20210921233442072](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921233442072.png)

获得password

> 提示：Form item: "password" = "ffb7567a1d4f4abdffdb54e022f8facd"

flag:

```bash
flag{ffb7567a1d4f4abdffdb54e022f8facd}
```

## 12 rar

> 提示：这个是一个rar文件，里面好像隐藏着什么秘密，但是压缩包被加密了，毫无保留的告诉你，rar的密码是4位纯数字。

根据提示4位数字的密码。archpr。解压密码：8795。

![image-20210921234103782](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921234103782.png)

flag:

```bash
flag{1773c5da790bd3caff38e3decd180eb7}
```

## 13 zip伪加密

一个zip压缩包，打开需要密码，zip伪加密，使用ZipCenOp.jar进行破解，直接覆盖原文件，解压即可。

```bash
java -jar .\ZipCenOp.jar r .\ee2f7f26-5173-4e7a-8ea4-e4945e6f04ff.zip
```

flag:

```bash
flag{Adm1N-B2G-kU-SZIP}
```

## 14 qr

打开是一个二维码图片，直接识别。

![image-20210921235243644](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921235243644.png)

flag:

```bash
Flag{878865ce73370a4ce607d21ca01b5e59}
```

## 15 被嗅探的流量

> 提示：某黑客潜入到某公司内网通过嗅探抓取了一段文件传输的数据，该数据也被该公司截获，你能帮该公司分析他抓取的到底是什么文件的数据吗？

wireshark打开，跟踪tcp流。

![image-20210921235817095](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210921235817095.png)

flag:

```bash
flag{da73d88936010da1eeeb36e945ec4b97}
```

## 16 ningen

> 提示：人类的科学日益发展，对自然的研究依然无法满足，传闻日本科学家秋明重组了基因序列，造出了名为ningen的超自然生物。某天特工小明偶然截获了日本与俄罗斯的秘密通信，文件就是一张ningen的特写，小明通过社工，知道了秋明特别讨厌中国的六位银行密码，喜欢四位数。你能找出黑暗科学家秋明的秘密么？ 

010editor打开，发现有压缩包。

![image-20210922000148741](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922000148741.png)

![image-20210922000209987](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922000209987.png)

根据提示，四位数字的密码。

![image-20210922000334127](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922000334127.png)

获取密码：8368。

flag:

```bash
flag{b025fc9ca797a67d2103bfbc407a6d5f}
```

## 17 镜子里面的世界

打开后是一张图片。

![steg](https://raw.githubusercontent.com/olist213/olistimg/master/upic/steg.png)

binwalk查看，存在压缩包。

![image-20210922200654960](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922200654960.png)

无内容。

![image-20210922200739471](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922200739471.png)

Stegsolve.jar继续查看，red plane0处，这里的特征是LSB隐写。

![image-20210922201301710](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922201301710.png)

获取key。

![image-20210922201437700](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922201437700.png)

flag:

```bash
flag{st3g0_saurus_wr3cks}
```

zsteg同样可以查看lsb隐写。

![image-20210922202118256](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922202118256.png)

## 18 小明的保险箱

> 提示：小明有一个保险箱，里面珍藏了小明的日记本，他记录了什么秘密呢？。。。告诉你，其实保险箱的密码四位纯数字密码。

打开后，一张图片。

![4a81409d-f24b-4915-adc9-304e6faf60f2](https://raw.githubusercontent.com/olist213/olistimg/master/upic/4a81409d-f24b-4915-adc9-304e6faf60f2.jpg)

binwalk解压。

![image-20210922203434947](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922203434947.png)

根据提示，四位数的解压密码，archpr破解rar密码。

![image-20210922204149484](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922204149484.png)

解压密码：7869。

flag:

```bash
flag{75a3d68bf071ee188c418ea6cf0bb043}
```

## 19 爱因斯坦

打开一张图片。

![misc2](https://raw.githubusercontent.com/olist213/olistimg/master/upic/misc2.jpg)

010editor打开，发现存在zip压缩包文件。![image-20210922205610414](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922205610414.png)

提取出压缩文件，发现有压缩密码，查看图片的属性，发现密码：

![image-20210922210550733](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922210550733.png)

解压获取flag。

flag:

```bash
flag{dd22a92bf2cceb6c0cd0d6b83ff51606}
```

## 20 easycap

流量分析，追踪tcp流。

![image-20210922211210751](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922211210751.png)

flag:

```bash
flag{385b87afc8671dee07550290d16a8071}
