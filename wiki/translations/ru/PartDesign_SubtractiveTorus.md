---
- GuiCommand:/ru
   Name/ru:Субтрактивный тор
   Name:PartDesign_SubtractiveTorus
   MenuLocation:Part Design → Создать субтрактивный примитив → Субтрактивный тор
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать субтрактивный примитив](PartDesign_CompPrimitiveSubtractive/ru.md)
---

## Описание

Inserts a subtractive torus in the active Body. Its shape is subtracted from the existing solid.

![](images/PartDesign_SubtractiveTorus_example.svg ) *On the left: active body (A) shown in grey and subtractive torus (B) shown in transparent red; result on the right.*

## Применение

1.  Press the **<img src="images/PartDesign_SubtractiveTorus.svg" width=24px> '''Subtractive Torus'''** button. **Note**: the Subtractive Torus is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Subtractive Box is the one displayed in the toolbar. To get the Torus, click on the down arrow besides the visible icon and select Subtractive Torus in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Torus feature appears under the active Body.

## Опции

The Torus can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Свойства

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: Label given to the Torus object. Change to suit your needs.

-    **Radius1**: Radius of the imaginary orbit around which the circular cross-section revolves. (The distance between the center of the torus and the center of the revolving cross section)

-    **Radius2**: Radius of the circular cross-section defining the form of the torus.

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the torus, parallel to the circular cross section (-180° in a full torus). A bug in the sources causes unexpected results at changing Angle1.

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (180° in a full torus). A bug in the sources causes unexpected results at changing Angle2.

-    **Angle3**: (labelled *U parameter* in the Primitive parameters) angle of rotation of the circular cross section (360° in a full torus).





{{PartDesign Tools navi

}}  
