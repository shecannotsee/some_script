import sys
import textwrap

# 获取命令行参数
# module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent('''#ifndef GLOBAL_TEST_SET_H
#define GLOBAL_TEST_SET_H

#include <string>
#include <gtest/gtest.h>
#include <gmock/gmock.h>

const std::string RESET_COLOR   = "\033[0m";
const std::string RED_COLOR     = "\033[31m";
const std::string GREEN_COLOR   = "\033[32m";
const std::string YELLOW_COLOR  = "\033[33m";
const std::string PURPLE_COLOR  = "\033[35m";
const std::string BLUE_COLOR    = "\033[34m";

#endif // GLOBAL_TEST_SET_H''')

print(code)
