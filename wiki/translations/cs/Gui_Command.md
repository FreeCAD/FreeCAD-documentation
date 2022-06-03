# Gui Command/cs
The GuiCommand is one of the most important functions of FreeCAD in the main interaction point of the user. Every time the user selects a menu item or presses a toolbar button it activates a GuiCommand. Some of the attributes of a GuiCommand are   *

-   Defines a name
-   Contains an icon
-   Defines the scope for an undo/redo
-   Has a help page
-   Opens and controls dialogs
-   Macro recording
-   and others.

## Naming

The GuiCommand is named in a standard way   * *ModuleName\_CommandName* e.g., \"[Base\_Open](Base_Open.md)\" this is the Open Gui Command in the Base system. The GuiCommand in a certain module is named with the module name in front e.g., \"[Part\_Cylinder](Part_Cylinder.md)\".

If the documentation is not finished use [Template   *UnfinishedDocu](Template_UnfinishedDocu.md).

## Help page 

Every GuiCommand has to have a help page. The help page is hosted on the FreeCAD documentation wiki. The article has the same name as the GuiCommand, e.g. [Draft ShapeString](Draft_ShapeString.md).

To create your own help pages you can use the template [GuiCommand model](GuiCommand_model.md)

Example   *

-   [Draft ShapeString](Draft_ShapeString.md)
-   [Draft Line](Draft_Line.md)

## Icons

<img alt="" src=images/Tango-Palette.png  style="width   *400px;">

Every GuiCommand has to have an icon. We use the [Tango icon set](http   *//tango-project.org/Tango_Desktop_Project/) and its guidelines. On the right side you see the tango color palette.

All icons should be created in [SVG](SVG.md) format with a vector image application, such as [Inkscape](http   *//inkscape.org). This makes it easier to apply changes and derive additional icons in the same application space.

### Icons color coding chart 

<img alt="" src=images/Colorchart.png  style="width   *200px;">

We try as much as possible to respect this chart, so the color of the icons has a direct meaning.

## Quality requirements 


**The [Complete Workbench](Complete_Workbench.md) is deprecated, it no longer holds each of the commands in FreeCAD.**

There are a lot of GuiCommands (tools) in FreeCAD which are experimental or used for a short time to test implementation of new features. These GuiCommands are mostly in the dedicated workbenches like Part, Mesh or Cam. To ensure a good user experience the workbench *Complete* was created. This workbench incorporates all GuiCommands which meet certain quality requirements which are described here   *

-   The command or feature has to be \"finished\", that is, not be a work in progress.
-   It has to set up a proper icon and menu position.
-   It has to have a help page, like [Draft ShapeString](Draft_ShapeString.md).
    -   All the fields in [Template   *GuiCommand](Template_GuiCommand.md) have to be filled in
    -   It should have a detailed description of the command and all its parameters and settings.
    -   It should have a picture of the dialogs that the command will produce.
    -   It should have a description of the related [Python](Python.md) interfaces and classes with example code.

Hopefully this becomes true for all GuiCommands in the [List of Commands](List_of_Commands.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > Gui Command/cs
