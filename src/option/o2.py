import os
from typing import NoReturn
from utils.file import get_content


def commit_standard() -> NoReturn:
    commit_standard_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "commit_standard.txt",        # commit_standard.txt
    )   # ../template/commit_standard.txt

    # output
    print(commit_standard_content)

