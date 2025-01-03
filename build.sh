#!/bin/bash

# 检查输出目录是否存在
if [ ! -d "log/test_output/output" ]; then
    echo "错误：源文件目录不存在！"
    echo "请确保 log/test_output/output 目录中包含生成的 .c 和 .h 文件"
    exit 1
fi

# 创建并进入构建目录
mkdir -p build
cd build

# 配置项目
cmake ..

# 编译
cmake --build .

# 运行测试
ctest --output-on-failure

# 检查测试结果
if [ $? -ne 0 ]; then
    echo "测试失败！"
    exit 1
fi

# 添加覆盖率报告生成
if [ "$1" == "--coverage" ]; then
    echo "生成代码覆盖率报告..."
    
    # 运行测试程序以生成覆盖率数据
    ./tests/test_multi_i18n
    
    # 生成覆盖率报告
    lcov --capture --directory . --output-file coverage.info
    lcov --remove coverage.info '/usr/*' --output-file coverage.info
    genhtml coverage.info --output-directory coverage_report
    
    echo "覆盖率报告已生成在 build/coverage_report 目录中"
fi

echo "构建和测试成功完成！" 