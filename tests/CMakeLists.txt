set(UNITY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Unity)

if(EXISTS "${UNITY_DIR}/src/unity.c")
    message(STATUS "Unity framework found locally")
    add_library(unity STATIC
        ${UNITY_DIR}/src/unity.c
    )
    target_include_directories(unity PUBLIC
        ${UNITY_DIR}/src
    )
else()
    message(STATUS "Unity framework not found locally, attempting to download...")
    include(FetchContent)
    FetchContent_Declare(
        unity
        GIT_REPOSITORY https://github.com/ThrowTheSwitch/Unity.git
        GIT_TAG v2.5.2
        GIT_SHALLOW TRUE
    )
    FetchContent_MakeAvailable(unity)
endif()

# 添加测试可执行文件
add_executable(test_multi_i18n
    test_multi_i18n.c
)

# 链接库
target_link_libraries(test_multi_i18n
    PRIVATE
    multi_i18n
    unity
)

# 添加测试
add_test(NAME test_multi_i18n COMMAND test_multi_i18n)