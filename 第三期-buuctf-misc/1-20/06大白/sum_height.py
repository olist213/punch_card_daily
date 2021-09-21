# coding: utf-8

## 计算精确的高度，使用下面的脚本

import struct
import binascii
from crypto.Util.number import bytes_to_long

img = open('./dabai.png', 'rb').read()

for i in range(0xFFFF):
    stream = img[12:20] + struct.pack('>i', i) + img[24:29]
    crc = binascii.crc32(stream)
    if crc == bytes_to_long(img[29:33]):
        print(hex(i))