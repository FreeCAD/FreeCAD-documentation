---
 GuiCommand:
   Name: Draft PointArray
   Name/de: Draft PunktAnordnung
   MenuLocation: Änderung , Array tools ,  Punkt-Anordnung
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Version: 0.18
   SeeAlso: Draft_OrthoArray/de, Draft_PolarArray/de, Draft_CircularArray/de, Draft_PathArray/de, Draft_PathLinkArray/de, Draft_PointLinkArray/de
---

# Draft PointArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> **Draft Punkt-Anordnung** erstellt eine regelmäßige Anordnung aus einem ausgewählten Basisobjekt, indem er Kopien auf den Punkten eines Punktobjekts positioniert. Der Befehl [Draft PunktVerknüpfungsanordnung](Draft_PointLinkArray/de.md) erstellt alternativ eine effizientere Verknüpfungsanordnung ([Link](App_Link/de.md)-Array). Außer der Art der Anordnung die erstellt wird, normale Anordnung oder Verknüpfungsanordnung, ist der Befehl [Draft PunktVerknüpfungsanordnung](Draft_PointLinkArray/de.md) identisch mit diesem Befehl.

Das Basisobjekt kann ein 2D-Objekt sein, das mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench.md) erstellt wurde, aber auch ein 3D-Objekt, das mit den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erstellt wurde.

Das Punktobjekt kann ein beliebiges Objekt mit einer Form und Knotenpunkten sein (einschließlich einem [Std Part](Std_Part/de.md), das ein oder mehrere solcher Objekte enthält), ein [Netz-Objekt](Mesh_Workbench/de.md) oder eine [Punktewolke](Points_Workbench/de.md). Doppelte Punkte im Punktobjekt werden herausgefiltert. {{Version/de|0.21}}

In {{VersionMinus/de|0.20}} wird nur der Typ Drei-Punkt-Objekt unterstützt, siehe [Punkt-Objekt-Version 0.20 und älter](#Punkt-Objekt-Version_0.20_und_älter/de.md).

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Draft PunktAnordnung*



## Anwendung

1.  Das Objekt auswählen, das angeordnet werden soll.
2.  Das Punkt-Objekt zur Auswahl hinzufügen.
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_PointArray.svg" width=16px> [Punkt-Anordnung](Draft_PointArray/de.md)** drücken.
    -   Den Menüeintrag **Änderung → Anordnungswerkzeuge → <img src="images/Draft_PointArray.svg" width=16px> Punkt-Anordnung** auswählen.
4.  Die Anordnung wird erstellt.
5.  Wahlweise die [Eigenschaften](#Eigenschaften.md) der Anordnung im [Eigenschafteneditor](Property_editor/de.md) anpassen.



## Punkt-Objekt - Version 0.20 und älter 

Dies sind die unterstützten Punktobjekte in {{VersionMinus/de|0.20}} und wie sie erstellt werden können:

-   [Part Verbund](Part_Compound/de.md): Erzeugen einen oder mehrere [Entwurf Punkte](Draft_Point/de.md) oder [Part Punkte](Part_Point/de.md), wähle diese aus und rufe den Befehl [Part Verbund](Part_Compound/de.md) auf.
-   Zeichnungsblock: Erzeuge einen oder mehrere [Entwurf Punkte](Draft_Point/de.md) oder [Part Punkte](Part_Point/de.md), markiere diese und rufe den Befehl [Entwurf Heraufstufen](Draft_Upgrade/de.md) auf.
-   [Skizzierer Skizze](Sketcher_NewSketch/de.md): Erstelle eine [Skizze](Sketcher_NewSketch/de.md) und füge der Skizze einen oder mehrere [Skizzierer Punkte](Sketcher_CreatePoint/de.md) hinzu.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Eine Punkt-Anordnung (PointArray-Objekt) ist von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften (mit Ausnahme einiger Ansicht-Eigenschaften, die nicht an die Verknüpfungsanordnungen vererbt werden). Außerdem sind, wenn nicht anders angegeben, die folgenden zusätzlichen Eigenschaften vorhanden:



### Daten


{{TitleProperty|Link}}

Die Eigenschaften dieser Gruppe stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

-    {{PropertyData/de|Scale|Float}}
    

-    {{PropertyData/de|Scale Vector|Vector|Hidden}}
    

-    {{PropertyData/de|Scale List|VectorList}}
    

-    {{PropertyData/de|Visibility List|BoolList|Hidden}}
    

-    {{PropertyData/de|Placement List|PlacementList|Hidden}}
    

-    {{PropertyData/de|Element List|LinkList|Hidden}}
    

-    {{PropertyData/de|_ Link Touched|Bool|Hidden}}
    

-    {{PropertyData/de|_ Child Cache|LinkList|Hidden}}
    

-    {{PropertyData/de|Colored Elements|LinkSubHidden|Hidden}}
    

-    {{PropertyData/de|Link Transform|Bool}}
    


{{TitleProperty|Objects}}

-    **Base|Link**: specifies the object to duplicate in the array.

-    **Count|Integer**: (read-only) specifies the number of elements in the array. This number is determined by the number of points in the **Point Object**.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Extra Placement|Placement**: : specifies an additional [placement](Placement.md), translation and rotation, for each element in the array.

-    **Point Object|Link**: specifies the compound object whose points are used to position the elements in the array. The object must have a **Links**, **Components** or **Geometry** property, and contain at least one element with **X**, **Y**, and **Z** properties.



### Ansicht


{{TitleProperty|Link}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Display Options}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

Die Eigenschaften dieser Gruppe werden nicht an Verknüpfungsanordnungen vererbt.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://www.freecadweb.org/api) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Punktanordnung verwende die Methode `make_point_array` ({{Version/de|0.19}}) des Entwurf Moduls. Diese Methode ersetzt die veraltete Methode `makePointArray`.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `point_object`is the object containing the points. It can also be the `Label` (string) of an object in the current document. It should have a `Geometry`, `Links`, or `Components` property containing points.

-    `extra`is an `App.Placement`, an `App.Vector` or an `App.Rotation` that displaces each element.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/de
