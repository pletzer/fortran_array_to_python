project(flibex)
cmake_minimum_required(VERSION 3.1)

enable_language(Fortran)

add_library(flibex SHARED flibex.f90)