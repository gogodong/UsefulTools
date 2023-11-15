import re
import os


def use_regex(input_text):
    pattern = re.compile(r"([A-Za-z]+(\.[A-Za-z]+)+).*S\d\dE\d\d", re.IGNORECASE)
    return pattern.match(input_text).group()


# 测试效果
# print(use_regex("The.Boys.2019.S01E08.1080p.AMZN.WEB-DL.H264.DDP5.1-NexusWEB.mkv"))

# 指定文件夹
folder_path = input("请输入文件夹路径：")


# 获取文件夹下文件名称
file_names = os.listdir(folder_path)

# 重命名
for old_name in file_names:
    new_name = use_regex(old_name) + os.path.splitext(old_name)[-1]
    os.chdir(folder_path)
    os.rename(old_name, new_name)
