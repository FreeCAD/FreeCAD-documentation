# FreeCAD 1.0 Development Cycle
{{Page_in_progress}}

Development of FreeCAD 1.0 began after tagging [FreeCAD 0.20](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20) on June 14, 2022.

### Minimum supported library versions 

The development of 1.0 targets Ubuntu 20.04 LTS as the oldest OS for compiling FreeCAD. The minimum supported infrastructure software versions are therefore the ones of Ubuntu 20.04 LTS:

-   Boost 1.71
-   GCC 7.5
-   Clang 6.0
-   CMake 3.16
-   Python 3.8
-   Qt 5.12
-   OpenCASCADE 7.3
-   VTK 6.3

This version of FreeCAD is compiled requiring the C++17 standard, and all C++17 features are allowed with two exceptions:

-   std::filesystem is not well-supported by GCC 7.5 \-- continue to use boost::filesystem instead
-   std::regex is much slower than boost::regex in some important cases, so we will continue to include the Boost regex library

The developers are encouraged to review the [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) for modern C++ coding advice. No strict coding convention has been selected for FreeCAD, though new C++ code often conforms to the [Qt coding conventions](https://wiki.qt.io/Coding_Conventions), and new Python typically conforms to [PEP 8](https://pep8.org/).

### Development Goal 

As volunteer-developed Open Source software it is impossible to guarantee that any particular feature will be implemented in a given time frame. For the 1.0 release there is however only one big goal:

-   Fix the [Topological naming problem](Topological_naming_problem.md) (in short: Toponaming)

### Toponaming branch 

In order to address the Toponaming issue, directly after the release of FreeCAD 0.20 a special Toponaming branch was created:


`https://github.com/FreeCAD/FreeCAD/tree/development/toponaming`

The workflow is the following:

FreeCAD\'s [master](https://github.com/FreeCAD/FreeCAD/tree/master) will contain the \"normal\" development. When the first portion of Toponaming is ready in the Toponaming branch

1.  the Toponaming is rebased on master
2.  an intermediate release is made to let users test it.
3.  If the feedback is positive the next portion of toponaming is as added to the toponaming branch

This cycle is repeated until FreeCAD is fully usable without the Toponaming issue.

#### Helping to test the Toponaming branch 

##### Snap package 

There will be a nightly [Snap](https://github.com/FreeCAD/FreeCAD-snap/issues/24) package available for convenience of testing the progress of the Toponaming branch.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Developer](Category_Developer.md) > FreeCAD 1.0 Development Cycle
