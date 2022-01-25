---
- GuiCommand:
   Name:PartDesign CoordinateSystem
   MenuLocation:PartDesign → Create a local coordinate system
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.18
   SeeAlso:[PartDesign Datum point](PartDesign_Point.md), [PartDesign Datum line](PartDesign_Line.md), [PartDesign Datum plane](PartDesign_Plane.md)
---

# PartDesign CoordinateSystem/pt-br

## Description

Creates a **local coordinate system** which can be used as reference for other datum geometry. It also helps identify the orientation of the referenced datum geometry in 3D space. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) 
*Local coordinate system originating out of a datum plane's origin.*

## Usage

1.  Press the **[<img src=images/PartDesign_CoordinateSystem.svg style="width:16px"> [Create a local coordinate system](PartDesign_CoordinateSystem.md)** button.
2.  Define Coordinate System parameters. Select a first reference in the 3D view to filter the available attachment modes.
3.  Depending on the selected reference, there may be one or more attachment modes available in the the list. The most likely one will automatically be selected and shown in bold in the list. The text *Attached with mode* along with the attachment mode name will appear in green at the top of the Parameters panel.
4.  To add an additional reference, press the next **Reference** button. Once pressed its label changes to *Selecting\...* until a selection is made.
5.  Select an attachment mode in the list.
6.  Define Attachment Offset values.
7.  Press **OK**.

## Options

Double-click the **Local\_CS** label in the Model tree or right-click and select **Edit datum** in the contextual menu to edit its parameters. For more details about Attachment mode and Attachment offset, see [Attachment](Part_EditAttachment.md).

## Properties

### Data

-    **MapMode**: lists the attachment mode used.

-    **Attachment Reversed**: indicates if the coordinate system is reversed in orientation.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Placement**: indicates the coordinates and alignment of the coordinates system´s origin .

-    **Label**: name given to the object, this name can be changed at convenience.

## Scripting


```python
lcs = App.activeDocument().addObject( 'PartDesign::CoordinateSystem', 'LCS' )
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign CoordinateSystem/pt-br
