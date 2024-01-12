#!/bin/bash
exec_program="shared_test_test"

############# 获取--gtest_list_tests输出的每一行并组成--gtest_filter的用例 #############
output=$(./${exec_program} --gtest_list_tests)
formatted_output=$(echo "${output}" | sed ':a;N;$!ba;s/\n\(\S\)/ \1/g')
items=($(echo "${formatted_output}" | grep -o '\S\+'))

suite_name=()
now_father_suite=""
# 打印数组中的每个元素
for ((i=0; i<${#items[@]}; i++)); do
    current_item="${items[i]}"
    # 检查末尾是否为.
    if [[ $current_item == *"." ]]; then
        # 进行特殊处理
        now_father_suite=$current_item
    else
        suite_name+=(${now_father_suite}${current_item})
    fi
done


############# 单独运行每一个测试用例 #############
error_suite=()
for ((i=0; i<${#suite_name[@]}; i++)); do
    ./${exec_program} --gtest_filter=${suite_name[i]} > output_file.txt 2>&1 &
    pid=$!
    (sleep 10 && kill -9 $pid) 2>/dev/null &
    wait $pid
    running_output=$(cat output_file.txt)
    if [ $? -eq 0 ] && echo "$running_output" | grep -q "PASSED"; then
      echo "./${exec_program} --gtest_filter=${suite_name[i]}"
    else
      error_suite+=(./${exec_program} --gtest_filter=${suite_name[i]})
      echo "./${exec_program} --gtest_filter=${suite_name[i]}"
    fi
done


############# 报错 #############
for ((i=0; i<${#error_suite[@]}; i++)); do
  echo "error suite:"
  echo ${error_suite[i]}
done

