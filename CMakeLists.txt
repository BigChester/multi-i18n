cmake_minimum_required(VERSION 3.10)
project(multi_i18n C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/log/test_output/output/c)

add_compile_options(-Wall -Wextra -Wpedantic)

add_library(multi_i18n
    ${SOURCE_DIR}/multi_i18n.c
)

target_include_directories(multi_i18n PUBLIC
    ${SOURCE_DIR}
)

# Start testing
enable_testing()
add_subdirectory(tests) 

option(CODE_COVERAGE "Enable coverage reporting" OFF)

if(CODE_COVERAGE)
    add_compile_options(-fprofile-arcs -ftest-coverage)
    add_link_options(-fprofile-arcs -ftest-coverage)
endif() 