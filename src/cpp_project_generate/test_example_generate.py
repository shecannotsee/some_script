import sys
import textwrap

# 获取命令行参数
# module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent('''

#ifndef TEST_EXAMPLE_H
#define TEST_EXAMPLE_H

TEST(test_example,equal) {
  EXPECT_EQ(10,10);
}

#endif // TEST_EXAMPLE_H


''')

print(code)
