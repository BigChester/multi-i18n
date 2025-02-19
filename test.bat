@echo off

REM Add MinGW and CMake to PATH
set PATH=D:\Program Files\mingw64\bin;D:\Program Files\cmake-3.30.2-windows-x86_64\bin;%PATH%

REM Check if output directory exists
if not exist "log\test_output\output" (
    echo Error: Source file directory does not exist!
    echo Please ensure that the log\test_output\output directory contains the generated .c and .h files
    exit /b 1
)

REM Clean build directory
rd /s /q .\build\

REM Create and enter build directory
if not exist build mkdir build
cd build

REM Configure project (using MinGW Makefiles)
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release ..

REM Build
cmake --build .

REM Run tests
ctest --output-on-failure

REM Check test results
if errorlevel 1 (
    echo Tests failed!
    exit /b 1
)

echo Build and test completed successfully!
cd .. 