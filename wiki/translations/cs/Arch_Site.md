# Arch Site/cs
---
- GuiCommand:   Name:Arch Site   Name/cs:Arch Site   Workbenches:[MenuLocation:Arch - Site   Shortcut:S I   SeeAlso:[[Arch Floor/cs|Arch Floor](Arch_Workbench/cs___Arch]].md), [Arch Building](Arch_Building/cs.md)---


</div>



## Popis


<div class="mw-translate-fuzzy">

Staveniště je speciální typ skupinového objektu FreeCADu zvlášť vhodný pro zobrazení celého staveniště nebo terénu. Většinou se používá pro uspořádání modelu obsahujícího objekty [Stavba](Arch_Building/cs.md)


</div>




<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Volitelně lze vybrat jeden nebo více objektů, které lze vložit do Vašeho nového staveniště
2.  Stiskněte tlačítko **<img src="images/Arch_Site.png" width=16px> '''Staveniště'''
** nebo klávesy **S** a **I**


</div>



## Volby


<div class="mw-translate-fuzzy">

-   Po vytvoření staveniště můžete přidávat další objekty pomocí myši přetáhnutím a upuštěním (drag and drop) na požadované místo v panelu stromu nebo použitím nástroje <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Přidat](Arch_Add/cs.md)
-   Odstranit objekty ze staveniště můžete podobně myší přetáhnutím a upuštěním objektu mimo panelu stromu nebo použitím nástroje <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Odebrat](Arch_Remove/cs.md).


</div>

## Properties

### Data

-    **Terrain**: The base terrain of this site

-    **Address**: The street and housenumber of this site

-    **Postal Code**: The postal or zip code of this site

-    **City**: The city of this site

-    **Country**: The country of this site

-    **Latitude**: The latitude of this site

-    **Longitude**: The longitude of this site

-    **Url**: An url that shows this site in a mapping website

-    **Projected Area**: The area of the projection of this object onto the XY plane

-    **Perimeter**: The perimeter length of this terrain

-    **Addition Volume**: The volume of earth to be added to this terrain

-    **Subtraction Volume**: The volume of earth to be removed from this terrain

-    **Extrusion Vector**: An extrusion vector to use when performing boolean operations

-    **Remove Splitter**: Remove splitters from the resulting shape

-    **Declination**: The angle between the true North and the North direction in this document, that is, the Y axis. This means that by default North points to the Y axis, and East to the X axis; the angle increments counterclockwise. This property was previously known as **North Deviation**.

-    **EPW File**: Allow to attach an EPW file from the [Ladybug EPW data website](https://www.ladybug.tools/epwmap/) to this site. This is needed to display wind rose diagrams

### View

-    **Solar Diagram**: Shows or hides the solar diagram

-    **Solar Diagram Color**: The color of the solar diagram

-    **Solar Diagram Position**: The position of the solar diagram

-    **Solar Diagram Scale**: The scale of the solar diagram

-    **Wind Rose**: Shows or hides the wind rose diagram (requires the **EPW File** data property filled, and the Ladybug Python module installed (see below)

## Typical workflow 

Start by creating an object that represents your terrain. For example, it is easy to import mesh data, that can be turned into a Part Shape from menu **Part → Create Shape from Mesh**. Then, create a Site object, and set its **Terrain** property to the Part we just created:

![](images/Arch_site_example_01.jpg )

Create some volumes (they must be solids) that represent the areas that you wish to be excavated or filled. Double-click the Site object in the Tree View, and add these volumes to the Additions or Subtractions groups. Click OK.

![](images/Arch_site_example_02.jpg )

The site geometry will be recomputed and the areas, perimeter, and volumes properties recalculated.

![](images/Arch_site_example_03.jpg )

## Solar and wind diagrams 

If [Ladybug](https://www.ladybug.tools/ladybug.html) is installed on your system, [Arch Sites](Arch_Site.md) can display a solar diagram and/or a wind rose. For this, **Longitude**, **Latitude** and **Declination** (previously **North Deviation**) must be correctly set, and **Solar Diagram** or **Wind Rose** set to `True`.

**Note**: If you don\'t have Ladybug, [pysolar](http://pysolar.org/) is still supported to generate solar diagrams, but not wind roses. Pysolar 0.7 or above is required; this version only works with Python 3. If you require this feature with Python 2, you should have Pysolar 0.6 as this is the last version that works with Python 2. However, Ladybug is a much more powerful tool that will probably be used more in the future, so we recommend using it instead of pysolar. Ladybug can be installed simply via [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Staveniště může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```


<div class="mw-translate-fuzzy">

vytvoří staveniště včetně objektů ze seznamu objectslist


</div>

Příklad: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```

### Solar diagram 

As long as the `pysolar` module is present, a solar diagram can be added to the site. Set the longitude, latitude and declination angles as appropriate, as well as an adequate scale for the size of your model.

Please note that Pysolar 0.7 or above is required, and this version only works with Python 3.


```python
Site.Longitude = -46.38
Site.Latitude = -23.33
Site.Declination = 30
#Site.Compass = True

Site.ViewObject.SolarDiagram = True
Site.ViewObject.SolarDiagramScale = 10000
FreeCAD.ActiveDocument.recompute()
```

### Solar diagram independent of Site 

A solar diagram can be created with the following function, independently of any site. 
```python
Node = makeSolarDiagram(longitude, latitude, scale=1, complete=False)
```

-   Creates a solar diagram as a Pivy node, using `longitude` and `latitude`, with an optional `scale`.
-   If `complete` is `True`, the 12 months are drawn, which shows the full solar [analemma](https://en.wikipedia.org/wiki/Analemma).


```python
import FreeCADGui, Arch

Node = Arch.makeSolarDiagram(-46.38, -23.33, scale=10000, complete=True)
FreeCAD.Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(Node)
```


<div class="mw-translate-fuzzy">


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Site/cs
