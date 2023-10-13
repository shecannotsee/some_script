import sys
import textwrap

# 获取命令行参数
# module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent('''
//
// Created by shecannotsee on 23-10-13.
//

#ifndef PLACEHOLDER_NAME_H
#define PLACEHOLDER_NAME_H

class placeholder_name {
 public:
  int add(int p1, int p2) {
    int ret = p1 + p2;
    return ret;
  }
};

#endif // PLACEHOLDER_NAME_H

''')

print(code)
