---
 GuiCommand:
   Name: Arch SectionPlane
   Name/sv: Arch SectionPlane
   MenuLocation: Arch , Section Plane
   Workbenches: Arch_Workbench
   Shortcut: **S** **P**
   SeeAlso: Draft Shape2DView, TechDraw_ArchView
---

# Arch SectionPlane/sv


</div>



## Beskrivning


<div class="mw-translate-fuzzy">

Detta verktyg placerar en sektionplansvisare i nuvarande dokument, vilken definierar ett tvärsnitt eller vy-plan. visaren kan omplaceras och omorienteras genom att flytta och rotera den, tills den visar den 2D vy som du vill erhålla. Om verktyget används utan att några objekt är markerade, så kommer alla objekt från scenen att inkluderas i 2D vyn. Om några objekt är markerade, så kommer 2D vyn endast att visa dessa objekt.


</div>


<div class="mw-translate-fuzzy">

Objekt kan senare adderas eller tas bort från ett SectionPlane objekt med [Arch Add](Arch_Add/sv.md) och [Arch Remove](Arch_Remove/sv.md) verktygen.

Vid skapandet, så skapar SectionPlane objekt för närvarande ett [Ritningssida](Drawing_Workbench/sv.md) objekt vilken innehåller den projicerade 2D vyn av de objekt som behandlas av Section Plane.


</div>

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;"> Till vänster i bilden ovan placeras ett Section Plane objekt i scenen, och till höger dess SVG 2D representation. Ytsortering är för närvarande inte helt implementerad.




<div class="mw-translate-fuzzy">

#### Bruk


</div>


<div class="mw-translate-fuzzy">

-   Välj objekt
-   Klicka på <img alt="" src=images/Arch_SectionPlane.png  style="width:16px;"> **SectionPlane** knappen
-   Flytta/rotera Section Plane till korrekt position
-   Klicka på <img alt="" src=images/Std_Recompute.png  style="width:16px;"> **Beräkna om** knappen för att uppdatera vyn


</div>

## Options

-   The Section plane object will only consider a certain set of objects, not all the objects of the document. Objects can be added or removed from a SectionPlane object by using the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools, or by double-clicking the Section Plane in the tree view, selecting objects either in the list of in the 3D scene, and pressing the **add** or **remove** buttons.

-   With a section plane object selected, use the [Draft Shape2DView](Draft_Shape2DView.md) tool to create a shape object representing the section view in the document.

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Create [TechDraw ArchView](TechDraw_ArchView.md).

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   The Section Plane can also be used to show the entire 3D view cut by an infinite plane. This is only visual, and won\'t affect the geometry of the objects being cut.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">

## Properties

-    **Only Solids**: If this is True, non-solid objects in the set will be disregarded

-    **Display Length**: The length of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Display Height**: The height of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Arrow Size**: The size of the arrows of the section plane gizmo in the 3D view. Doesn\'t affect the resulting view

-    **Cut View**: If this is `True`, the whole 3D view will be cut at the location of this section plane.

-    **Clip view**: if this is `True`, it will clip the view to the display height and length of the section plane. This effectively turns the section plane into an orthographic camera, limiting the field of view.

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App::PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The SectionPlane tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Creates a `Section` object from `objectslist`, which is a list of objects.

Example:


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
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch SectionPlane/sv
