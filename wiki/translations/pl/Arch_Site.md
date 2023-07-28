---
- GuiCommand:
   Name:Arch Site
   Workbenches:[Arch](Arch_Workbench.md)
   MenuLocation:Arch → Site
   Shortcut:**S** **I**
   SeeAlso:[Arch Floor](Arch_Floor.md), [Arch Building](Arch_Building.md)
---

# Arch Site/pl

## Description

The Arch Site is a special object that combines properties of a standard FreeCAD group object and Arch objects. It is particularly suited for representing a whole project site, or terrain. In IFC-based architectural work, it is mostly used to organize your model, by containing [building](Arch_Building.md) objects. The site is also used to manage and display a physical terrain, and can compute volumes of earth to be added or removed.

## Usage

1.  Optionally, select one or more objects to be included in your new site.
2.  Press the **<img src="images/Arch_Site.svg" width=16px> [Arch Site](Arch_Site.md)** button, or press the **S** then **I** keys.

## Options

-   After creating a site, you can add objects to it by drag and dropping them in the [Tree view](Tree_view.md) or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool. This only determines which objects are part of the given site, and has no effect on the terrain.
-   You can remove objects from a site by drag and dropping them out of it in the [Tree view](Tree_view.md) or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.
-   You can add a terrain object by editing the Site\'s **Terrain** property. The terrain can be an open shell or (<small>(v0.21)</small> ) a solid.
-   You can add volumes to be added or subtracted from the base terrain, by double-clicking the Site, and adding objects to its Additions or Subtractions groups. The objects must be solids.
-   The **Extrusion Vector** property can be used to solve some problems that can appear when the terrain is an open shell and there are additions and/or subtractions. In order to perform those additions/subtractions, the open shell is extruded into a solid, which is then appropriately unioned/subtracted. Depending on the terrain topology, this extrusion might fail with the default extrusion vector. You might then be able to remedy the problem by changing this to a different value. This property is ignored if the terrain is a solid.

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


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Site tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Creates a `Site` object from `objectslist`, which is a list of objects, or `baseobj`, which is a `Shape` or `Terrain`.

Example: 
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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Site/pl
