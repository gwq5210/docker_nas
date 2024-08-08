#!/usr/bin/python3

import os
import sys

def copy_dir_files(dir_name: str):
    print(dir_name)
    if not os.path.isdir(dir_name):
        print(f"{dir_name}不是文件夹")
        return
    sub_dir_names = os.listdir(dir_name)
    sub_dir_names.sort()
    cp_cmd_str = ""
    all_file_paths = set()
    for sub_dir_name in sub_dir_names:
        sub_dir_path = os.path.join(dir_name, sub_dir_name)
        if os.path.isdir(sub_dir_path):
            file_names = os.listdir(sub_dir_path)
            file_names.sort()
            for file_name in file_names:
                file_path = os.path.join(sub_dir_path, file_name)
                if os.path.isfile(file_path):
                    print(f"{file_path}是文件，复制到{dir_name}")
                    src_file_path = os.path.join(sub_dir_path, file_name)
                    dst_file_path = os.path.join(dir_name, file_name)
                    if dst_file_path in all_file_paths:
                        print(f"{dst_file_path}已存在，跳过")
                    else:
                        cp_cmd_str += f"cp {src_file_path} {dst_file_path}\n"
                        all_file_paths.add(dst_file_path)
                else:
                    print(f"{file_path}不是文件，跳过")
        else:
            print(f"{sub_dir_path}不是文件夹，跳过")
    print("生成的命令如下:\n")
    print(cp_cmd_str)

def main():
    if len(sys.argv) == 0:
        print("请输入文件夹列表")
        return
    for dir_name in sys.argv[1:]:
        copy_dir_files(dir_name)

if __name__ == '__main__':
    main()

