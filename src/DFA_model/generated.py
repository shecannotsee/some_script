import configparser
import textwrap


def read_ini_file():
    # 创建ConfigParser对象
    config = configparser.ConfigParser()
    # 读取INI文件
    config.read('DFA_model.ini')
    return config
# def class_generate():


class five_tuples:
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
    result = five_tuples(all_states,
                        all_alphabet, all_alphabet_value,
                        all_S, all_Q, all_S_END,
                        start_state,
                        accept_state)
    # return ##########################################################################################################
    return result
# def get_data(config):


def generate_cpp_code(data):
    with open("DFA_model.cpp", "w") as cpp_code_file:
        content = textwrap.dedent('''#ifndef DFA_MODEL_H
#define DFA_MODEL_H

#include <unordered_map>

namespace DFA_model {
        ''')
        cpp_code_file.write(content)
        # get states ###################################################################################################
        state_str = "  "
        for state in data.states:
            state_str += state
            state_str += ", "
        content = textwrap.dedent(f'''
/********** States ****************************************************************************************************/
enum class states : int {{
  {state_str}REFUSE
}};

''')
        cpp_code_file.write(content)

        # get alphabet #################################################################################################
        for alphabet, value in zip(data.alphabet, data.alphabet_value):
            print("Alphabet:", alphabet, "Value:", value)
        content = textwrap.dedent(f'''
/********** alphabet **************************************************************************************************/
enum class states : int {{
  {state_str}REFUSE
}};

''')

        # get function #################################################################################################
        for i in range(len(data.function_S)):
            print("Function", i + 1, "S:", data.function_S[i])
            print("Function", i + 1, "Q:", data.function_Q[i])
            print("Function", i + 1, "S_END:", data.function_S_END[i])

        # get start state ##############################################################################################
        print("Start State:", data.start_state)

        # get end state ################################################################################################
        print("Accept State:", data.accept_state)

        # END ##########################################################################################################
        cpp_code_file.write("}// namespace DFA_model\n\n")
        cpp_code_file.write("#endif //DFA_MODEL_H\n")
# def generate_cpp_code(data):

def main():
    config = read_ini_file()
    info = get_data(config)
    # print(info.states)
    # print(info.alphabet)
    # print(info.alphabet_value)
    # print(info.function_S)
    # print(info.function_Q)
    # print(info.function_S_END)
    # print(info.start_state)
    # print(info.accept_state)
    generate_cpp_code(info)
# def main():


if __name__ == "__main__":
    main()
