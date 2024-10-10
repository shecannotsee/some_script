import os
import subprocess

def use_valgrind(build_dir: str, test_target: str, output_file: str):
    test_executable = os.path.join(build_dir, test_target)

    if not os.path.exists(test_executable):
        raise Exception(f"Test target {test_executable} does not exist.")

    # Run the test executable with Valgrind
    valgrind_cmd = [
        "valgrind",
        "--leak-check=full",
        "--track-origins=yes",
        f"--log-file={output_file}",
        test_executable
    ]

    try:
        subprocess.run(valgrind_cmd, check=True)
        print(f"Valgrind analysis completed for {test_target}. Report saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Valgrind failed with error: {e}")
        raise
