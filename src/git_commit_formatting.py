import textwrap


def commit_prompt():
    prompt_content = textwrap.dedent('''
- feat: (new feature)提交新的功能
- fix: (fix bug)解决了bug
- docs: (documentation)修改的是文档相关的内容
- style: 格式修改。没有修改代码逻辑，比如格式化，换行，清除空白,删除分号等
- refactor: 重构代码，既没有新增功能，也没有修复bug。比如提取某段代码为一个方法、重构某个功能
- perf: (performance)性能、体验优化等
- test: 新增test用例或修改现有测试用例
- build: 构建过程或者外部依赖的修改
- chore: 其他修改修改
    ''')
    print(prompt_content)
# def commit_prompt():


def main():
    commit_prompt()
# def main():


if __name__ == "__main__":
    main()
