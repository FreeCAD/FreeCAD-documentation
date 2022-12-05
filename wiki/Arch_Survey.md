---
- GuiCommand:
   Name:Arch Survey
   MenuLocation:Arch → Survey
   Workbenches:[Arch](Arch_Workbench.md)
   SeeAlso:[Macro FCInfo](Macro_FCInfo.md), [Macro SimpleProperties](Macro_SimpleProperties.md)
---

# Arch Survey

## Description

The **<img src="images/Arch_Survey.svg" width=16px> [Arch Survey](Arch_Survey.md)** tool enters a special surveying mode, which allows you to quickly grab measurements and information from a model, and transfer that information to other applications. Once you are in Survey mode, clicking on different subelements of 3D objects gathers the following information (depending on what you click):

-   If you click on an edge, you get its length
-   If you click on a vertex, you get its height (coordinate on the Z axis)
-   If you click on a face, you get its area
-   If you double-click anything, therefore select the whole object, you get its volume

When such a piece of information is gathered, several things happen:

-   A label is placed on top of the element you clicked, that displays the value (with \"a\" for area, \"l\" for length, \"z\" for height, or \"v\" for volume)
-   The numeric value is copied to the clipboard, so you can paste it in another application
-   A line is printed on the FreeCAD output window. After you exit the survey mode, those lines can be copied and pasted in another application (the values are comma-separated, making it easy to convert to spreadsheet data)
-   The total length or area of the elements you clicked so far is also printed in the output window
-   Each length or area is also recorded in the task dialog

 <img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;"> 

*The above image shows what happens when running the survey mode.*

## Usage

1.  Press the **<img src="images/Arch_Survey.svg" width=16px> [Arch Survey](Arch_Survey.md)** button.
2.  Click on vertices, edges, faces or double-click to select whole objects.
3.  Click outside any geometry (on the background of the 3D view) to remove existing labels, print a total line in the Task dialog, and restart counting lengths and areas from zero.
4.  Press **Esc** or the **Close** button to exit survey mode and remove all the labels.

## Options

-   You can add a custom label to any line in the Task dialog by clicking that line, then adding a text in the description field, then press the **set description** button.
-   Once you are done, before closing, you can export the contents of the Task dialog by pressing the \"export CSV\" button. The resulting CSV file can then be opened in any spreadsheet application such as Excel or LibreOffice Calc. The values and units will be separated in the resulting CSV file, and the totals are written as SUM() functions.

 <img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;"> 

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Survey tool doesn\'t have a programming interface, but gathering the same information from any selected [Part](Part_Workbench.md)-based object is reproduced with the following script:

 
```python
import FreeCADGui

selection = FreeCADGui.Selection.getSelectionEx()

for obj in selection:
    for element in obj.SubObjects:
        print("Area: %f", element.Area)
        print("Length: %f", element.Length)
        print("Volume: %f", element.Volume)
        print("Center of Mass: %f", element.CenterOfMass)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Survey
