#!/usr/bin/env python3
import os
import codecs

images_dir = r'D:\nanjing\images'

# 用UTF-8读取目录
with os.scandir(images_dir) as entries:
    for entry in sorted(entries, key=lambda x: x.name):
        # 尝试用不同编码读取文件名
        name = entry.name
        try:
            # 尝试用GBK解码（Windows中文系统）
            decoded = name.encode('gbk').decode('utf-8', errors='ignore')
            print(f"  {name} -> try decode")
        except:
            pass
        print(f"  {name}")