import base64


def decode(char_input):
    char_display = char_input
    if char_input == '\n':
        char_display = "line_break"
    if char_input == '\\':
        char_display = "escape_character"
    if char_input == ' ':
        char_display = "space"
    # encode
    encoded_char = base64.b64encode(char_input.encode('utf-8')).decode('utf-8')
    print(f"char:                {char_display}")
    print(f"after Base64 encode: {encoded_char}")


# def decode(char_input):


decode('\n')
decode('\\')
decode(' ')
