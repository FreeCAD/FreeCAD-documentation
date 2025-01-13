---
 GuiCommand:
   Name/ru: Создать опорную точку
   Name: PartDesign_Point
   MenuLocation: Part Design , Create a datum , Создать опорную точку
   Workbenches: PartDesign_Workbench/ru
   Version: 0.17
   SeeAlso: PartDesign_Line/ru, PartDesign_Plane/ru
---

# PartDesign Point/ru



## Описание

Создает **опорную точку**, которую можно использовать для размещения эскизов или другой опорной геометрии.

![](images/DatumPoint.png ) 
*A datum point attached to a sphere with an attachment offset of {{Value|2* in the Z direction.}}



## Применение

1.  Press the **<img src="images/PartDesign_Point.svg" width=24px> '''Create a datum point'''** button.
2.  Define Point parameters. Select a first reference in the 3D view to filter the available attachment modes.
3.  Depending on the selected reference, there may be one or more attachment modes available in the the list. The most likely one will automatically be selected and shown in bold in the list. The text *Attached with mode* along with the attachment mode name will appear in green at the top of the Parameters panel.
4.  To add an additional reference, press the next **Reference** button. Once pressed its label changes to *Selecting\...* until a selection is made.
5.  Select an attachment mode in the list.
6.  Define Attachment Offset values.
7.  Press **OK**.



## Опции

Double-click the DatumPoint label in the Model tree or right-click and select **Edit datum** in the contextual menu to edit its parameters. For more details about Attachment mode and Attachment offset, see [Part EditAttachment](Part_EditAttachment.md).

## Preferences

See [PartDesign Plane](PartDesign_Plane#Preferences.md).



## Свойства

-    **MapMode**: lists the attachment mode used.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Label**: name given to the object, this name can be changed at convenience.



## Ограничения

-   The datum point cannot be used as section for Pipe and Loft features.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/ru
