---
- GuiCommand:Addon
   Name:BIM Preflight
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench.md)
   Addon:BIM
   MenuLocation:Manage → Preflight check
---

## Description

<img alt="" src=images/BIM_preflight_screenshot.png  style="width:1024px;">

As FreeCAD is a very loose and free-style modelling platform, the requirements are very low. You can basically model and organize your BIM model the way you like, using all the tools that FreeCAD offers, both from the BIM workbench and other workbenches. The IFC format, however, has some strict requirements, and other BIM applications that can read IFC files often bring additional limitations as they more than often have difficulties with certain entities or the way certain objects are modeled.

The BIM Preflight tool allows you to perform several tests on your model to verify its compatibility with IFC standards and best practices, and help you to detect possible issues you might want to fix.

The results of most of the tests provided by this tool are optional, which means you can choose to export your model even if they fail. You are the one to assess if you need the test to pass or not. We tried our best to give sound information to help you decide.

## Usage

-   Have a model opened in FreeCAD, with at least some objects
-   You can select objects before launching the tests, in which case you have the option to perform the test only on the selected objects
-   Press the **Test All** button to perform all the tests, or only buttons corresponding to individual tests.
-   When the tests have finished, pressing a **Failed** button will give you additional information to help you decide if this is relevant to you or not.

## Builtin tests 

-   **Run all tests**: Runs all the tests one after the other

### FreeCAD setup tests 

-   **IFC4 support**: Tests if the IFC import/export system of FreeCAD is working correctly, and if the IFC4 format is available (which requires an up-to-date version of [IfcOpenShell](Arch_IFC.md) and enabled in the preferences.

### Project organization tests 

-   **Project hierarchy**: The IFC format requires at least one [building](Arch_Building.md) and it is also a common practice to have one [site](Arch_Site.md) and at least one [level (storey)](Arch_BuildingPart.md). This test checks if these are present in the model
-   **Buildings**: Checks that all buildings found in the model are part of a [site](Arch_Site.md)
-   **Levels**: Checks that all [levels](Arch_BuildingPart.md) (building storeys) found in the model are prt of a building
-   **Objects structure**: Checks that all objects found in the model are part of a level

### Objects & property tests 

-   **Undefined objects**: Checks if there are objects in the model that are not BIM objects, and will therefore be exported without full BIM properties
-   **Solids**: Checks that all objects in the model have valid solid geometry
-   **Explicit quantities**: Checks that all objects with length, width or height properties are [marked for explicit export](BIM_IfcQuantities.md) of these quantities
-   **Common Properties sets**: Checks that all BIM objects of common types (wall, door, etc\...) have the corresponding \"common\" properry set applied (Pset\_WallCommon, Pset\_DoorCommon, etc)
-   **Property sets integrity**: Checks that all common Psets (Pset\_WallCommon, Pset\_DoorCommon, etc) found in the model include all and only the properties defined by the IFC standards
-   **Materials**: Checks that all BIM objects have a material
-   **Standards**: Checks that all BIM objects have a [standard code](BIM_Classification.md)

### Compatibility tests 

-   **Extrusions**: Checks that all BIM objects are linear extrusions
-   **Standard cases**: Checks that all [walls](Arch_Wall.md) and [structural elements](Arch_Structure.md) are standard cases, as defined by the IFC schema
-   **Tiny lines**: Checks that no line segment in the model is smaller than 1/32\", the minimum length that Revit is able to manage\...
-   **IfcRectangleProfileDef**: Checks that the option to export rectangular profiles as IfcRectangleProfileDef is disabled, because Revit (yes, them again) is unable to import that entity.

## Custom tests 

The Preflight tool also allows you to write custom tests, that will be appended after the built-in tools in the Preflight dialog, and run when using the **Run all tests** button. These tests are written in Python. They consists of simple functions inside one or more Python files. You can perform any operation you want inside those functions, they must just pass or fail, and in case they fail, show a message informing the user of what failed.

You can write several tests in one single Python file, or divide in several files, as you prefer. These files must be placed in \$USERAPPDATA/BIM/Preflight and can be given any name (Be sure to use very unique names as to not conflict with any built-in Python module. The \$USERAPPDATA folder depends on your platform/operating system (usually \$HOME/.FreeCAD on linux/mac, /users/YOUR USER/Application Data/roaming/FreeCAD on windows), and can also be found by entering this in the FreeCAD Python console:

FreeCAD.getUserAppDataDir()

Inside each Python file, tests are simple functions that take no argument, and return either True if the test passed, or a string of text that will be shown to the user if the test failed.

A typical test file would be like this, that should be named something like \"myCustomTest.py\" and placed inside \$USERAPPDATA/BIM/Preflight: 

import FreeCAD
# The name of your test. You can give the functions any name
# you want, the important is the description text below
def myCustomTest():
   # This describes what your test does. For example,
   # here, it checks that there is at least one object in the document.
   # This text will appear next to the button in the Preflight tool
   """Checks that the document contains at least one object"""
   doc = FreeCAD.ActiveDocument
   objects = doc.Objects
   if len(objects) >= 1:
       result = True
   else:
       result = "This document contains no object"
   # The function must return either True or a string of
   # text if the test failed. The string or text will be displayed
   # to the user when they press the "Failed" button.
   return result
