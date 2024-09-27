import os
import re
from typing import NoReturn
from typing import Tuple, List, Dict, Optional, Union
from utils.file import get_content

def param_parse(param: str) -> Tuple[str, str]:
    # 使用空格分隔字符串，得到单词列表
    param_list_str: List[str] = param.split()
    if len(param_list_str) > 0:
        param_name: str = param_list_str[-1]
        param_type: str = " ".join(param_list_str[:-1])
        if param_name[0] == "*":
            param_type += "*"
            param_name = param_name[1:]
        return param_type, param_name
    else:
        # 如果字符串为空，返回两个空字符串
        return "", ""


def parse_c_function(c_function_string: str) -> Optional[Dict[str, Union[str, List[Tuple[str, str]]]]]:
    # get function return and name info
    function_return: str = ""
    function_name: str = ""
    match = re.search(r'[^()]+(?=\()', c_function_string)
    if match:
        function_return_name: List[str] = match.group().split()
        function_return: str = function_return_name[0]
        function_name: str = function_return_name[1]
        if function_name[0] == "*":
            function_return += "*"
            function_name = function_name[1:]
    else:
        print("parse c function error")
        return None

    # get param info
    param_info_list: List[Tuple[str, str]] = []
    match = re.search(r'\((.*?)\)', c_function_string)
    if match:
        # 获取匹配到的括号内的内容
        param_info: List[str] = match.group(1).split(',')
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


def mock_sys_function() -> NoReturn:
    mock_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "sys_func_mock.h",            # sys_func_mock.h
    )   # ../template/sys_func_mock.h

    # get input
    function_str: str = input("input function [example int func(int a)]:")
    function_info = parse_c_function(function_str)
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

    # replace
    mock_content = mock_content.replace("{function_name}", function_name)
    mock_content = mock_content.replace("{function_return}", function_return)
    mock_content = mock_content.replace("{function_name_list}", function_name_list)

    # output
    print(mock_content)