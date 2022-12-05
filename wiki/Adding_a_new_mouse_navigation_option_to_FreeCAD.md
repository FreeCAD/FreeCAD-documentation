---
- TutorialInfo:   Topic:Adding new navigation option to FreeCAD
   Level:Advanced
   Time:
   Author:Kunda1
   FCVersion:0.19.x and above
   Files:
---

# Adding a new mouse navigation option to FreeCAD






## Introduction

This tutorial attempts to help developers understand how to add their own custom \'mouse\' models to FreeCAD. There are currently several options within FreeCAD to customize navigation, they are listed in the [Mouse navigation](Mouse_navigation.md) page. Some of the options include: Revit, OpenCascade, Inventor, Touchpad etc\...

## Prerequisite

-   Familiarity with C++ syntax
-   Ability to compile FreeCAD from source

## Relevant source files 

At the time of writing this documentation the relevant source code files are located at:

-    **src/Gui/NavigationStyle.(h,cpp)**
    

-    **src/Gui/(Foo)NavigationStyle.cpp***Foo* is a placeholder for the different mouse/navigation modes, for example: Revit, Inventor, OpenCascade, Touchpad, CAD etc\...

-    **src/Gui/CMakeLists.txt**\- Add your new mouse/navigation mode here so it\'s picked up by the compiler

-    **src/Gui/SoFCDB.cpp**
    

## Historical code commits 

We can refer to previous code commits that added different mouse modes for orientation. Here are a few:

-   Revit ([commit](https://github.com/FreeCAD/FreeCAD/commit/c397aee9ed3efcb2e33fa719313c98cc4867cf32))
-   OpenCascade ([commit](https://github.com/FreeCAD/FreeCAD/commit/be70bad701cb881f169b15aebb50e12a22828fbd))

## Source code



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Developer Documentation](Category_Developer Documentation.md) > Adding a new mouse navigation option to FreeCAD
