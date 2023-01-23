---
- GuiCommand:/de
   Name:Part Primitives
   Name/de:Part Grundelemente
   MenuLocation:Formteil → Grundkörper erstellen...
   Workbenches:[Part](Part_Workbench/de.md), [OpenSCAD](OpenSCAD_Workbench/de.md)
   SeeAlso:[Part Formgenerator](Part_Builder/de.md)
---

# Part Primitives/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> **Part Grundelemente** öffnet ein Dialogfeld zum Erstellen eines oder mehrerer parametrischer Grundelemente. 16 verschiedene Grundelemente (Körper und Linienelemente) stehen zur Verfügung.

<img alt="" src=images/Part_Primitives_example.png  style="width:600px;"> 
*Die Grundelemente, die mit dem Befehl erstellt werden können.*



## Anwendung



### Erstellung


<div class="mw-translate-fuzzy">

Um ein Grundelement zu erstellen, entweder

#\* drücke die **<img src="images/Part_Primitives.svg" width=24px> '''Erstelle Grundelement'''** Schaltfläche in der Werkzeugleiste.

#\* wähle den {**Part → Grundelement erstellen...**} in der Menüleiste.

#\* Wähle im erscheinenden Dialogfeld den Grundelementtyp, stelle seine Parameter und seinen Speicherort ein und drücke schließlich **Erstellen**. Der Dialog bleibt offen, so dass du anschließend weitere Grundelemente erstellen kannst.


</div>



### Bearbeiten


<div class="mw-translate-fuzzy">

Verwendung des Dialogs: <small>(v0.19)</small> 

1.  Wähle das Grundelement im Baum aus und doppelklicke darauf.
2.  Das gleiche Dialogfeld wird geöffnet, das auch zum Erstellen des Grundelements verwendet wurde. Ändere dort die Parameter und du erhältst eine Live Vorschau des geänderten Grundelements.
3.  Um die Bearbeitung abzuschließen, drücke **OK**.


</div>

The properties of a Part Primitive can also be changed in the [Property editor](Property_editor.md), and its **Placement** can also be changed with the <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std TransformManip](Std_TransformManip.md) command.



## Geometrische Grundelemente 


<div class="mw-translate-fuzzy">

Einige der verfügbaren (parametrischen) geometrischen Grundelemente, die möglich sind:

:   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Ebene](Part_Plane/de.md): fügt eine einfache parametrische Ebene 10 x 10 mm mit den Parametern Position, Länge und Breite ein.
:   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Kasten/Würfel](Part_Box/de.md): fügt einen parametrischen, [rechteckiger Quader](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), geometrisches Grundelement in das aktive Dokument ein.
:   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Zylinder](Part_Cylinder/de.md): Fügt einen einfachen parametrischen Zylinder mit den Parametern Position, Winkel, Radius und Höhe in das aktive Dokument ein.
:   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Kegel](Part_Cone/de.md): Fügt einen parametrischen abgeschnittenen Kegel in das aktive Dokument ein.
:   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Kugel](Part_Sphere/de.md): Fügt eine parametrische Kugel ein, mit den Parametern Position, Winkel1, Winkel2, Winkel3 und Radius.
:   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid/de.md): Fügt einen parametrischen Ellipsoid Volumenkörper in das aktive Dokument ein.
:   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Torus](Part_Torus/de.md): Fügt einen einfachen parametrischen Torus mit Position, Winkel1, Winkel2, Winkel3, Radius1 und Radius2 als Parameter in das aktive Dokument ein.
:   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/de.md): Fügt einen Volumenkörper, der durch einen regelmäßigen Polygonquerschnitt und eine Höhe definiert ist, in das aktive Dokument ein. <small>(v0.14)</small> 
:   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Keil](Part_Wedge/de.md): Fügt ein parametrisches Keilobjekt in das aktive Dokument ein.
:   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix/de.md): Fügt ein geometrisches Helix Grundelement in das aktive Dokument ein. Übliche Verwendung für Helix ist die Erstellung von [Gewinde](Thread_for_Screw_Tutorial/de.md).
:   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/de.md): Fügt ein geometrisches Spiral Grundelement in den aktiven Arbeitsbereich ein. <small>(v0.14)</small> 
:   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Kreis](Part_Circle/de.md): Fügt eine kreisförmig gekrümmte Kante in das aktive Dokument ein.
:   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/de.md): Fügt eine elliptisch gekrümmte Kante in das aktive Dokument ein.
:   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punkt](Part_Point.md) (Knoten): Fügt ein geometrisches Punkt (Knoten) Grundelement in das aktive Dokument ein.
:   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Linie](Part_Line/de.md) (Kante): erzeugt ein einfaches Liniensegment, das von zwei Eckpunkten begrenzt wird.
:   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regelmäßiges Polygon](Part_RegularPolygon/de.md): Fügt ein geometrisches RegelmäßigesPolygon Grundelement in das aktive Dokument ein. <small>(v0.14)</small> 


</div>



## Hinweise

-   The Part Primitives command cannot create a <img alt="" src=images/Part_Tube.svg  style="width:16px;"> [Part Tube](Part_Tube.md).



## Skripten

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Part scripting](Part_scripting.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Teste die Erstellung der Grundkörper mit einem Skript. <small>(v0.19)</small> 


</div>


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```


<div class="mw-translate-fuzzy">

Dieses Skript befindet sich im Installationsverzeichnis des Programms und kann untersucht werden, um zu sehen, wie die Basisgrundelemente aufgebaut sind.


</div>


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```


<div class="mw-translate-fuzzy">

Es kann auch als Eingabe in das Programm verwendet werden.


</div>


```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/de
