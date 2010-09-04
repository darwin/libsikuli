include_directories("../")

if (WIN32)

include_directories("C:\\cxxtest")

endif (WIN32)

# cxxtest (http://battlemidget.blogspot.com/2010/03/c-cxxtest-cmake.html)
find_package(CxxTest)
if(CXXTEST_FOUND)
    add_executable(cxxtest 
       main_cxxtest.cpp 
       FlashTestSuite.cpp
       CoreTestSuite.cpp
       MacTestSuite.cpp)

    target_link_libraries(cxxtest 
       sikuli 
       ${APPLE_LIBRARIES} 
       ${OPENCV_LIBRARIES})
endif()