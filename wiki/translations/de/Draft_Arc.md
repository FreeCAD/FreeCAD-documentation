---
- GuiCommand:/de
   Name:Draft Arc
   Name/de:Entwurf Bogen
   MenuLocation:Entwurf → Bogen
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Version:0.7
   SeeAlso:[Entwurf Kreis](Draft_Circle/de.md), [Entwurf Ellipse](Draft_Ellipse/de.md)
   Shortcut:**A** **R**
   SeeAlso:[Entwurf Kreis](Draft_Circle/de.md), [Entwurf Ellipse](Draft_Ellipse/de.md), [Entwurf Bogen 3Punkte](Draft_Arc_3Points/de.md)
---

# Draft Arc/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Bogen Werkzeug erstellt einen Kreisbogen in der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) durch Eingabe von vier Punkten, dem Mittelpunkt, dem Radius, dem ersten und letzten Punkt oder durch Auswahl von Tangenten oder einer Kombination von diesen. Es benutzt den [Entwurf Linienstil](Draft_Linestyle/de.md) auf den [Entwurf Tray](Draft_Tray/de.md) gesetzt.


</div>

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;"> 
*Bogen definiert durch vier Punkte, Mittelpunkt, Radius, Startpunkt und letzter Punkt des Bogens*

## Anwendung

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

## Anwendung 

1.  Drücke den **<img src="images/Draft_Arc.svg" width=16px> [Bogen](Draft_Arc/de.md)
** Taste oder drücke **A**, dann **R**
2.  Klicke einen ersten Punkt in der 3D Ansicht oder tippe eine [Koordinate](Draft_Coordinates/de.md) und drücke den **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** Taste.
3.  Klicke einen zweiten Punkt in der 3D Ansicht oder gib einen Wert für den Radius ein.
4.  Klicke einen dritten Punkt in der 3D Ansicht oder gib einen Startwinkel ein.
5.  Klicke einen vierten Punkt in der 3D Ansicht oder gib einen Öffnungswinkel ein.


</div>

## Optionen

Die im Aufgabenpaneel verfügbaren Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.


<div class="mw-translate-fuzzy">

## Optionen 

-   Die primäre Anwendung des Kreisbogen-Werkzeugs erfolgt durch Auswahl von vier Punkten: dem Mittelpunkt, einem Punkt auf dem Umkreis, dem Startwinkel und dem Endpunkt.
-   Durch Drücken von **Alt** kannst Du eine Tangente anstatt eines Punkts zur Definition des Basiskreises des Bogens auswählen. Du kannst deshalb verschiedene Kreisarten durch Auswahl von ein, zwei oder drei Tangenten erstellen.
-   Die Richtung des Kreisbogens hängt von der Bewegung Deiner Maus ab. Wenn Du sie nach Eingabe des dritten Punkts im Uhrzeigersinn bewegst, wird auch der Kreisbogen im Uhrzeigersinn erstellt. Um ihn gegen den Uhrzeigersinn zu erstellen, bewege die Maus einfach zurück über den dritten Punkt, bis der Kreisbogen in die andere Richtung gezeichnet wird.
-   Um Koordinaten manuell einzugeben, gibt einfach die Ziffern ein, drücke dann **Enter** zwischen den X-, Y- und Z-Komponenten. Du kannst den **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)**-Button drücken, wenn Du die gewünschten Werte zum Einfügen des Punkts hast.

-   Drücke **T** oder klicke das Ankreuzkästchen zum de/aktivieren des **'''Nächstes'''**-Buttons. Wenn der Fortsetzungsmodus aktiviert ist, wird das Kreisbogen-Tool nach Beenden des Bogens neugestartet, um das Zeichnen eines weiteren ohne erneutes Drücken des Werkzeug-Buttons zu ermöglichen.
-   Halte **Strg** während des Zeichnens, um das Einrasten Deines Punkts an der nächsten Einrastposition zu erzwingen, unabhängig vom Abstand.
-   Halte **Shift** während des Zeichnens, um Deinen Punkt horizontal oder vertikal in Relation zum Mittelpunkt einzuschränken.
-   Drücke **Esc** oder den **'''Schließen'''**-Button, um den aktuellen Linien-Befehl abzubrechen.


</div>

## Hinweise

-   Ein Bogen kann mit dem [Bearbeiten](Draft_Edit/de.md)-Befehl geändert werden.

## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Eigenschaften

Siehe [Draft Kreis](Draft_Circle/de#Properties.md).

## Skripten

Siehe auch: _.

Um einen Entwurf Bogen zu erstellen, verwende die Methode `make_circle` (<small>(v0.19)</small> ) des Entwurfmoduls. Diese Methode ersetzt die veraltete Methode `makeCircle`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/de
