import configparser


def read_ini_file():
    # 创建ConfigParser对象
    config = configparser.ConfigParser()
    # 读取INI文件
    config.read('DFA_model.ini')
    return config
# def class_generate():


def get_data(config):
    # 1.states #########################################################################################################
    print("\n1.states")
    state_num = 0
    states = "states"
    keys = config.options(states)
    # 遍历并打印键和对应的值
    for key in keys:
        state_num = state_num + 1
        value = config.get(states, key)
        print(f"{key} = {value}")

    # 2.alphabet #######################################################################################################
    print("\n2.alphabet")
    alphabet_num = 0
    alphabet = "alphabet"
    keys = config.options(alphabet)
    # 遍历并打印键和对应的值
    for key in keys:
        alphabet_num = alphabet_num + 1
        value = config.get(alphabet, key)
        print(f"{key} = {value}")

    # 3.function #######################################################################################################
    print("\n3.function")
    function = "function"
    function_sum = (state_num - 1) * alphabet_num
    for i in range(function_sum):
        function_section = function + str(i + 1)
        S = config.get(function_section, 'S')
        Q = config.get(function_section, 'Q')
        S_END = config.get(function_section, 'S_END')
        print(S, "+", Q, "->" + S_END)

    # 4.start_state ####################################################################################################
    print("\n4.start_state")
    start_state = "start_state"
    start_state = config.get(start_state, start_state)
    print(start_state)
    # 5.accept_state ###################################################################################################
    print("\n5.accept_state")
    accept_state = "accept_state"
    accept_state = config.get(accept_state, accept_state)
    print(accept_state)
# def get_data(config):


def main():
    config = read_ini_file()
    get_data(config)
# def main():


if __name__ == "__main__":
    main()
