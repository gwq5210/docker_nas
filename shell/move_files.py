#!/usr/bin/python3

import os
import sys

def copy_dir_files(dir_name: str):
    print(dir_name)
    if not os.path.isdir(dir_name):
        print(f"{dir_name}不是文件夹")
        return
    sub_dir_names = os.listdir(dir_name)
    suffixs = set([".mp4", ".mkv"])
    sub_dir_names.sort()
    all_file_paths = set()
    for sub_dir_name in sub_dir_names:
        sub_dir_path = os.path.join(dir_name, sub_dir_name)
        if os.path.isdir(sub_dir_path):
            need_move = False
            match_suffix = None
            for suffix in suffixs:
                if sub_dir_name.endswith(suffix):
                    match_suffix = suffix
                    need_move = True
                    break
            if need_move:
                move_cmd = f"mv {sub_dir_path} {sub_dir_path[:-len(match_suffix)]}"
                print(move_cmd)
                os.system(move_cmd)

    sub_dir_names = os.listdir(dir_name)
    for sub_dir_name in sub_dir_names:
        sub_dir_path = os.path.join(dir_name, sub_dir_name)
        if os.path.isdir(sub_dir_path):
            file_names = os.listdir(sub_dir_path)
            file_names.sort()
            for file_name in file_names:
                file_path = os.path.join(sub_dir_path, file_name)
                if os.path.isfile(file_path):
                    if file_name.startswith("."):
                        print(f"{file_path}是隐藏文件，跳过")
                        continue
                    print(f"{file_path}是文件，复制到{dir_name}")
                    src_file_path = os.path.join(sub_dir_path, file_name)
                    dst_file_path = os.path.join(dir_name, file_name)
                    if dst_file_path in all_file_paths:
                        print(f"{dst_file_path}已存在，跳过")
                    else:
                        mv_cmd = f"cp {src_file_path} {dst_file_path}\n"
                        print(mv_cmd)
                        os.system(mv_cmd)
                        all_file_paths.add(dst_file_path)
                else:
                    print(f"{file_path}不是文件，跳过")
        else:
            print(f"{sub_dir_path}不是文件夹，跳过")
    print(f"总数: {len(all_file_paths)}")

def main():
    if len(sys.argv) == 0:
        print("请输入文件夹列表")
        return
    for dir_name in sys.argv[1:]:
        copy_dir_files(dir_name)

if __name__ == '__main__':
    main()

