# Set the minimum required version of CMake for this project
cmake_minimum_required(VERSION 3.12)

# Set the project name and version
project(SnakeApp VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(SnakeApp main.cpp)
