# Arch Site/ro
---
- GuiCommand:   Name:Arch Site   Workbenches:[MenuLocation:Arch → Site   Shortcut:S I   SeeAlso:[[Arch Floor|Arch Floor](Arch_Workbench/ro___Arch]].md), [Arch Building](Arch_Building.md)---


</div>

## Descriere

Site-ul Arch este un obiect special care combină proprietățile unui obiect standard al grupului FreeCAD și a obiectelor Arch. Este deosebit de potrivit pentru a reprezenta un întreg sit de proiect sau teren. În cazul lucrărilor arhitecturale bazate pe IFC, se utilizează cea mai mare parte pentru a vă organiza modelul, conținând obiecte [building](Arch_Building.md). Site-ul este, de asemenea, folosit pentru a gestiona și a afișa un teren fizic și poate calcula volumul de pământ care trebuie adăugat sau eliminat.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Optionally, select one or more objects to be included in your new site
2.  Press the **<img src="images/Arch_Site.png" width=16px> '''Arch Site'''** button, or press the **S** then **I** keys


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   After creating a site, you can add more objects to it by drag and dropping them in the Tree View or by using the <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Arch Add](Arch_Add.md) tool. This only determines which object is part of the given site, and has no effect on the terrain itself.
-   You can remove objects from a site by drag and dropping them out of it the Tree View or by using the <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Arch Remove](Arch_Remove.md) tool
-   You can add a terrain object by editing the Site\'s **Terrain** property. The terrain must be an open shell or surface.
-   You can add volumes to be added or subtracted from the base terrain, by double-clicking the Site, and adding objects to its Subtractions or Additions groups. The objects must be solids.
-   The **Extrusion Vector** property can be used to solve some problems that can appear when working with subtractions and additions. In order to perform those additions/subtractions, the terrain surface is extruded into a solid, which is then appropriately unioned/subtracted. Depending on the terrain topology, this extrusion might fail with the default extrusion vector. You might therefore be able to remedy the problem by changing this to a different value.


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

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

-    **North Deviation**: The angle between the true North and the north direction in this document

-    **Solar Diagram**: Shows or hides the solar diagram

-    **Solar Diagram Color**: The color of the solar diagram

-    **Solar Diagram Position**: The position of the solar diagram

-    **Solar Diagram Scale**: The scale of the solar diagram


</div>

### View

-    **Solar Diagram**: Shows or hides the solar diagram

-    **Solar Diagram Color**: The color of the solar diagram

-    **Solar Diagram Position**: The position of the solar diagram

-    **Solar Diagram Scale**: The scale of the solar diagram

-    **Wind Rose**: Shows or hides the wind rose diagram (requires the **EPW File** data property filled, and the Ladybug Python module installed (see below)

## Typical workflow 


<div class="mw-translate-fuzzy">

Start by creating an object that represents your terrain. It must be an open surface, not a solid. For example, it is easy to import mesh data, that can be turned into a Part Shape from menu **Part -\> Create Shape from Mesh\...**. Then, create a Site object, and set its **Terrain** property to the Part we just created:


</div>

![](images/Arch_site_example_01.jpg )

Create some volumes (they must be solids) that represent the areas that you wish to be excavated or filled. Double-click the Site object in the Tree View, and add these volumes to the Additions or Subtractions groups. Click OK.

![](images/Arch_site_example_02.jpg )

The site geometry will be recomputed and the areas, perimeter, and volumes properties recalculated.

![](images/Arch_site_example_03.jpg )


<div class="mw-translate-fuzzy">

## Solar diagram 


</div>


<div class="mw-translate-fuzzy">

If [pysolar](http://pysolar.org/) is installed on your system, Arch Sites can display a solar diagram. For this, **Longitude**, **Latitude** and **NorthDeviation** properties must be correctly set, and **SolarDiagram** view property turned on. <small>(v0.17)</small> 


</div>

**Note**: If you don\'t have Ladybug, [pysolar](http://pysolar.org/) is still supported to generate solar diagrams, but not wind roses. Pysolar 0.7 or above is required; this version only works with Python 3. If you require this feature with Python 2, you should have Pysolar 0.6 as this is the last version that works with Python 2. However, Ladybug is a much more powerful tool that will probably be used more in the future, so we recommend using it instead of pysolar. Ladybug can be installed simply via [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Site poate fi utilizat în [macros](macros.md) și de la consola python utilizând următoarele funcții:


</div>


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```


<div class="mw-translate-fuzzy">

creează un site incluzând obiectele din lista dată.


</div>

Exempluː 
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


<div class="mw-translate-fuzzy">

O diagramă de însorire poate fi creată cu :


</div>


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


{{docnav|[Building](Arch_Building.md)|[Reference](Arch_Reference.md)|[Arch](Arch_Workbench/ro.md)|IconL=Arch_Building.svg |IconC=Workbench_Arch.svg |IconR=Arch_Reference.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Site/ro
