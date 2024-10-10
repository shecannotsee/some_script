import os
import subprocess

def use_googletest(build_dir: str, target: str):
    os.chdir(build_dir)

    command = ["./" + target]
    subprocess.run(command, check=True)
    return " ".join(command) # Format output command
