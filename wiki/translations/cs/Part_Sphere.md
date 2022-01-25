# Part Sphere/cs
---
- GuiCommand:/cs   Name:Part Sphere   Name/cs:Díl Koule   MenuLocation:Díl -> Koule   |Workbenches:[SeeAlso:[[Part_CreatePrimitives/cs|Díl Vytváření zákl.geom.tvarů](Part_Workbench/cs___Modul_Díl]],_Kompletace.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

Vytvoří jednoduchou parametrickou kouli podle parametrů pozice, úhel1, úhel2, úhel3 a poloměr.


</div>

<img alt="" src=images/SimpleSphere.jpg  style="width:400px;">

## Usage


<div class="mw-translate-fuzzy">

## Použití

V pracovní ploše [Díl](Part_Workbench/cs.md) klikněte na ikonu koule <img alt="" src=images/Part_Sphere.png  style="width:32px;">. Koule bude při vytvoření umístěna do počátečního bodu (bod 0,0,0). Parametry úhly dovolují vytvořit částečnou kouli místo celé koule (defaultně jsou nastaveny na 360°)


</div>

**Result:** The sphere will be positioned at origin (point 0,0,0) on creation. The angle parameters permit to make a portion of sphere instead of a full sphere (they are set to 360° by default).

The properties of the object can be edited, either in the [Property editor](Property_editor.md) or by double-clicking the object in the [Tree view](Tree_view.md).


<div class="mw-translate-fuzzy">

## Volby


</div>

### Data


{{TitleProperty|Sphere}}

-    **Radius:**Radius of the sphere

-    **Angle 1:**1nd angle to cut / define the sphere

-    **Angle 2:**2nd angle to cut / define the sphere

-    **Angle 3:**3rd angle to cut / define the sphere

Because it is quite difficult to explain the meaning of the parameters angle 1, angle 2, angle 3, the picture below gives an explanation about these parameters with following values: angle 1 = -45°, angle 2 = 45° and angle 3= 90°.

<img alt="" src=images/SphereCutThreeAngles.jpg  style="width:400px;">

## Scripting

A Part Sphere can be created using the following function:


```python
sphere = FreeCAD.ActiveDocument.addObject("Part::Sphere", "mySphere")
```

-   Where {{Incode|"mySphere"}} is the name for the object.
-   The function returns the newly created object.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/cs
