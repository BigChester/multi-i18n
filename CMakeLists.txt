cmake_minimum_required(VERSION 3.10)
project(multi_i18n C)

# 设置 C 标准
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# 定义源文件目录
set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/log/test_output/output)

# 编译选项
add_compile_options(-Wall -Wextra -Wpedantic)

# 添加库
add_library(multi_i18n
    ${SOURCE_DIR}/multi_i18n.c
)

# 设置头文件包含目录
target_include_directories(multi_i18n PUBLIC
    ${SOURCE_DIR}
)

# 启用测试
enable_testing()
add_subdirectory(tests) 

option(CODE_COVERAGE "Enable coverage reporting" OFF)

if(CODE_COVERAGE)
    add_compile_options(-fprofile-arcs -ftest-coverage)
    add_link_options(-fprofile-arcs -ftest-coverage)
endif() 