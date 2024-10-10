import subprocess

def use_doxygen(doxyfile_file: str):
    command = ["doxygen", doxyfile_file]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running doxygen: {e.stderr}")
