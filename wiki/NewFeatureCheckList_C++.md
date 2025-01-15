# NewFeatureCheckList C++
# Checklist for adding a new feature to an existing workbench in C++ 

This checklist is intended as an aid to contributors.

The checklist itemizes the tasks involved in adding a wholly new feature to an existing module (workbench). It assumes that the existing workbench (myModule) and the new feature are written in C++.

The module code is divided into an App portion that deals with the document and its objects and a Gui portion that deals with visual aspects. Our source tree looks like this:


{{Code|lang=text|code=
src
    Mod
        myModule
            myModuleTest
                TestmyModuleApp.py
                TestmyModuleGui.py
                myFeatureTest.py
            App
                AppmyModule.cpp
                myFeature.cpp
                myFeature.h
                myFeaturePy.xml
                myFeaturePyImp.cpp
            Gui
                GuimyModule.cpp
                ViewProvidermyFeature.cpp
                ViewProvidermyFeature.h
                TaskmyFeature.cpp
                TaskmyFeature.h
                TaskmyFeature.ui
}}

## App changes 

-   new myModule/App/myFeature.cpp
-   new myModule/App/myFeature.h
-   new myModule/App/myFeaturePy.xml
-   new myModule/App/myFeaturePyImp.cpp

-   edit myModule/App/CMakeLists.txt
    -   add new source files
-   edit myModule/App/AppmyModule.cpp
    -   add include(s) for new objects
    -   add init calls for new objects

## Gui changes 

-   new myModule/Gui/ViewProvidermyFeature.cpp
-   new myModule/Gui/ViewProvidermyFeature.h
-   new myModule/Gui/TaskmyFeature.cpp
-   new myModule/Gui/TaskmyFeature.h
-   new myModule/Gui/TaskmyFeature.ui

-   edit myModule/Gui/CMakeLists.txt
    -   add new source files
-   edit myModule/Gui/AppmyModuleGui.cpp
    -   add includes for new objects
    -   add init calls for new objects
-   edit myModule/Gui/CommandXXXX.cpp
    -   add new command
-   edit myModule/Gui/Workbench.cpp
    -   add new command to menu & toolbar

-   new myModule/Gui/Resources/icons/myModule_myFeature.svg
-   edit myModule/Gui/Resources/myModule.qrc
    -   add icon to list

## Test changes 

-   new test script myModule/myModuleTest/myFeatureTest.py
-   edit myModule/myModuleTest/TestmyModuleApp.py and/or myModule/myModuleTest/TestmyModuleGui.py
    -   add import for myFeatureTest
-   edit myModule/CMakeLists.txt
    -   add myFeatureTest.py to list
-   new unit tests
    -   ????

## Documentation changes 

-   new wiki.freecad.org/myModule_myFeature
-   edit wiki.freecad.org/myModule_Workbench
    -   add new entry in module overview
-   edit predecessor and successor wiki entries
    -   update next and previous article pointers



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer%20Documentation.md) > NewFeatureCheckList C++
