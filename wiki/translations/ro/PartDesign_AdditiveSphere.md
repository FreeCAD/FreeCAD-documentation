# PartDesign AdditiveSphere/ro
---
- GuiCommand:   Name: PartDesign AdditiveSphere   Workbenches: [MenuLocation: Part Design - Create an additive primitive - Additive Sphere   Shortcut: None   SeeAlso: [[PartDesign CompPrimitiveAdditive](PartDesign_Workbench___PartDesign]].md)---


</div>

## Descriere

Inserează o primitivă geometrică tip sferă în Corpul activ ca prima funcție(onalitate) sau se conectează la funcționalitățile existente.

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/PartDesign_AdditiveSphere.png" width=24px> '''Additive Sphere'''**. **Note**: the Additive Sphere is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Sphere, click on the down arrow besides the visible icon and select Additive Sphere in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  O funcție Sphere apre sub Corpul activ.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Sfera poate fi editată după crearea sa pe două căi:

-   Double-clicking pe ea în arborescența Model, sau right-clicking și selectarea **Edit primitive** în meniul contextual; aceasta deschide parametrii Primitivei geometrice.
-   Via [Property editor](Property_editor.md).


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Attachment**: definește modul de atașarea ca și the Attachment Offset. A se vedea [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: Label given to the Sphere object. Change to suit your needs.

-    **Radius**: Radius of the sphere.

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the sphere, parallel to the circular cross section (-90 degrees in a full sphere)

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (90 degrees in a full sphere).

-    **Angle3**: (etichetat ca parametru U între parametrii Primitive) unghiul de rotație al secțiunii transversale (360 de grade într-o sferă completă).


</div>





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/ro
