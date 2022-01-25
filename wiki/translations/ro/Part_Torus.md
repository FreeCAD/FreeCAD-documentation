---
- GuiCommand:/ro
   Name:Part Torus
   Name/ro:Part Torus
   MenuLocation:Part → Torus
|
   Workbenches:[Part](Part_Workbench/ro.md), Complete
   SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives/ro.md)
---

# Part Torus/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Creează un tor simplu parametric, cu parametrii de poziție, unghi1, unghi2, unghi 3, raza1 și raza2.


</div>

<img alt="" src=images/SimpleTorus.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

În bara de lucru [Part](Part_Workbench.md) faceți clic pe pictograma torus <img alt="" src=images/_Part_Torus.png  style="width:32px;">. Torusul va fi poziționat la origine (punctul 0,0,0) la crearea. Parametrii unghiului (unghiul1, unghiul2, unghiul3), precum și parametrii razei (raza1, raza2) permit parametrizarea torusului, a se vedea paragraful următor.


</div>

**Result:** The torus will be positioned at origin (point 0,0,0) on creation.
The angle parameters (angle1, angle2, angle3), as well as the radius parameters (radius1, radius2) permit to parametrize the torus, see next section.

## Opțiuni

![](images/TorusExampleOverviewParameters.jpg )

**Parameter**

A torus can be assimilated to a small disc that makes a circular orbit around an imaginary axe. Thus the parametric torus is defined by the following parameters:

-    {{Parameter|Radius1:}}Raza cercului în jurul căruia circulă discul

-    {{Parameter|Radius2:}}Raza discului care definește forma torului

-    {{Parameter|Angle1:}}un unghi pentru a tăia / defini discul torului

-    {{Parameter|Angle2:}}al doilea unghi pentru a tăia / defini discul torului

-    {{Parameter|Angle3:}}al treilea unghi pentru a defini circumferința torului.

precum și setul standard de parametri de plasare. Imaginile de mai jos oferă o imagine de ansamblu vizuală a parametrilor menționați antecedent:

![](images/TorusExampleRadius1.jpg ) The parameter Radius1 has a value of 20 mm.

![](images/TorusExampleRadius2.jpg ) The parameter Radius2 has a value of 2 mm.

![](images/TorusExampleAngle1.jpg ) The parameter Angle1 has a value of -90°. Notice that, the \"angle measure\" tool cannot display negative angle. Considered the displayed value in picture as \"-90°\".

![](images/TorusExampleAngle2.jpg ) The parameter Angle2 has a value of 90°.


<div class="mw-translate-fuzzy">

![](images/TorusExampleAngle3.jpg ) The parameter Angle3 has a value of 90°.


</div>

## Scripting

A Part Torus can be created using the following function:


```python
torus = FreeCAD.ActiveDocument.addObject("Part::Torus", "myTorus")
```

-   Where {{Incode|"myTorus"}} is the name for the object.
-   The function returns the newly created object.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Torus/ro
