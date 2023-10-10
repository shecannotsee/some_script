import configparser


def read_ini_file():
    # 创建ConfigParser对象
    config = configparser.ConfigParser()
    # 读取INI文件
    config.read('DFA_model.ini')
    return config


# def class_generate():


class five_tuple:
    def __init__(self, states, alphabet, alphabet_value, function_S, function_Q, function_S_END, start_state,
                 accept_state):
        self.states = states
        self.alphabet = alphabet
        self.alphabet_value = alphabet_value
        self.function_S = function_S
        self.function_Q = function_Q
        self.function_S_END = function_S_END
        self.start_state = start_state
        self.accept_state = accept_state
    # def __init__( ......


# class five_tuple:


def get_data(config):
    # 1.states #########################################################################################################
    all_states = []
    state_num = 0
    states = "states"
    keys = config.options(states)
    # 遍历并打印键和对应的值
    for key in keys:
        state_num = state_num + 1
        value = config.get(states, key)
        all_states.append(key)

    # 2.alphabet #######################################################################################################
    all_alphabet = []
    all_alphabet_value = []
    alphabet_num = 0
    alphabet = "alphabet"
    keys = config.options(alphabet)
    # 遍历并打印键和对应的值
    for key in keys:
        alphabet_num = alphabet_num + 1
        value = config.get(alphabet, key)
        all_alphabet.append(key)
        all_alphabet_value.append(value)

    # 3.function #######################################################################################################
    all_S = []
    all_Q = []
    all_S_END = []
    function = "function"
    function_sum = (state_num - 1) * alphabet_num
    for i in range(function_sum):
        function_section = function + str(i + 1)
        S = config.get(function_section, 'S')
        Q = config.get(function_section, 'Q')
        S_END = config.get(function_section, 'S_END')
        all_S.append(S)
        all_Q.append(Q)
        all_S_END.append(S_END)

    # 4.start_state ####################################################################################################
    start_state = "start_state"
    start_state = config.get(start_state, start_state)

    # 5.accept_state ###################################################################################################
    accept_state = "accept_state"
    accept_state = config.get(accept_state, accept_state)

    # ret ##############################################################################################################
    result = five_tuple(all_states,
                        all_alphabet, all_alphabet_value,
                        all_S, all_Q, all_S_END,
                        start_state,
                        accept_state)
    # return ##########################################################################################################
    return result
# def get_data(config):


def main():
    config = read_ini_file()
    info = get_data(config)
    print(info.states)
    print(info.alphabet)
    print(info.alphabet_value)
    print(info.function_S)
    print(info.function_Q)
    print(info.function_S_END)
    print(info.start_state)
    print(info.accept_state)
# def main():


if __name__ == "__main__":
    main()
