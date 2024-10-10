import subprocess

def use_gcov(run_dir: str, output_file: str, report_dir: str):
    command: list[str] = ["lcov",
                          "--directory", run_dir,
                          "--capture",
                          "--output-file", output_file,
                          "--rc", "lcov_branch_coverage=1" ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running gcov: {e.stderr}")

    command: list[str] = ["genhtml",
                          output_file, "-o",
                          report_dir,
                          "--branch-coverage"]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running genhtml: {e.stderr}")
