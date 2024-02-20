
import os
import random


# 特定的目录名列表
DATASET_NAMES = [
    "hotpotwikiqa_mixup", "loogle_SD_mixup", "loogle_CR_mixup", "loogle_MIR_mixup", \
    "multifieldqa_en_mixup", "multifieldqa_zh_mixup", "factrecall_en", "factrecall_zh", \
    "cmrc_mixup", "lic_mixup", "dureader_mixup"
]

# 遍历目录名列表，为每个目录创建一个目录及同名的python文件
for dir in DATASET_NAMES:
    # 创建目录
    directory=f"lveval{dir}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 在新建的目录下创建同名的python文件
    pyname=f"lveval_{dir}"
    hex_number = "{:06x}".format(random.randint(0, 0xFFFFFF))
    filename = os.path.join(directory, f"{pyname}_gen_{hex_number}.py")
    with open(filename, 'w') as f:
        f.write(f"print('Hello from {directory}')")

    filename = os.path.join(directory, f"{pyname}_gen.py")
    with open(filename, 'w') as f:
        f.write(f"hello!")