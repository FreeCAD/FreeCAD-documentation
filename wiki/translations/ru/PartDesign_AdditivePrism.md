---
- GuiCommand:/ru
   Name/ru:Аддитивная призма
   Name:PartDesign_AdditivePrism
   MenuLocation:Part Design → Создать аддитивный примитив → Аддитивная Призма
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать аддитивный примитив](PartDesign_CompPrimitiveAdditive/ru.md), [Субтрактивная призма](PartDesign_SubtractivePrism/ru.md)
---

## Описание

Inserts a primitive prism in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width:200px;">

## Применение

1.  Press the **<img src="images/PartDesign_AdditivePrism.svg" width=24px> '''Additive Prism'''** button. **Note**: the Additive Prism is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Prism, click on the down arrow besides the visible icon and select Additive Prism in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Prism feature appears under the active Body.

## Опции

It is possible to create skewed prisms by specifying angles in respect to the normal vector of the chosen attachment. <small>(v0.19)</small> 

The Prism can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Свойства

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: label given to the Prism object. Change to suit your needs.

-    **Polygon**: number of sides in the polygon cross-section of the prism.

-    **Circumradius**: [circumscribed radius](https://en.wikipedia.org/wiki/Circumscribed_circle) of the polygon cross-section of the prism.

-    **Height**: height of the prism.

-    **First Angle**: angle in first direction. <small>(v0.19)</small> 

-    **Second Angle**: angle in second direction. <small>(v0.19)</small> 





{{PartDesign Tools navi

}}  
