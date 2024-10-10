import  os
from utils.build               import cmake, make
from utils.static_analysis     import use_clang_tidy
from utils.run_test            import use_googletest
from utils.dynamic_analysis    import use_valgrind
from utils.coverage_report     import use_gcov
from utils.document_generation import use_doxygen


if __name__ == "__main__":
    # check path
    work_path: str = "project_name"
    current_path: str = os.getcwd()
    suffix: str = current_path[-len(work_path):]
    if suffix != work_path:
        raise Exception(f"Work path error: please ensure that the last few strings after using pwd are \"{work_path}\"")

    # build
    build_dir: str = "build"
    try:
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
        os.chdir(build_dir)
        cmake("..")
        make()
        os.chdir(current_path)
    except Exception as e:
        print(f"Build failed: {e}")
        exit(1)
    test_target: str = "test"

    # static analysis
    src_dir: str = "./src"
    try:
        use_clang_tidy(src_dir, "./report/static_analysis_report.log")
    except Exception as e:
        print(f"static analysis failed: {e}")
        exit(1)

    # run test
    try:
        use_googletest(build_dir, test_target)
        os.chdir(current_path)
    except Exception as e:
        print(f"run test failed: {e}")
        exit(1)

    # dynamic analysis
    try:
        use_valgrind(build_dir, test_target, "./report/valgrind_report.log")
    except Exception as e:
        print(f"dynamic analysis failed: {e}")
        exit(1)

    # coverage report
    try:
        use_gcov(build_dir, "./report/coverage.info", "./report/coverage_rate")
    except Exception as e:
        print(f"coverage report failed: {e}")
        exit(1)

    # document generation
    try:
        use_doxygen("./report/Doxyfile")
    except Exception as e:
        print(f"document generation failed: {e}")
        exit(1)


    print("ci done.")
