---
- GuiCommand:   Name:PartDesign SubtractiveTorus   Workbenches:[MenuLocation:Part Design → Create a subtractive primitive → Subtractive Torus   Shortcut:None   SeeAlso:[[PartDesign CompPrimitiveSubtractive](PartDesign_Workbench___PartDesign]].md)---


</div>

## Descriere

Inserează un tor substractiv în Corpul activ. Forma sa este scăzută din solidul existent.

![](images/PartDesign_SubtractiveTorus_example.svg ) *În partea stângă: corpul activ (A) afișat în gri și torul substractiv (B) afișat în roșu transparent; rezultatul în partea dreaptă.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/PartDesign_SubtractiveTorus.png" width=24px> '''Subtractive Torus'''**. **Notă**: torul substractiv face parte din meniul cu iconițe numită *Create an additive primitive*. După lansarea FreeCAD, Cubul Substractiv este afișat implicit în bara de instrumente. Pentru a obține Torul substractiv, faceți clic pe săgeata în jos și alegeți <img alt="" src=images/PartDesign_SubtractiveTorus.png  style="width:24px;"> torul subtractiv din meniu.
2.  Setați parametrii Primitivei și [Attachment](Part_Attachment.md).
3.  Click **OK**.
4.  Un Tor apare sub corpul activ.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

The Torus can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Attachment**: definește modurile de atașare, precum și dispunerea atașamentului. Consultați atașamentul [Part Attachment](Part_Attachment.md).

-    **Label**:Botezați torul, schimbați numele dacă este necesar.

-    **Radius1**: Raza imaginară a orbitei în jurul căreia se rotește secțiunea circulară. (Distanța dintre centrul torului și centrul secțiunii rotative)

-    **Radius2**: Raza secțiunii ciruculare a care definește forma torului

-    **Angle1**: (numit Parametrul V printre parametrii primitivei) paralel cu partea inferioară a secțiunii circulare (-180 ° pentru un torus întreg). O eroare în codul sursă cauzează rezultate neașteptate la editarea Angle1.

-    **Angle2**: (care nu este etichetată printre parametrii primitivei), reprezintă trunchierea superioară a elipsoidului, paralelă cu secțiunea transversală circulară (180 ° într-un tor plin). O eroare în codul sursă provoacă rezultate neașteptate atunci când schimbați Angle2.

-    **Angle3**: (numit parametrul U printre parametrii primitivei) unghiul de rotație a secțiunii circulare (360 ° pentru un tor întreg).


</div>





{{PartDesign Tools navi

}}  
