#### 一些规则

默认使用linux下换行符\n

#### cpp_class_generated.py

生成一个c++类，并且默认禁止移动和复制

```c++
// python3 cpp_class_generated.py foo
class foo {
 public:
  // copy:off
  foo(const foo&) = delete;
  foo& operator=(const foo&) = delete;
  // move:off
  foo(foo&&) = delete;
  foo& operator=(foo&&) = delete;
  //destructors
  ~foo();
  //constructors
  foo();
 private:
  // data
 public:
  //interface

};
```

