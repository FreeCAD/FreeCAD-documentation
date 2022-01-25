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

See also: [Property editor](Property_editor.md).

An Arch BuildingPart is derived from an [App GeoFeature](App_GeoFeature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Group|LinkList**: List of referenced objects.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**: The computed floor area of this floor.

-    **Height|Length**: The height of this object, and of its children objects. The children objects could be, for example, [Arch Walls](Arch_Wall.md). Each wall\'s height must be set to `0` (zero), so the height property of the BuildingPart propagates to the objects inside of it.

-    **Level Offset|Length**: The level of the (0,0,0) point of this level. This value is added to the `Placement.Base.z` attribute of the BuildingPart, to indicate a vertical offset without actually moving the object. The resulting offset is displayed if **Show Level** is `True`.

-    **Materials Table|Map|Hidden**: A MaterialName:SolidIndexesList map that relates material names with solid indexes to be used when referencing this object from other files.

-    **Only Solids|Bool**: If true, only solids will be collected by this object when referenced from other files.

-    **Saved Inventor|FileIncluded|Hidden**: This property stores an inventor representation for this object.

-    **Shape|PartShape|Hidden**: The shape of this object.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**: If true, the height value propagates to contained objects.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**: IFC data.

-    **Ifc Properties|Map|Hidden**: IFC properties of this object.

-    **Ifc Type|Enumeration**: The IFC type of this object.


{{TitleProperty|IFC Attributes}}

-    **Description|String**: An optional description for this component

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**: An optional tag for this component.

-    **User Defined Partitioning Type|String**
    

### View


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**: Automatically set the capture box size from the Building Part contents. <small>(v0.20)</small> 

-    **Autogroup Box|Bool**: Turns auto grouping (and the display of the capture box) on/off. <small>(v0.20)</small> 

-    **Autogroup Margin|Length**: A margin to use when autosize is turned on. <small>(v0.20)</small> 

-    **Autogroup Size|IntegerList**: The capture box for newly created objects expressed as \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. <small>(v0.20)</small> 


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**: The individual face colors.

-    **Display Offset|Placement**: A transformation to apply to the level mark.

-    **Font Name|Font**: The font to be used for texts.

-    **Font Size|Length**: The font size of texts.

-    **Line Width|Float**: The line width of this object.

-    **Origin Offset|Bool**: If true, when activated, Display offset will affect the origin mark too.

-    **Override Unit|String**: An optional unit to express levels.

-    **Show Label|Bool**: If true, when activated, the object\'s label is displayed.

-    **Show Level|Bool**: If true, show the level.

-    **Show Unit|Bool**: If true, show the unit on the level tag.


{{TitleProperty|Children}}

-    **Children Line Color|Color**: The line color to apply to the children of this Building Part.

-    **Children Line Width|Float**: The line width to apply to the children of this Building Part.

-    **Children Override|Bool**: If true, the objects contained in this Building Part will adopt these line, color and transparency settings.

-    **Children Shape Color|Color**: The shape color to apply to the children of this Building Part.

-    **Children Transparency|Percent**: The transparency to apply to the children of this Building Part.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**: Turn cutting on when activating this level.

-    **Cut Margin|Length**: The distance between the level plane and the cut line.

-    **Cut View|Bool**: Cut the view above this level.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**: If set to True, the working plane will be kept on Auto mode.

-    **Double Click Activates|Bool**: If True, double-clicking this object in the tree activates it.

-    **Restore View|Bool**: If set, the view stored in this object will be restored on double-click.

-    **Save Inventor|Bool**: If this is enabled, the inventor representation of this object will be saved in the FreeCAD file, allowing to reference it in other files in lightweight mode.

-    **Saved Inventor|FileIncluded|Hidden**: A slot to save the inventor representation of this object, if enabled.

-    **Set Working Plane|Bool**: If true, when activated, the working plane will automatically adapt to this Building Part.

-    **View Data|FloatList|Hidden**: Camera position data associated with this object.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul BuildingPart poate fi utilizat în [macro-uri](Macros/ro.md) și din consola Python utilizând următoarea funcție:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/ro
