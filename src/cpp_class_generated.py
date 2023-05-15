# 拷贝和移动参考
# class vector {
# private:
#     // ......
# public:
# vector() = default;
# ~vector() = default;
# // copy
# vector(const vector& x) = default;
# vector& operator=(const vector& x) = default;
# // move
# vector(vector&&) = default;
# vector& operator=(vector&& x) = default;
# public:
# // ......
# };
import sys

# 获取命令行参数
class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

code = ""
code += "class "+ class_name + " {\n"
code += " public:\n"
code += "  // copy:off\n"
code += "  "+class_name+"(const "+class_name+"&) = delete;\n"
code += "  "+class_name+"& operator=(const "+class_name+"&) = delete;\n"
code += "  // move:off\n"
code += "  "+class_name+"("+class_name+"&&) = delete;\n"
code += "  "+class_name+"& operator=("+class_name+"&&) = delete;\n"
code += "  //destructors\n"
code += "  ~"+class_name+"() = default;\n"
code += "  //constructors\n"
code += "  "+class_name+"() = default;\n"
code += " private:\n"
code += "  // data\n"
code += " public:\n"
code += "  // interface\n"
code += "\n"
code += "};"

print(code)



