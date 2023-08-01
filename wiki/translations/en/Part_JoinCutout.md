---
- GuiCommand:
   Name:Part JoinCutout
   MenuLocation:Part - Join - Cutout for Object
   Workbenches:[Part](Part_Workbench.md)
   Version:0.16
   SeeAlso:[Part JoinConnect](Part_JoinConnect.md), [Part JoinEmbed](Part_JoinEmbed.md), [Part Boolean](Part_Boolean.md), [Part Thickness](Part_Thickness.md)
---

# Part JoinCutout/en

## Description

The <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> [Part JoinCutout](Part_JoinCutout.md) tool creates a cutout in a walled object (e.g., a pipe) to fit another walled object.

![600px](images/JoinFeatures_Cutout.png)

## Usage

1.  Select the base object first, then the object to define the cutout.
    The order of selection is important. It is enough to select one sub-shape of each object (e.g., faces).
2.  Invoke the Part JoinCutout command several ways:
    -   Pressing on the <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> [Part JoinCutout](Part_JoinCutout.md) button in the Part toolbar
    -   Using the **Part → Join → Cutout for Object** entry in the Part menu

A Part JoinFeature object is created, with Mode set to \'Cutout\'. Original objects are hidden, and the result of cutting is shown in [3D view](3D_view.md).

## Properties


{{TitleProperty|Base}}

-    **Base**: Reference to base object (the one to make the cutout in). The object should be a single solid.

-    **Tool**: Reference to tool object (the object that is to fit into the cutout). The object can be a single solid, or a [valid compound](Part_Compound.md) of solids.

-    **Mode**: The mode of operation, equals \'Cutout\' (Changing that will transform the tool into another Part_JoinXXX). The value of \'bypass\' can be used to temporarily disable the long computations (a compound of Base and Tool will be created, which is a fast operation).

-    **Refine**: Sets whether to apply [Refine](Part_RefineShape.md) operation or not, to the final shape. The default value is determined by a \'Automatically refine shape after boolean operation\' checkbox in PartDesign preferences. When Mode property is \'bypass\', Refine is ignored (never applied).

## Example

1.  Create a pipe by applying [thickness](Part_Thickness.md) to a [cylinder](Part_Cylinder.md):
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Create another, smaller diameter pipe, and [place](Placement.md) it so that it pierces the wall of the first pipe:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Select the first pipe, then the second pipe (order of selection is important), and click the \'Cutout for object\' option from the Join tools dropdown toolbar button.
    ![320px](images/JoinFeatures_Example_step3_Cutout.png)

## Algorithm

The algorithms behind Join tools are quite simple, and understanding them is important to use the tools correctly.

1\. Base object is [boolean-cut](Part_Cut.md) with Tool object. The resulting shape is a set ([compound](Part_Compound.md)) of non-intersecting solids (typically, two).

2\. The resulting compound is filtered: only the largest solid is kept.

3\. If Refine property is true, the resulting shape is [refined](Part_RefineShape.md).
![800px](images/JoinFeatures-Algo-Cutout.png)

### Notes

-   If after step 1, the object remains in one piece, the result of Cutout will be equivalent to [boolean cut](Part_Cut.md) of Base with Tool.
-   Now, the tool will produce unexpected result, if a compound is supplied as Base. This may be changed in the future.
-   Because the largest piece is determined by comparing volumes of pieces, the tool can only work with solids. This may be changed in the future.

## Scripting

The Join tools can by used in [macros](macros.md) and from the python console by using the following function:


```pythonJoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout')```

-   Creates an empty Cutout feature (or other Join feature, depending on mode passed). The properties Base and Tool must be assigned explicitly, afterwards.
-   Returns the newly created object.

Example: {{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

The tool itself is implemented in Python, see **/Mod/Part/JoinFeatures.py** ([Github link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) under where FreeCAD is installed.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinCutout/en
