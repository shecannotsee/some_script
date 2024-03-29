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
#include <provide_hash.h>

namespace DFA_model {
        ''')
        cpp_code_file.write(content)
        # get states ###################################################################################################
        state_str = "  "
        for state in data.states:
            state_str += state
            state_str += ","
        content = textwrap.dedent(f'''
/********** States ****************************************************************************************************/
enum class states : int {{
  {state_str}REFUSE
}};
''')
        cpp_code_file.write(content)

        # get alphabet #################################################################################################
        a_state = ""
        hash_table = ""
        for alphabet, value in zip(data.alphabet, data.alphabet_value):
            # print("Alphabet:", alphabet, "Value:", value)
            a_state += alphabet
            a_state += ","
            hash_table += "  {'" + value + "', alphabet::" + alphabet + "},\n"
        content = textwrap.dedent(f'''
/********** alphabet **************************************************************************************************/
enum class alphabet : int {{
  {a_state}
}};

static std::unordered_map<char, alphabet> cher_table = {{
{hash_table}}};

// convert Character to State
template<typename char_type>
alphabet get_alphabet(char_type input) {{
  if (cher_table.find(input) != cher_table.end()) {{
    return cher_table[input];
  }} else {{
    //
  }}
}}
''')
        cpp_code_file.write(content)

        # get function #################################################################################################
        function_str = ""
        for i in range(len(data.function_S)):
            # print("Function", i + 1, "S:", data.function_S[i])
            # print("Function", i + 1, "Q:", data.function_Q[i])
            # print("Function", i + 1, "S_END:", data.function_S_END[i])
            function_str += "  {{static_cast<int>(states::" + data.function_S[i] + \
                            "),static_cast<int>(alphabet::" + data.function_Q[i] + \
                            ")},/* -> */states::" + data.function_S_END[i] + "},\n"

        content = textwrap.dedent(f'''
/********** Transition Function ***************************************************************************************/
static std::unordered_map<std::tuple<int,int>,states> transfer_function = {{
{function_str}}};

template<typename char_type>
states transition_status(states now, char_type input) {{
  int input_S = static_cast<int>(now);
  int input_Q = static_cast<int>(get_alphabet(input));
  auto key = std::make_tuple(input_S,input_Q);
  if(transfer_function.find(key)!= transfer_function.end())
    return transfer_function[key];
  else {{
    return states::REFUSE;
  }}
}}
''')
        cpp_code_file.write(content)

        # get start state ##############################################################################################
        # print("Start State:", data.start_state)
        content = textwrap.dedent('''
/********** init state ************************************************************************************************/
        ''')
        content += "constexpr states start_state = states::" + data.start_state + ";\n"
        cpp_code_file.write(content)

        # get end state ################################################################################################
        # print("Accept State:", data.accept_state)
        content = textwrap.dedent('''
/********** accept state **********************************************************************************************/
        ''')
        content += "constexpr states accept_state = states::" + data.accept_state + ";\n\n"
        cpp_code_file.write(content)

        # END ##########################################################################################################
        cpp_code_file.write("}// namespace DFA_model\n\n")
        cpp_code_file.write("#endif //DFA_MODEL_H\n")

    with open("provide_hash.h", "w") as hash_code:
        content = textwrap.dedent('''#ifndef PROVIDE_HASH_H
#define PROVIDE_HASH_H

#include <tuple>

// Provide custom hashes to <>
namespace std {
template<>
struct hash<std::tuple<int, int>> {
  std::size_t operator()(const std::tuple<int, int> &key) const {
    using std::hash;
    // Combine the hash values of the two enum values to create a unique hash
    return hash<int>()(static_cast<int>(std::get<0>(key))) ^ hash<int>()(static_cast<int>(std::get<1>(key)));
  }
};
}// namespace std

#endif //PROVIDE_HASH_H
        ''')
        hash_code.write(content)



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
