#!/usr/bin/env python3
import os
import sys

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

images_dir = r'D:\nanjing\images'
for f in sorted(os.listdir(images_dir)):
    if f.endswith('.jpg'):
        print(f)