import os
import subprocess

def use_clang_tidy(src_dir: str, log_file: str):
    # 获取目标文件
    files = []
    for root, _, filenames in os.walk(src_dir):
        for filename in filenames:
            if filename.endswith(('.cpp', '.c')):
                files.append(os.path.join(root, filename))

    # 检查目标文件
    if files:
        # 构建 clang-tidy 命令
        clang_tidy_cmd = [
                             'clang-tidy',
                             '-header-filter=.*',  # 显示所有头文件的警告
                             '-system-headers',    # 包括系统头文件中的警告
                         ] + files + [
                             '--',
                             '-std=c++17',         # 编译器选项
                         ]

        # 运行 clang-tidy 并捕获输出
        result = subprocess.run(clang_tidy_cmd, capture_output=True, text=True)

        # 将结果写入日志文件
        with open(log_file, 'w') as log:
            log.write(result.stdout)
            log.write(result.stderr)

        print(f"Warnings and errors have been written to {log_file}.")
    else:
        print("No target files found.")
