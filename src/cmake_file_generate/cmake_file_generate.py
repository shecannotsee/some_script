import configparser
import textwrap

# 该函数用来处理是否启用配置文件来生成cmake
def use_config():
  user_input = input("是否使用配置文件(config.ini)？(y/n,default yes): ")
  if user_input.lower() == "y" or user_input.strip().lower() == '':
    return True
  elif user_input.lower() == "n":
    return False
  else:
    print("无效的输入，请输入 'y' 或 'n'。")
    return use_config()  # 递归调用函数以重新获取有效输入
# END:[use_config()]

def config_generate():
  # 创建一个ConfigParser对象
  config = configparser.ConfigParser()
  # 读取INI文件
  config.read('config.ini')

  code = ""
  code += "#" * 120 + "\n\n"
  # cmake_set
  cmake_set__version = config.get('cmake_set', 'version')
  code += "cmake_minimum_required(VERSION {})\n".format(cmake_set__version)
  code += "\n"

  # language
  language__cpp_standard = config.get('language', 'cpp_standard')
  code += "set(CMAKE_CXX_STANDARD {})\n".format(language__cpp_standard)
  code += "set(CMAKE_CXX_STANDARD_REQUIRED ON)\n"
  code += "set(CMAKE_CXX_FLAGS \"-g\")\n" # to debug
  code += "\n"

  code += "#" * 120 + "\n\n"
  # project
  project__name = config.get("project", "name")
  code += "set(PROJECT_NAME \"{}\" VERSION 0.0.1)\n".format(project__name)
  code += "set(CMAKE_BUILD_TYPE \"RELEASE\") # [Release]or[Debug]or[MinSizeRel]\n"
  code += "project(${PROJECT_NAME})\n"
  code += "\n"

  code += "#" * 120 + "\n\n"
  # set project type
  project__type = config.get("project", "type")
  code += "set(test \"ON\")\n"
  code += "set(library \"{}\")\n".format("ON" if project__type == "lib" else "OFF")
  code += textwrap.dedent('''
          # test set
          if (test STREQUAL "ON")
              set(test_name "${PROJECT_NAME}_test")
          else()
              message(STATUS "CMakeLists.txt error")
          endif ()
      
          # lib set
          if (library STREQUAL "ON")
              set(library_static_name "${PROJECT_NAME}_static")
              set(library_dynamic_name "${PROJECT_NAME}_dynamic")
              message(STATUS "This is a library")
          elseif(library STREQUAL "OFF")
              message(STATUS "This is an executable program")
          else()
              message(STATUS "CMakeLists.txt error")
          endif ()
          # message(STATUS "${test_name}")
          # message(STATUS "${library_static_name}")
          # message(STATUS "${library_dynamic_name}")
          ''')
  code += "\n"

  code += "#" * 120 + "\n"
  # some set
  code += textwrap.dedent('''
          get_filename_component(cmake_upper_path ${CMAKE_SOURCE_DIR} DIRECTORY)
          # message(STATUS "cmake_upper_path's path:${cmake_upper_path}")
          ''')
  code += "\n"

  code += "#" * 120 + "\n"
  # include and lib
  code += textwrap.dedent('''
          # include
          include_directories(${CMAKE_SOURCE_DIR}/src)
          # lib
          link_directories()
          ''')
  code += "\n"

  code += "#" * 120 + "\n"
  # target
  code += textwrap.dedent('''
          file(GLOB_RECURSE SRC "${CMAKE_SOURCE_DIR}/src/*")
          file(GLOB_RECURSE TEST_SRC "${CMAKE_SOURCE_DIR}/test/*")
          # list(REMOVE_ITEM SRC "${CMAKE_SOURCE_DIR}/src/TaskControl.cpp") # Exclude specific files
          
          # test target
          add_executable(${test_name} ${TEST_SRC} ${SRC})
          target_link_libraries(${test_name} "-pthread")
          
          # lib target
          if (library STREQUAL "ON")
              add_library(${library_static_name} STATIC ${SRC})
              # Rename the generated static library
              set_target_properties(${library_static_name} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
              
              add_library(${library_dynamic_name} SHARED ${SRC})
              # Rename the generated dynamic library
              set_target_properties(${library_dynamic_name} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
          # exe target
          elseif(library STREQUAL "OFF")
              add_executable(${PROJECT_NAME} ${TEST_SRC} ${SRC})
              target_link_libraries(${PROJECT_NAME} "-pthread")
              message(STATUS "This is an executable program")
          # error
          else()
              message(STATUS "CMakeLists.txt error:target error")
          endif ()

          ''')
  code += "\n"

  code += "#" * 120
  # install
  code += textwrap.dedent('''
          # local debug
          set(CMAKE_INSTALL_PREFIX "./")
          # Release Code
          #set(CMAKE_INSTALL_PREFIX "/")
          
          message(STATUS "The default installation path is ${CMAKE_INSTALL_PREFIX}")
          message(STATUS "Please use \"make install DESTDIR=./PATH\" to set install path")
          
          # test install
          install(TARGETS
                  ${test_name} DESTINATION ${PROJECT_NAME}/bin
                  )
          
          if (library STREQUAL "ON")
              # include install
              install(FILES
                      ${CMAKE_SOURCE_DIR}/src/she_base64.h # source head
                      DESTINATION # to
                      ${PROJECT_NAME}/include # target dir
                      )
              # lib install
              install(TARGETS
                      ${library_static_name} ${library_dynamic_name}
                      DESTINATION ${PROJECT_NAME}/include
                      )
          ''')


  # 打印获取到的值
  print(code)
# END:[config_generate()]


def default_generate():
  print("88")
# END:[default_generate()]


def main():
  config = use_config()
  if config == True :
    print("使用配置文件来生成")
    config_generate()
  else :
    default_generate()
# END:[main()]

if __name__ == "__main__":
  main()

