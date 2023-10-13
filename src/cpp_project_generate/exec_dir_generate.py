import sys
import textwrap

# 获取命令行参数
# module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent('''// application.cpp
#include <iostream>

int main() {
  std::cout << "\\033[32m" << "application start" << "\\033[0m" << std::endl;

  std::cout << "\\033[32m" << "application done" << "\\033[0m" << std::endl;
  return 0;
}''')

print(code)
