import sys
import textwrap
import re

# int fclose (FILE *__stream, int b)
# FILE *fopen (const char *__restrict __filename,
# const char *__restrict __modes)

# Split strings. like[const char *__restrict __filename] to [const char *__restrict] and [__filename]
def param_parse(param):
    # 使用空格分隔字符串，得到单词列表
    param_list_str = param.split()
    if len(param_list_str) > 0:
        param_name = param_list_str[-1]
        param_type = " ".join(param_list_str[:-1])
        if param_name[0] == "*":
            param_type += "*"
            param_name = param_name[1:]
        return param_type, param_name
    else:
        # 如果字符串为空，返回两个空字符串
        return "", ""
# def param_parse(input_string):

def parse_c_function(c_function_string):
    # get function return and name info
    function_return = ""
    function_name = ""
    match = re.search(r'[^()]+(?=\()', c_function_string)
    if match:
        function_return_name = match.group()
        function_return_name = function_return_name.split()
        function_return = function_return_name[0]
        function_name = function_return_name[1]
        if function_name[0] == "*":
            function_return += "*"
            function_name = function_name[1:]
    else:
        print("parse c function error")
        return None

    # get param info
    param_info_list = []
    match = re.search(r'\((.*?)\)', c_function_string)
    if match:
        # 获取匹配到的括号内的内容
        param_info = match.group(1).split(',')
        for param in param_info:
            param_info_list.append(param_parse(param))
    else:
        print("parse c function error")
        return None

    return {
        'function_name': function_name,
        'function_return': function_return,
        'function_params': param_info_list
    }
# def parse_c_function(declaration):

def get_input():
    c_function = ""
    input_lines = []
    print("input function [example int func(int a)]: use enter to end the input")
    while True:
        line = input()
        if not line:  # 如果输入为空（用户按下了 Enter 键）
            for argv in input_lines:
                c_function += argv
            break
        input_lines.append(line)
    return c_function
# def get_input():

def code_generate():
    # 获取命令行参数
    c_function = get_input()
    function_info = parse_c_function(c_function)
    function_name = function_info['function_name']
    function_name = function_name.strip()
    function_return = function_info['function_return']
    function_return = function_return.strip()
    function_param = ""
    function_name_list = ""
    for index, (param_type, param_name) in enumerate(function_info['function_params']):
        function_name_list += param_name
        function_param += param_type + " " + param_name

        # Check if it's not the last iteration
        if index < len(function_info['function_params']) - 1:
            function_name_list += ", "
            function_param += ", "

    print("function name: " + function_name)
    print("function return: " + function_return)
    print("function param: " + function_param)
    print("function name list: " + function_name_list)
    print("Parameters:")
    for param_type, param_name in function_info['function_params']:
        print(f"  Type: {param_type}, Name: {param_name}")

    code = textwrap.dedent(f'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* global mock set */
static bool mock_{function_name} = false;
constexpr int mock_{function_name}_errno = 1;
enum class {function_name}_case_des : int {{
    ret_1,
}};
static {function_name}_case_des {function_name}_case = {function_name}_case_des::ret_1;
/* {function_name} mock set */
typedef FILE* (*{function_name}_func_t)({function_param});
/* The real function address function */
{function_name}_func_t {function_name}_func = reinterpret_cast<{function_name}_func_t>(dlsym(RTLD_NEXT,"{function_name}"));
/* {function_name} mock */
extern "C" {function_return} {function_name}({function_param}) {{
  if (mock_{function_name}) {{
    if ({function_name}_case == {function_name}_case_des::ret_1) {{
      return {function_return}{{}};
    }} else if ( 1 ) {{
      return {function_return}{{}};
    }} else {{
      return {function_return}{{}};
    }}
  }} else {{
    return {function_name}_func({function_name_list});
  }}
}}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ''')

    print(code)
# def class_generate():

def main():
    code_generate()
# def main():

if __name__ == "__main__":
    main()
