# FreeCAD 1.0 Development Cycle
{{Page_in_progress}}

Development of FreeCAD 1.0 began following the tagging of [\| FreeCAD\'s 0.20 release version](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.20) on June 13, 2022.

### Minimum supported library versions 

Development of 1.0 targets Ubuntu 20.04 LTS as the oldest OS for compiling FreeCAD. Minimum supported infrastructure software versions are   *

-   GCC 7.5
-   Clang 6.0
-   CMake 3.16
-   Python 3.8
-   Qt 5.12
-   OpenCASCADE 7.3

This version of FreeCAD is compiled requiring the C++17 standard, and all C++17 features are allowed with two exceptions   *

-   std   *   *filesystem is not well-supported by GCC 7.5 \-- continue to use boost   *   *filesystem instead
-   std   *   *regex is much slower than boost   *   *regex in some important cases, so we will continue to include the Boost regex library

Developers are encouraged to review the [C++ Core Guidelines](https   *//isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) for modern C++ coding advice. No strict coding convention has been selected for FreeCAD, though new C++ code often conforms to the [Qt coding conventions](https   *//wiki.qt.io/Coding_Conventions), and new Python typically conforms to [PEP 8](https   *//pep8.org/).

### Development Goal 

As volunteer-developed Open Source software it is impossible to guarantee that any particular feature will be implemented in a given time frame. For the 1.0 release there is however only one big goal   *

-   Fix the [Topological naming problem](Topological_naming_problem.md) (in short   * Toponaming)

### Toponaming branch 

In order to address the Toponaming issue, directly after the release of FreeCAD 0.20 a special Toponaming branch was created   *

-   ???will follow???

FreeCAD\'s [master](https   *//github.com/FreeCAD/FreeCAD/tree/master) will contain the \"normal\" development.

Now, when the first portion of Toponaming is ready in the Toponaming branch

1\. the Toponaming is rebased on master 1. an intermediate release is made to let users test it. 1. If the feedback is positive the next portion of toponaming is as added to the toponaming branch

This cycle is repeated until FreeCAD is fully usable without the Toponaming issue.

[Category   *Roadmap](Category_Roadmap.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Developer](Category_Developer.md) > FreeCAD 1.0 Development Cycle
