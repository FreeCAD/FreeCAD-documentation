---
- GuiCommand:/ru
   Name/ru:Создать опорную плоскость
   Name:PartDesign_Plane
   MenuLocation:Part Design → Create a datum → Создать опорную плоскость
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать опорную точку](PartDesign_Point/ru.md), [Создать опорный отрезок](PartDesign_Line/ru.md)
---

# PartDesign Plane/ru

## Описание

Создает **опорную плоскость**, которую можно использовать для размещения эскизов или другой опорной геометрии. Эскизы можно размещать на опорных плоскостях. ![](images/Datum_plane.png ) *Datum Plane crossing 3 corners of the Cube with a Cylinder sketched on it using the Datum Plane as its X-Y Plane.*

## Требования

A datum plane, as of FreeCAD 0.18, can only be created inside of a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Body](PartDesign_Body.md). Every body has an origin, which is hidden by default. To be able to refer to the origin base planes, make the the origin visible. You can do this before creating a datum plane.

## Применение

1.  Press the **<img src="images/PartDesign_Plane.svg" width=16px> [Create a datum plane](PartDesign_Plane.md)** button.
2.  Define Plane parameters. Select a first reference in the 3D view to filter the available [attachment](Part_EditAttachment.md) modes.
3.  Depending on the selected reference, there may be one or more attachment modes available in the the list. The most likely one will automatically be selected and shown in bold in the list. The text *Attached with mode* along with the attachment mode name will appear in green at the top of the Parameters panel.
4.  To add an additional reference, press the next **Reference** button. Once pressed its label changes to *Selecting\...* until a selection is made.
5.  Select an attachment mode in the list.
6.  **Offsets:** Define Attachment Offset values. **Note** that the x, y and z offset represent the local coordinate system of the datum plane, not the world coordinate system. Therefore the z-offset is always the offset along the datum plane normal vector.
7.  **Rotation:** Changing \"Around x-axis\" makes the plane rotate around its local X-axis. Changing \"Around y-axis\" makes the plane rotate around its local Y-axis. Changing \"Around z-axis\" makes the plane rotate around its local Z-axis.
8.  Press **OK**.

## Опции

Double-click the DatumPlane label in the Model tree or right-click and select **Edit datum** in the contextual menu to edit its parameters. For more details about Attachment mode and Attachment offset, see [Part EditAttachment](Part_EditAttachment.md).

## Свойства

-    **MapMode**: lists the attachment mode used.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Label**: name given to the object, this name can be changed at convenience.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Plane/ru
