---
- GuiCommand:/de
   Name:Part Box
   Name/de:Part Quader
   MenuLocation:Formteil → Grundkörper → Würfel 
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundkörper](Part_Primitives/de.md)
---

# Part Box/de

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Der Würfel-Befehl aus dem [Part-Arbeitsbereich](Part_Workbench/de.md) fügt einen parametrischen [Quader](https://de.wikipedia.org/wiki/Quader)förmigen geometrischen Grundkörper in das aktive Dokument ein. Als Standardvorgabe wird der Würfel-Befehl einen 10x10x10mm-Würfel am Ursprung mit der Bezeichnung \"Cube\" einfügen. Diese Parameter können nach dem Hinzufügen verändert werden.


</div>

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Usage


<div class="mw-translate-fuzzy">

## Anwendung

1.  Wechsle zum <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Arbeitsbereich](Part_Workbench/de.md)
2.  Aufrufen des Befehls auf verschiedene Weise:
    -   Drücke die **<img src="images/Part_Box.svg" width=16px> Würfel**Schaltfläche in der Werkzeugleiste.
    -   Wähle den {{MenuCommand/de|Part → Grundkörper → <img src="images/Part_Box.svg" width=16px> Würfel}} in der Menüleiste.


</div>

**Ergebnis:** Das Standardergebnis ist ein Würfel mit gleicher Länge, Breite und Höhe von 10mm. Er steht auf der xy-Ebene und hat eine gemeinsame Kante mit der z-Achse.

Die Würfeleigenschaften können später geändert werden, entweder im Eigenschaftseditor oder durch doppelklicken des Würfels in der Baumansicht.

## Properties


{{Properties_Title|Box}}


<div class="mw-translate-fuzzy">


{{Properties_Title|Box}}

-    **Length**: Die Länge des Würfel-Objekts in X-Richtung.

-    **Width**: Die Breite des Würfel-Objekts in Y-Richtung.

-    **Height**: Die Höhe des Würfel-Objekts in Z-Richtung.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scripting 

Der Würfel-Befehl kann mit [Makros](Macros/de.md) und von der Python-Konsole aus mithilfe der folgenden Funktion verwendet werden:


</div>


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

-   Wobei \"myBox\" die Bezeichnung für das Würfel-Objekt ist.
-   Liefert das neu erstellte Objekt vom Typ \'Box\' zurück.


</div>


<div class="mw-translate-fuzzy">

Du kannst die Attribute des Box-Objekts ansehen und verändern. Du kannst beispielsweise die Werte für Länge, Breite und Höhe ändern.


</div>


```python
box.Length = 25
box.Width = 15
box.Height = 30
```

Du kannst die Position wählen mit:


```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/de
