#!/usr/bin/env python3
import os

# 获取images文件夹中所有文件
images_dir = r'D:\nanjing\images'
files = os.listdir(images_dir)

print("Images folder contents:")
for f in sorted(files):
    print(f"  {f}")