---
- GuiCommand:/ro
   Name:Arch BuildingPart
   Name/ro:Arch BuildingPart
   MenuLocation:Arch → BuildingPart
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:
   SeeAlso:[[Arch Building]], [[Arch Floor]]
---

# Arch BuildingPart/ro


</div>


<div class="mw-translate-fuzzy">

## Descriere


</div>


<div class="mw-translate-fuzzy">

BuildingPart intenționează să înlocuiască [Arch Floor](Arch_Floor.md) cu o versiune mai capabilă care să poată fi utilizată nu numai pentru crearea de podele/etaje/niveluri ci și pentru toate tipurile de situații în care trebuie să fie grupate diferite obiecte Arch/BIM și acel grup ar putea fi necesar să fie tratate ca un obiect sau replicate.


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Optional, selectați unul sau mai multe obiecte pentru a fi incluse în noul Building Part
2.  Apăsați butonul **<img src="images/Arch_BuildingPart.png" width=16px> '''Arch BuildingPart'''
**


</div>

### Notes

BuildingParts have a built-in, implicit [Arch SectionPlane](Arch_SectionPlane.md). <small>(v0.19)</small> 

This plane is always parallel to the BuildingPart\'s base plane, but you can specify the offset between them. So all tools that work with a section plane, such as [Draft Shape2DView](Draft_Shape2DView.md) and [TechDraw ArchView](TechDraw_ArchView.md) also work with BuildingParts.


<div class="mw-translate-fuzzy">

## Opţiuni


</div>


<div class="mw-translate-fuzzy">

-   După ce ați creat un BuildingPart, puteți să adăugați mai multe obiecte prin glisarea și plasarea lor în Tree View sau utilizând instrumentul <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Arch Add](Arch_Add.md)
-   Puteți să eliminați obiecte dintr-un BuildingPart prin tragerea și plasarea lor din Tree View sau utilizând instrumentul <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Arch Remove](Arch_Remove.md)
-   Dând dublu clic pe obiectul BuildingPart din vizualizarea arborescentă, [Working Plane](Draft_SelectPlane.md) va fi setat la locația sa, iar BuildingPart va deveni activ, ceea ce înseamnă că vor fi adăugate automat noi obiecte. Dacă dați dublu clic pe BuildingPart din nou, îl dezactivați și setați planul de lucru înapoi în poziția sa anterioară
-   BuildingPart poate afișa un marcaj în vizualizarea 3D cu o etichetă și indicarea nivelului
-   Când un BuildingPart este mutat / rotit, toți copiii acestuia care nu au nici o proprietate \"Move With Host\" sau o pornesc, se vor mișca/roti împreună.
-   Elementele de construcție pot fi [cloned](Draft_Clone.md)
-   Componentele de construcție pot lua orice tip de IFC


</div>


<div class="mw-translate-fuzzy">

## Proprietăți


</div>


<div class="mw-translate-fuzzy">

-    **Height**: The height of this object

-    **LevelOffset**: The level of the (0,0,0) point of this level

-    **Area**: The computed floor area of this floor

-    **IfcRole**: The role of this object

-    **Description**: An optional description for this component

-    **Tag**: An optional tag for this component

-    **IfcAttributes**: Custom IFC properties and attributes

-    **LineWidth**: The line width of this object

-    **OverrideUnit**: An optional unit to express levels

-    **DisplayOffset**: A transformation to apply to the level mark

-    **ShowLevel**: If true, show the level

-    **ShowUnit**: If true, show the unit on the level tag

-    **SetWorkingPlane**: If true, when activated, the working plane will automatically adapt to this level

-    **OriginOffset**: If true, when activated, Display offset will affect the origin mark too

-    **ShowLabel**: If true, when activated, the object\'s label is displayed

-    **FontName**: The font to be used for texts

-    **FontSize**: The font size of texts

-    **RestoreView**: If set, the view stored in this object will be restored on double-click

-    **DiffuseColor**: The individual face colors


</div>

### View

-    **LineWidth**: The line width of this object

-    **OverrideUnit**: An optional unit to express levels

-    **DisplayOffset**: A transformation to apply to the level mark

-    **ShowLevel**: If true, show the level

-    **ShowUnit**: If true, show the unit on the level tag

-    **SetWorkingPlane**: If true, when activated, the working plane will automatically adapt to this Building Part

-    **OriginOffset**: If true, when activated, Display offset will affect the origin mark too

-    **ShowLabel**: If true, when activated, the object\'s label is displayed

-    **FontName**: The font to be used for texts

-    **FontSize**: The font size of texts

-    **RestoreView**: If set, the view stored in this object will be restored on double-click

-    **DiffuseColor**: The individual face colors


<small>(v0.19)</small> 

-    **ChildrenOverride**: If set, the settings below will affect the children of this Building Part

-    **ChildrenLineWidth**: The line width to apply to the children of this Building Part

-    **ChildrenLineColor**: The line color to apply to the children of this Building Part

-    **ChildrenShapeColor**: The shape color to apply to the children of this Building Part

-    **ChildrenTransparency**: The transparency to apply to the children of this Building Part


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul BuildingPart poate fi utilizat în [macro-uri](macro-uri.md) și din consola Python utilizând următoarea funcție:


</div>


```python
BuildingPart = makeBuildingPart(objectslist=None)
```


<div class="mw-translate-fuzzy">

creează o BuildingPart incluzând obiectele din lista dată.


</div>


<div class="mw-translate-fuzzy">

Exempluː


</div>


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav|[Floor](Arch_Floor.md)|[Building](Arch_Building.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Floor.svg |IconC=Workbench_Arch.svg |IconR=Arch_Building.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/ro
