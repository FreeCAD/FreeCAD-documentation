---
 GuiCommand:
   Name: Part Primitives
   Name/de: Part Grundelemente
   MenuLocation: Formteil , Grundkörper erstellen...
   Workbenches: Part_Workbench/de, OpenSCAD_Workbench/de
   SeeAlso: Part_Builder/de
---

# Part Primitives/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> **Part Grundelemente** öffnet ein Dialogfeld zum Erstellen eines oder mehrerer parametrischer Grundelemente. 16 verschiedene Grundelemente (Körper und Linienelemente) stehen zur Verfügung.

<img alt="" src=images/Part_Primitives_example.png  style="width:600px;"> 
*Die Grundelemente, die mit dem Befehl erstellt werden können.*



## Anwendung



### Erstellung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Primitives.svg" width=16px> [Grundkörper erstellen...](Part_Primitives/de.md)** drücken.
    -   Den Menüeintrag **Part → <img src="images/Part_Primitives.svg" width=16px> Grundkörper erstellen...** auswählen.
2.  Das Aufgaben-Fenster **Geometrische Grundkörper** wird geöffnet.
3.  Einen Typ Grundkörper aus der Aufklappliste auswählen.
4.  Die Eigenschaften festlegen.
5.  Die Schaltfläche **Erstellen** drücken.
6.  Das Grundkörper-Objekt wird erstellt.
7.  Man beachte, dass das Aufgaben-Fenster geöffnet bleibt.
8.  Wahlweise weitere Grundkörper erstellen.
9.  Die Schaltfläche **Schließen** drücken, um das Aufgaben-Fenster zu schließen und den Befehl fertigzustellen.



### Bearbeiten

1.  Auf das Grundkörperobjekt in der [Baumansicht](Tree_view/de.md) doppelklicken.
2.  Der Aufgabenbereich **Geometrische Grundkörper** wird geöffnet.
3.  Eine oder mehrere Eingenschaften ändern.
4.  Das Objekt wird in der [3D-Ansicht](3D_view/de.md) dynamisch aktualisiert.
5.  Die Schaltfläche **OK** drücken.

Die Eigenschaften eines Part-Grundkörpers können auch im [Eigenschafteneditor](Property_editor/de.md) geändert werden und seine {{PropertyData/de|Placement}} kann auch mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md) geändert werden.



## Geometrische Grundelemente 

Die folgenden Grundelemente können erstellt werden:

-   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Ebene](Part_Plane/de.md): Erstellt eine Ebene.
-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Quader](Part_Box/de.md): Erstellt einen Quader. Dieses Objekt kann auch mit dem Werkzeug [Würfel](Part_Box/de.md) erstellt werden.
-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder/de.md): Erstellt einen Zylinder. Dieses Objekt kann auch mit dem Werkzeug [Zylinder](Part_Cylinder/de.md) erstellt werden.
-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Kegel](Part_Cone/de.md): Erstellt einen Kegel. Dieses Objekt kann auch mit dem Werkzeug [Kegel](Part_Cone/de.md) erstellt werden.
-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Kugel](Part_Sphere/de.md): Erstellt eineKugel. Dieses Objekt kann auch mit dem Werkzeug [Kugel](Part_Sphere/de.md) erstellt werden.
-   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid/de.md): Erstellt ein Ellipsoid.
-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus/de.md): Erstellt einen Torus. Dieses Objekt kann auch mit dem Werkzeug [Torus](Part_Torus/de.md) erstellt werden.
-   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/de.md): Erstellt ein Prisma.
-   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Keil](Part_Wedge/de.md): Erstellt einen Keil.
-   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix/de.md): Erstellt eine Wendel.
-   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/de.md): Erstellt eine Spirale.
-   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Kreis](Part_Circle/de.md): Erstellt einen Kreisbogen.
-   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/de.md): Erstellt einen Ellipsenbogen.
-   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point/de.md): Erstellt einen Punkt.
-   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line/de.md): Erstellt eine Linie.
-   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regelmäßiges Polygon](Part_RegularPolygon/de.md): Erstellt ein regelmäßiges Vieleck.



## Hinweise

-   Der Befehl Part Grundkörper kann keinen <img alt="" src=images/Part_Tube.svg  style="width:16px;"> [Part Hohlzylinder erstellen](Part_Tube.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Es gibt ein Python-Skript, um die Erstellung von Grundkörpern zu testen. Es kann von der [Python-Konsole](Python_console/de.md) gestartet werden:


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Dieses Skript befindet sich im Installationsverzeichnis des Programms und kann untersucht werden, um zu sehen, wie die einfachsten Grundelemente aufgebaut werden:


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

Es kann auch als Eingabe für das Programm verwendet werden:


```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/de
