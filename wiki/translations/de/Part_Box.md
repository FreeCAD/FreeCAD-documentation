---
- GuiCommand:/de
   Name:Part Quader
   MenuLocation:Formteil → Grundkörper → Würfel 
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundkörper](Part_Primitives/de.md)
---

## Beschreibung

Der Würfel-Befehl aus dem [Part-Arbeitsbereich](Part_Workbench/de.md) fügt einen parametrischen [Quader](https://de.wikipedia.org/wiki/Quader)förmigen geometrischen Grundkörper in das aktive Dokument ein. Als Standardvorgabe wird der Würfel-Befehl einen 10x10x10mm-Würfel am Ursprung mit der Bezeichnung \"Cube\" einfügen. Diese Parameter können nach dem Hinzufügen verändert werden.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Anwendung

1.  Wechsle zum <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Arbeitsbereich](Part_Workbench/de.md)
2.  Aufrufen des Befehls auf verschiedene Weise:
    -   Drücke die **<img src="images/Part_Box.svg" width=16px> Würfel**Schaltfläche in der Werkzeugleiste.
    -   Wähle den {{MenuCommand/de|Part → Grundkörper → <img src="images/Part_Box.svg" width=16px> Würfel}} in der Menüleiste.

**Ergebnis:** Das Standardergebnis ist ein Würfel mit gleicher Länge, Breite und Höhe von 10mm. Er steht auf der xy-Ebene und hat eine gemeinsame Kante mit der z-Achse.

Die Würfeleigenschaften können später geändert werden, entweder im Eigenschaftseditor oder durch doppelklicken des Würfels in der Baumansicht.

## Eigenschaften


{{Properties_Title|Base}}

-    **Placement**: Gibt die Ausrichtung und Position des Würfels im 3D-Raum an. Siehe [Positionierung](Placement/de.md). Der Referenzpunkt ist die vordere linke untere Ecke des Würfels.

-    **Label**: Das Label ist der zugeordnete Name der Operation. Dieser Name kann nach Belieben geändert werden.


{{Properties_Title|Box}}

-    **Length**: Die Länge des Würfel-Objekts in X-Richtung.

-    **Width**: Die Breite des Würfel-Objekts in Y-Richtung.

-    **Height**: Die Höhe des Würfel-Objekts in Z-Richtung.

![Formteil\_Würfel-Eigenschaften](images/Part_Box-Properties.jpg )

## Scripting

Der Würfel-Befehl kann mit [Makros](Macros/de.md) und von der Python-Konsole aus mithilfe der folgenden Funktion verwendet werden: 
```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Wobei \"myBox\" die Bezeichnung für das Würfel-Objekt ist.
-   Liefert das neu erstellte Objekt vom Typ \'Box\' zurück.

Du kannst die Attribute des Box-Objekts ansehen und verändern. Du kannst beispielsweise die Werte für Länge, Breite und Höhe ändern. 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

Du kannst die Position wählen mit: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```





 
