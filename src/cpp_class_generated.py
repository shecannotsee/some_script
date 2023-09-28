import sys
import textwrap


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
def class_generate():
    # 获取命令行参数
    class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")
    code = textwrap.dedent(f'''
class {class_name} {{
 public:
  // copy:off
  {class_name}(const {class_name}&) = delete;
  {class_name}& operator=(const {class_name}&) = delete;
  // move:off
  {class_name}({class_name}&&) = delete;
  {class_name}& operator=({class_name}&&) = delete;
  // destructors
  ~{class_name}() = default;
  // constructors
  {class_name}() = default;

 private:
  // data
 public:
  // interface

}};
    ''')
    print(code)
# def class_generate():


def main():
    class_generate()
# def main():


if __name__ == "__main__":
    main()



