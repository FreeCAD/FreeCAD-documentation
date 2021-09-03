---
- GuiCommand:/cs   Name:Draft Clone   Name/cs:Kreslení Klon   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Draft → Clone   SeeAlso:[Kreslení Měřítko](Draft_Scale/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Tento nástroj vytváří klon (kopie, která je parametricky svázaná s originálním objektem). Jestliže se změní originální objekt, změní se i klon, ale podrží si svoji pozici, otočení a měřítko.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md). Clones of 2D objects can be used in [PartDesign Bodies](PartDesign_Body.md).

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;">


</div>

## Usage


<div class="mw-translate-fuzzy">

## Použití

1.  Vyberte objekty, které chcete klonovat
2.  Stiskněte tlačítko **<img src="images/Draft_Clone.png" width=16px> [Klon](Draft_Clone/cs.md)
**


</div>

## Properties

See also: [Property editor](property_editor.md).

An object created with the Draft Clone command is derived from a [Part Part2DObject](Part_Part2DObject.md), a [Part Feature](Part_Feature.md) object or, if an Arch Clone is created, from the object type of the source object. It inherits all properties from that object. A clone derived from one of the first two objects also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Měřítko**: Specifikuje volitelné měřítko pro klon

-   Výsledek použití nástroje [Kreslení Měřítko](Draft_Scale/cs.md) je také klon


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Klon může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a clone use the `make_clone` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `clone` method.


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```


<div class="mw-translate-fuzzy">

-   Vytvoří klon(y) zadaného objektu(ů).
-   Klon je přesná, propojená kopie zadaného objektu.
-   Jestliže se změní originální objekt, změní se i finální objekt. Volitelně můžete zadat delta Vektor čímž posunete klon z originální pozice.


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```





 
