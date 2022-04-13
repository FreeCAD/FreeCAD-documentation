---
- GuiCommand:/ru
   Name/ru:Аддитивный клин
   Name:PartDesign_AdditiveWedge
   MenuLocation:Part Design → Создать аддитивный примитив → Аддитивный клин
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать аддитивный примитив](PartDesign_CompPrimitiveAdditive/ru.md), [Субтрактивный клин](PartDesign_SubtractiveWedge/ru.md)
---

# PartDesign AdditiveWedge/ru


</div>

## Описание

Inserts a primitive wedge in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;">

## Применение

1.  Press the **<img src="images/PartDesign_AdditiveWedge.svg" width=24px> '''Additive Wedge'''** button. **Note**: the Additive Wedge is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Wedge, click on the down arrow besides the visible icon and select Additive Wedge in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Wedge feature appears under the active Body.

## Опции

The Wedge can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Свойства

Using the default placement, the below inputs are:

-    **X min/max**: Base face X axis span

-    **Y min/max**: Wedge height span

-    **Z min/max**: Base face Z axis span

-    **X2 min/max**: Top face X axis span

-    **Z2 min/max**: Top face Z axis span

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge/ru
