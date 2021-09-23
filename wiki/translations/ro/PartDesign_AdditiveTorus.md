# PartDesign AdditiveTorus/ro
---
- GuiCommand:   Name:PartDesign AdditiveTorus   Workbenches:[MenuLocation:Part Design → Create an additive primitive → Additive Torus   Shortcut:   SeeAlso:[[PartDesign CompPrimitiveAdditive](PartDesign_Workbench___PartDesign]].md)---


</div>

## Descriere

Inserează o primitivă geometrică tip tor în Corpul activ ca prima funcție(onalitate) sau se conectează la funcționalitățile existente.

<img alt="" src=images/PartDesign_AdditiveTorus_example.png  style="width:200px;">


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/PartDesign_AdditiveTorus.png" width=24px> '''Additive Torus'''** . **Note**: the Additive Torus is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Torus, click on the down arrow besides the visible icon and select Additive Torus in the menu.
2.  Set the Primitive parameters and [Attachment](Part_Attachment.md).
3.  Click **OK**.
4.  OP funcție Tor apare sub Corpul activ.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Torul poate fi definit după crearea sa în două moduri:

-   Dublu-click pe el în arborescența Model, sau click dreapta și selectarea **Edit primitive** în meniul contextual; Acest lucru face să apară parametrii
-   Via [Property editor](Property_editor.md).


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Attachment**: definește atașamentul ca și Attachment Offset. A se vedea [Part Attachment](Part_Attachment.md).

-    **Label**: Label given to the Torus object. Change to suit your needs.

-    **Radius1**: Radius of the imaginary orbit around which the circular cross-section revolves. (The distance between the center of the torus and the center of the revolving cross section)

-    **Radius2**: Radius of the circular cross-section defining the form of the torus.

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the torus, parallel to the circular cross section (-180 degrees in a full torus). A bug in the sources causes unexpected results at changing Angle1.

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (180 degrees in a full torus). A bug in the sources causes unexpected results at changing Angle2.

-    **Angle3**: (marcată cu parametrul \"U\" în parametrii Primitive) unghiul de rotație al secțiunii circulare (360 de grade într-un tor complet).


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveTorus/ro
