# PartDesign AdditiveWedge/ro
---
- GuiCommand:   Name:PartDesign AdditiveWedge   Workbenches:[MenuLocation:Part Design → Create an additive primitive → Additive Wedge   Shortcut:None   SeeAlso:[[PartDesign CompPrimitiveAdditive](PartDesign_Workbench___PartDesign]].md)---


</div>

## Descriere

Inserează o primitivă geometrică tip pană în corpul activ ca prima funcție(onalitate) sau se conectează la funcționalitățile existente.

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;">


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/PartDesign_AdditiveWedge.png" width=24px> '''Additive Wedge'''** . **Note**: the Additive Wedge is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Wedge, click on the down arrow besides the visible icon and select Additive Wedge in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  O funcție tip Pană apare sub Corpul activ.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Pana(Wedge) poate fi editată după crearea ei în douăî moduri:

-   Dublu-clicking în arborescența Model, sau prin clic drapta și selectarea **Edit primitive** ăn meniul contextula; aceasta aduce parametrii Primitive .
-   Via [Property editor](Property_editor.md).


</div>

## Proprietăți

Utilizarea plasamentului implicit, intrările de mai jos sunt:

-    **X min/max**: Base face X axis span

-    **Y min/max**: Wedge height span

-    **Z min/max**: Base face Z axis span

-    **X2 min/max**: Top face X axis span

-    **Z2 min/max**: Top face Z axis span

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge/ro
