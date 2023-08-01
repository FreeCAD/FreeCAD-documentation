---
- GuiCommand:
   Name: Arch SectionPlane
   Name/ro: Arch SectionPlane
   MenuLocation: Arch - Section Plane
   Workbenches: [Arch](Arch_Workbench/ro.md)
   Shortcut: **S** **P**
   SeeAlso: [Draft Shape2DView](Draft_Shape2DView.md), [TechDraw NewArch](TechDraw_ArchView.md)
---

# Arch SectionPlane/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrumetn plasează în documentul curent un plan de secțiune gizmo, care definește secțiunea sau planul de vizualizare. Gizmo își ia locul în conformitate cu planul de lucru [ Draft Work Plan](Draft_SelectPlane.md) și poate fi mutat și reorientat prin mutarea și rotirea acestuia, până când descrie vizualizarea 2D pe care doriți să o obțineți. Obiectul plan de secțiune va lua în considerare numai un anumit set de obiecte. Obiectele selectate la crearea unei planuri de secțiune vor fi adăugate la setarea automată. Alte obiecte pot fi adăugate sau eliminate mai târziu dintr-un obiect SectionPlane cu ajutorul instrumentelor [Arch Add](Arch_Add.md) și [Remove Arch](Arch_Remove.md) sau prin dublu clic pe planul de secțiuni din vizualizarea arborescentă.


</div>

The Section Plane alone won\'t create any view of its objects set. For that, you must create a [TechDraw ArchView](TechDraw_ArchView.md) to create a view in a [TechDraw page](TechDraw_Workbench.md).

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Optional, definiți [Draft Working Plane](Draft_SelectPlane.md) pentru a reflecta planul unde dirți să plasați Section Plane
2.  Selectați obiecte pe care doriți să le includeți în vizualizarea secțiunii dvs
3.  Apăsați butonul **<img src="images/Arch_SectionPlane.png" width=16px> '''SectionPlane'''
** sau apăsați tastele **S** apoi **P**
4.  [Move](Draft_Move.md)/[rotate](Draft_Rotate.md) the Section Plane into correct position if needed
5.  Selectați Section Plane dacă nu este deja selectați
6.  Folosiți sau [Drawing DraftView](Draft_Drawing.md), [Draft Shape2DView](Draft_Shape2DView.md) sau [TechDraw ArchView](TechDraw_ArchView.md) pentru a crea o vizualizare


</div>



## Opţiuni


<div class="mw-translate-fuzzy">

-   Planul de secțiune va considera doar un set de obiece , nu toate obiectele din document. Obiectele pot fi adăugate sau eliminate dintr-un obiect SectionPlane utilizând instrumentele [Arch Add](Arch_Add.md) și [Arch Remove](Arch_Remove.md) sau făcând dublu clic pe planul de secțiuni din vizualizarea arborescentă, selectând obiecte fie în lista din Scena 3D și apăsarea butonului **adăuga** sau **ștergeți**.


</div>


<div class="mw-translate-fuzzy">

-   Cu un plan de secțiune obiect selectat, utilizați instrumentul [Draft Shape2DView](Draft_Shape2DView.md) pentru a crea un obiect tip formă reprezentând vizualizarea secțiunii în document


</div>

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Create [Drawing DraftViews](Draft_Drawing.md) if you are working with the [Drawing Workbench](Drawing_Workbench.md), or [TechDraw ArchView](TechDraw_ArchView.md) if you are using the [TechDraw Workbench](TechDraw_Workbench.md).


</div>

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   Planul secțiunii poate fi, de asemenea, utilizat pentru a arăta întreaga vedere 3D tăiată printr-un plan infinit. Aceasta este doar vizuală și nu va afecta geometria obiectelor tăiate.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">



## Proprietăți


<div class="mw-translate-fuzzy">

-    **Only Solids**: If this is True, non-solid objects in the set will be disregarded

-    **Display Length**: The length of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Display Height**: The height of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Arrow Size**: The size of the arrows of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Cut View**: If this is true, the whole 3D view will be cut at the location of this section plane (experimental).


</div>

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App::PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Section Plane poate fi utilizat în [macros](macros.md) și de la consola Python utilizând următoarele funcții:


</div>


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```


<div class="mw-translate-fuzzy">


:   Creates a Section plane objects including the given objects.


</div>

Exempluː


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SectionPlane/ro
