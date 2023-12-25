import sys
import textwrap
import re


# int fclose (FILE *__stream, int b)
# FILE* fopen(const char *__restrict __filename, const char *__restrict __modes)
def parse_c_function(c_function_string):
    # Regular expression to extract function information
    pattern = r'(\w+)\s+([\w\s\*]+)\s*\(([^)]*)\)'
    match = re.match(pattern, c_function_string)

    if match:
        function_return = match.group(1)
        function_name = match.group(2)
        param_list = match.group(3).split(',')

        # Extracting parameter types and names
        param_info = [tuple(param.strip().split()) for param in param_list if param.strip()]

        # process
        for i in range(len(param_info)):
            if param_info[i]:
                param_name, param_type = param_info[i]
                if param_type[0] == "*":
                    param_info[i] = (param_name + param_type[0], param_type[1:])

        return {
            'function_name': function_name,
            'function_return': function_return,
            'function_params': param_info
        }
    else:
        print("parse c function error")
        return None
# def parse_c_function(declaration):


def code_generate():
    # 获取命令行参数
    c_function = sys.argv[1] if len(sys.argv) > 1 else input("input function [example int func(int a)]：")

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
