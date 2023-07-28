# C++ code testing
NOTE: This article is a stub \-- please help by filling in the missing details!

Beginning in late 2022 the developers of FreeCAD incorporated the [Google Test](https://google.github.io/googletest/) (gtest) testing framework into FreeCAD builds. This enables direct testing of the C++ code itself, without having to go through the Python wrappers (as was the case previously). This wiki page is intended as a simple, practical introduction to testing C++ code using Google Test. As a developer gains experience with the framework, they will likely be interested in more advanced techniques: see Further Reading, below.

## Overview of Testing with Google Test 

The basic premise of Google Test is that each individual test is wholly standalone. Test must be designed to be independent of one another: the order tests are run should never be relied on (in fact, many IDEs support running individual tests by clicking a \"run\" button next to the test function, so it is often the case that only a single test is run). A test writer uses a set of macros defined within Google Test to construct the individual tests: those macros ultimately expand into entire classes that are responsible for setup, teardown, and running of the test.

## Test Basics 

At its most simple, a test suite for a class \"MyClass\" in module \"MyMod\" consists of a file in `tests/src/Mod/MyMod/MyClass.cpp` containing the gtest include, the class header file include, and one or more individual tests, instantiated via the TEST macro. For example:

    #include "gtest/gtest.h"

    #include "App/License.h"

    TEST(License, AllRightsReserved)
    {
        auto lic = App::License{App::License::Type::AllRightsReserved};
        ASSERT_EQ(lic.getType(), App::License::Type::AllRightsReserved);
        ASSERT_EQ(lic.getLicense(), "All rights reserved");
        ASSERT_EQ(lic.getUrl(), "https://en.wikipedia.org/wiki/All_rights_reserved");
    }

This file is referenced in the CMakeLists.txt file in the `tests/src/Mod/MyMod/` directory:

    target_sources(
        Tests_run
            PRIVATE
                ${CMAKE_CURRENT_SOURCE_DIR}/MyClass.cpp
    )

## Compiling the tests 

The FreeCAD cMake scripts use the variable `BUILD_TEST` to determine whether to compile the tests during a build. If that variable is `ON`, the test executables are compiled when compiling FreeCAD.

## Further Reading 

-   Google Test: Advanced Topics: <https://google.github.io/googletest/advanced.html>
-   Feathers, Michael. Working Effectively with Legacy Code. ISBN: 978-0131177055
-   Beck, Kent. Test-Driven Development. ISBN: 978-0321146533
-   Langr, Jeff. Modern C++ Programming with Test-Driven Development. 978-1937785482



---
![](images/Right_arrow.png) [documentation index](../README.md) > C++ code testing
