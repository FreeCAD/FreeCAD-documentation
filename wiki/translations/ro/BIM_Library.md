---
- GuiCommand:Addon
   Name:BIM Library
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench.md)
   Addon:BIM
   MenuLocation:3D Modeling → Library
   SeeAlso:[[Arch Equipment]]
---

# BIM Library/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Bibliotecă vă permite să plasați, în modelul curent, un obiect din [FreeCAD Parts Library](Parts_Library.md), care trebuie instalat prin [Addon Manager](Addon_Manager.md) pentru ca acest instrument să fie disponibil.


</div>

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;">


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/BIM_Library.png" width=16px> '''BIM Library'''
**
2.  Faceți clic pe un fișier din bibliotecă
3.  Faceți dublu clic pe el sau apăsați butonul **Insert**
4.  Faceți clic pe un punct din vizualizarea 3D sau introduceți manual o coordonată pentru a plasa obiectul


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   Fișierele FCStd, STEP și BREP sunt acceptate. Numai fișierele STEP și BREP pot fi plasate. Fișierele FCStd nu vă vor permite să alegeți o destinație de plasare, deoarece acestea ar putea fi compuse dintr-o serie complexă de obiecte cu poziții importante. Atunci când alegeți un fișier FCStd, conținutul acestuia va fi introdus în poziția definită în fișier.
-   Obiectele STEP și BREP sunt inserate ca \[\[Echipamente Arch\] \|\] fără formă de bază separată. Adăugarea unei forme de bază la aceste obiecte după aceea va distruge forma lor actuală.
-   La plasarea unui obiect, puteți alege punctul lor de inserție între original (punctul (0,0,0) definit în fișier), de sus, de mijloc, de jos și de stânga, de centru și de dreapta.


</div>


 

_

---
[documentation index](../README.md) > [BIM](Category_BIM.md) > BIM Library/ro
