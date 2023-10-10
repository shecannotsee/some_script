import configparser


def read_ini_file():
    # 创建ConfigParser对象
    config = configparser.ConfigParser()

    # 读取INI文件
    config.read('example.ini')

    # 获取值
    value1 = config.get('Section1', 'key1')
    value2 = config.get('Section1', 'key2')
    value3 = config.get('Section2', 'key3')
    value4 = config.get('Section2', 'key4')

    # 打印值
    print(f"Section1 key1: {value1}")
    print(f"Section1 key2: {value2}")
    print(f"Section2 key3: {value3}")
    print(f"Section2 key4: {value4}")
# def class_generate():


def main():

    read_ini_file()
# def main():


if __name__ == "__main__":
    main()



