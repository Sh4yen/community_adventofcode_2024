cmake_minimum_required(VERSION 3.21) # Minimum version for Fortran stdlib support
project(MyFortranProject LANGUAGES Fortran)

# Find the Fortran Standard Library package
find_package(fortran_stdlib REQUIRED)

# Define the executable target
add_executable(${PROJECT_NAME}
  src/main.f90
  # src/module.f90
)

# Add include directories (if needed)
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Specify compiler flags
target_compile_options(${PROJECT_NAME} PRIVATE -O2 -Wall -g)

# Link the Fortran Standard Library
target_link_libraries(
  ${PROJECT_NAME}
  PRIVATE
  fortran_stdlib::fortran_stdlib
)
