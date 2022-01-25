# Part Cylinder/ro
---
- GuiCommand:/ro
   Name:Part Cylinder
   Name/ro:Part Cylinder
   MenuLocation:Part -> Cylinder
|
   Workbenches:[Part Workbench](Part_Workbench/ro.md), Complete
   SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives/ro.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Creează un simplu cilindru parametric, cu parametrii de poziție, unghi, rază și înălțime.


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 

În bara de lucru Atelierului [Part](Part_Workbench.md) faceți clic pe pictograma cilindrului ![ 32px](images/_Part_Cylinder.png ). Valoarea prestabilită este pentru poziționarea unui cilindru complet, centrul unei fețe circulare care coincide cu originea globală (punctul 0,0,0), cu o rază de 2 mm și o înălțime de 10 mm.

### Prima metodă 

Faceți clic direct pe butonul {{KEY/it|<img src="images/_Part_Cylinder.png" width=16px> Cilindru}} din bara de instrumente.

Creează un cilindru implicit cu o rază de 2 mm, înălțime de 10 mm și centrul cercului inferior poziționat la origine (punctul 0,0,0).


</div>

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Cylinder.svg" width=16px> Cylinder** button in the toolbar.
    -   Select **Part → Primitives → <img src="images/Part_Cylinder.svg" width=16px> Cylinder** entry from the top menu

**Result:** The default result is a full cylinder with a radius of 2 mm and height of 10 mm, centered along the global z-axis and attached to the global xy-plane.

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="a cylinder created with the Cylinder tool" src=images/cylinder.png  style="width:650px;">


<div class="mw-translate-fuzzy">

## Opțiuni

Proprietățile pot fi ulterior editate în fila de date pentru cilindru:


</div>

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small> 

## Scripting

A Part Cylinder can be created using the following function:


```python
cylinder = FreeCAD.ActiveDocument.addObject("Part::Cylinder", "myCylinder")
```

-   Where {{Incode|"myCylinder"}} is the name for the object.
-   The function returns the newly created object.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/ro
